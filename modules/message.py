import os
import sys
from random import randint  # For random answers.
from time import localtime

from basics import timeElapsed
from basics import splitIntoGroupsOf
from basics import cyrillicToLatin
import re

class Message():

  subSuppressions = {}

  ################################
  # Various checks and metadata. #
  ################################
  def contains(self, string):
    return re.match(".*" + string + ".*", self.text)
    
  def contains_caseInsensitive(self, string):
    return re.match(".*" + string.lower() + ".*", self.text.lower())
    
  def endsWith(self, string):
    return re.match(".*" + string + "$", self.text)
  
  def equals(self, string):
    return self.text == string

  def getID(self):
    return re.sub(".+?;id=([0-9]+).*", r'\1', self.meta)

  def getMeta(self):
    return re.sub("(.+?[A-Z]+ #[^ ]+).*", r'\1', self.fullText)

  # For continued subgifts.
  def getOriginalGifter(self):
    return re.sub(".+?;msg-param-sender-name=([^;]+).*", r'\1', self.meta)
 
  def getRaidersCount(self):
    return re.sub(".+?;msg-param-viewerCount=([^;]+).*", r'\1', self.meta)

  def getSenderLevel(self):
    if self.senderIsBroadcaster():
      return 4
    if self.senderIsMod():
      return 3
    if self.senderIsSubscriber():
      return 2
    if self.isFirstMsg():
      return 0
    # None of the above matches: user is an ordinary one.
    return 1

  def getSenderDisplayName(self):
    return re.sub(".+?;display-name=([^;]+).*", r'\1', self.meta)

  def getSenderName(self):
    return re.sub('.+?@(.*?)tmi\.twitch\.tv PRIVMSG #.*', r'\1', self.meta)

  def getSubGiftCount(self):
    return re.sub(".+?;msg-param-mass-gift-count=([^;]+).*", r'\1', self.meta)

  def getSubGiftCountTotal(self):
    return re.sub(".+?;msg-param-sender-count=([^;]+).*", r'\1', self.meta)

  def getSubGiftRecipient(self):
    return re.sub(".+?;msg-param-recipient-display-name=([^;]+).*", r'\1', self.meta)

  def getSubMonth(self):
    return re.sub(".+?;msg-param-cumulative-months=([^;]+).*", r'\1', self.meta)
  
  def getText(self):
    return re.sub(".+?[A-Z]+ #[^ ]+ :(.+)", r'\1', self.fullText)

  def getType(self):
    return re.sub(".+?tmi\.twitch\.tv ([A-Z]+) .*", r'\1', self.meta)

  def isFirstMsg(self):
    return ";first-msg=1;" in self.meta

  def isRaid(self):
    return ";msg-id=raid;" in self.meta

  def isSub(self):
    return (";msg-id=sub;" in self.meta) or (";msg-id=resub;" in self.meta)

  def isSubGiftContinued(self):
    return ";msg-id=giftpaidupgrade;" in self.meta

  def isSubGiftSingle(self):
    return ";msg-id=subgift;" in self.meta

  def isSubGiftMulti(self):
    return ";msg-id=submysterygift;" in self.meta and int(self.getSubGiftCount()) > 1

  def isSubPrime(self):
    return ";msg-param-sub-plan=Prime;" in self.meta

  def matchesRegex(self, regex):
    try:
      re.compile(regex)
      return re.match(regex, self.text)
    except:
      print("Regex error! Please check " + regex + ".")
    
  def senderIsBroadcaster(self):
    return "badges=broadcaster" in self.meta

  def senderIsMod(self):
    return ";mod=1;" in self.meta

  def senderIsSubscriber(self):
    return ";subscriber=1;" in self.meta

  def startsWith(self, string):
    return re.match("^" + string, self.text)  


  ##################################
  # More complex message handling. #
  ##################################
  def resolvePlaceholders(self, answerText):
    # Message is a raid notification.
    if self.isRaid():
      answerText = answerText.replace('$raidersChannel', self.getSenderDisplayName())
      answerText = answerText.replace('$raidersCount', self.getRaidersCount())
    # Message is a subscription (self).
    elif self.isSub() or self.isSubPrime():
      answerText = answerText.replace('$subMonth', self.getSubMonth())
      answerText = answerText.replace('$subName', self.getSenderDisplayName())
    # Message is a continued subscription.
    elif self.isSubGiftContinued():
      answerText = answerText.replace('$subName', self.getSenderDisplayName())
      answerText = answerText.replace('$subGiftGifter', self.getOriginalGifter())
    # Message is a subscription gift (single).
    elif self.isSubGiftSingle():
      answerText = answerText.replace('$subGiftGifter', self.getSenderDisplayName())
      answerText = answerText.replace('$subGiftRecipient', self.getSubGiftRecipient())
      answerText = answerText.replace('$subGiftCountTotal', self.getSubGiftCountTotal())
    # Message is a subscription gift (multiple).
    elif self.isSubGiftMulti():
      answerText = answerText.replace('$subGiftGifter', self.getSenderDisplayName())
      answerText = answerText.replace('$subGiftCountTotal', self.getSubGiftCountTotal())
      answerText = answerText.replace('$subGiftCount', self.getSubGiftCount())
    # Message is a user’s message or Prime Sub.
    else:
      answerText = answerText.replace('$msgID', self.getID())
      answerText = answerText.replace('$senderName', self.getSenderName())
      answerText = answerText.replace('$senderDisplayName', self.getSenderDisplayName())

    return answerText

  
  def resolveArguments(self, answerText):
    argsMsg = re.findall("[^ ]+", self.text)
    # Delete the command triggering the bot so that only the arguments remain.
    del argsMsg[0]

    argsAnswer = re.findall("\$arg[0-9]+", answerText)

    # If the command does not contain any arguments, but argument variables are used in the answer, …
    if len(argsMsg) == 0 and (len(argsAnswer) > 0 or re.match('.*\$arg@', answerText)):
      # … return an empty string, i.e. prevent the bot from reacting with a message.
      return ""

    else:
      answerText = answerText.replace("$arg@", " ".join(argsMsg))

      # Resolve the argument-gathering placeholder variables first.
      argsAnswer_gathered = re.findall("\$arg[0-9]+\+", answerText)
      for a in argsAnswer_gathered:
        i = re.sub('\$arg([0-9]+)\+', r'\1', a)
        # Copy the original message arguments to a new, temporary array.
        # Simple assignment will not copy but link the variables to each other.
        argsMsg_tmp = []
        for arg in argsMsg:
          argsMsg_tmp.append(arg)
        k = 0
        while len(argsMsg) > 0 and k < int(i):
          del argsMsg_tmp[0]
          k += 1
        answerText = answerText.replace(a, " ".join(argsMsg_tmp))
      
      # Resolve the single arguments.
      if len(argsMsg) >= len(argsAnswer):
        for i in range(0, len(argsAnswer)):
          answerText = answerText.replace("$arg" + str(i), argsMsg[i])
        return answerText
      else:
        return ""


  def reactToMessage(self, reaction, irc):
    # If the command contains an answer key, process its value.
    if 'answer' in reaction:
      answer = self.resolveArguments(reaction['answer'])
      answer = self.resolvePlaceholders(answer).split('\n')
      if len(answer) > 1:
        if 'answerType' in reaction and reaction['answerType'] == 'random':
          # Choose a random answer to send.
          answer = answer[randint(0, len(answer) - 1)]
          # Turn the answer into a list of chunks with a maximum of 500 characters.
          answer = splitIntoGroupsOf(answer, 500)
          for a in answer:
            irc.send(a)
        else:
          # Defaults to »sequence«.
          for a in answer:
            chunkList = splitIntoGroupsOf(a, 500)
            for c in chunkList:
              irc.send(c)
      else:
        answer = splitIntoGroupsOf(answer[0], 500)
        for a in answer:
          irc.send(a)

    # Execute the string in »os-command« as a system command.
    if 'os-command' in reaction:
      os.system(reaction['os-command'])

    # If there is a debug message provided, output this on the console.
    if 'debug' in reaction:
      answer = self.resolveArguments(reaction['debug'])
      answer = self.resolvePlaceholders(answer).split('\n')
      if len(answer) > 1:
        if 'answerType' in reaction and reaction['answerType'] == 'random':
          # Choose a random answer to send.
          answer = answer[randint(0, len(answer) - 1)]
          # Turn the answer into a list of chunks with a maximum of 500 characters.
          answer = splitIntoGroupsOf(answer, 500)
          for a in answer:
            print("    [debug]: " + a)
        else:
          # Defaults to »sequence«.
          for a in answer:
            chunkList = splitIntoGroupsOf(a, 500)
            for c in chunkList:
              print("    [debug]: " + c)
      else:
        answer = splitIntoGroupsOf(answer[0], 500)
        for a in answer:
          print("    [debug]: " + a)


  def processCommands(self, commands, message, irc):
    self.fullText = message
    self.meta = self.getMeta()
    #print(self.meta)
    msgTime = localtime()
    msgTime = ("" if msgTime.tm_hour > 9 else "0") + str(msgTime.tm_hour) + ":" + ("" if msgTime.tm_min > 9 else "0") + str(msgTime.tm_min) + ":" + ("" if msgTime.tm_sec > 9 else "0") + str(msgTime.tm_sec)

    # Response type is user’s chat message.
    if self.getType() == "PRIVMSG":
      # Convert Cyrillic letters to Latin ones to strike scam bots.
      self.text = cyrillicToLatin(self.getText())
      self.level = self.getSenderLevel()
      print(self.getSenderDisplayName() + " (lvl " + str(self.level) + ", " + msgTime + ")\n" + self.text + "\n—————")

      # Check for a match with the commands defined for this channel.
      match = ''
      for c in commands['general']:
        # User-triggered commands.
        # Set a default value for the match type if none is provided.
        if not 'matchType' in commands['general'][c]:
          commands['general'][c]['matchType'] = "is"
        if commands['general'][c]['matchType'] == "startsWith" and self.startsWith(c):
          match = c
          break
        if commands['general'][c]['matchType'] == "contains" and self.contains(c):
          match = c
          break
        if commands['general'][c]['matchType'] == "contains_caseInsensitive" and self.contains_caseInsensitive(c):
          match = c
          break
        if commands['general'][c]['matchType'] == "endsWith" and self.endsWith(c):
          match = c
          break
        if commands['general'][c]['matchType'] == "regex" and self.matchesRegex(c):
          match = c
          break
        if commands['general'][c]['matchType'] == "is" and self.text == c:
          match = c
          break
      
      # If there was a match, check more conditions.
      if match != '':        
        # Check if the command is in its cooldown.
        if 'cooldown' in commands['general'][match] and not timeElapsed(commands['general'][match], 'cooldown'):
          return
      
        # Check the fields minLevel …
        if 'minLevel' in commands['general'][match] and self.level < commands['general'][match]['minLevel']:
          return
      
        # … and level.
        if 'level' in commands['general'][match] and self.level != commands['general'][match]['level']:
          return

        # When this point is reached, the checks before have been passed.
        # The reaction to the command in the chat can finally be executed.
        self.reactToMessage(commands['general'][match], irc)


    elif self.getType() == "USERNOTICE":

      # Message indicates a Prime sub. Has to be checked first, because it has the same msg-id as ordinary subs do and the only distinguishing feature is the msg-param-sub-plan parameter.
      if self.isSubPrime():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subPrime':
            subMonth = self.getSubMonth()
            if ('subLevel' in commands['sub'][m] and subMonth == commands['sub'][m]['subLevel']) or ('minSubLevel' in commands['sub'][m] and subMonth >= commands['sub'][m]['minSublevel']) or (not 'subLevel' in commands['sub'][m] and not 'minSubLevel' in commands['sub'][m]):
              self.reactToMessage(commands['sub'][m], irc)
              break
        
      # Message indicates a subscription.
      elif self.isSub():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'sub':
            subMonth = self.getSubMonth()
            if ('subLevel' in commands['sub'][m] and subMonth == commands['sub'][m]['subLevel']) or ('minSubLevel' in commands['sub'][m] and subMonth >= commands['sub'][m]['minSublevel']) or (not 'subLevel' in commands['sub'][m] and not 'minSubLevel' in commands['sub'][m]):
              self.reactToMessage(commands['sub'][m], irc)
              break

      # Message indicates that a user continues his/her gifted sub.
      elif self.isSubGiftContinued():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftContinued':
            subMonth = self.getSubMonth()
            if ('subLevel' in commands['sub'][m] and subMonth == commands['sub'][m]['subLevel']) or ('minSubLevel' in commands['sub'][m] and subMonth >= commands['sub'][m]['minSublevel']) or (not 'subLevel' in commands['sub'][m] and not 'minSubLevel' in commands['sub'][m]):
              self.reactToMessage(commands['sub'][m], irc)
              break

      # Message indicates a gifted subscription.
      elif self.isSubGiftSingle():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftSingle':
            gifter = self.getSenderDisplayName()
            if gifter in self.subSuppressions:
              self.subSuppressions[gifter] -= 1
              print("Suppressing a followup single sub gift. " + str(self.subSuppressions[gifter]) + " more to come.")
              if self.subSuppressions[gifter] == 0:
                del self.subSuppressions[gifter]
                print("Followup counter deleted. Processing single sub gifts from " + gifter + " again.")
            else:
              self.reactToMessage(commands['sub'][m], irc)
            
            break

      # Message indicates a sub bomb i. e. multiple gifted subs.
      elif self.isSubGiftMulti():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftMulti':
            # If the followup single subs are set to be suppressed, …
            if 'suppressFollowupSingles' in commands['sub'][m] and commands['sub'][m]['suppressFollowupSingles']:
              # … create an entry for the multi sub gifting user in the subSuppressions dictionary
              gifter = self.getSenderDisplayName()
              self.subSuppressions[gifter] = int(self.getSubGiftCount())

            self.reactToMessage(commands['sub'][m], irc)
            break

      # Message indicates a raid.
      elif self.isRaid():
        raidersCount = self.getRaidersCount()
        for m in commands['raid']:
          if ('minRaidersCount' in commands['raid'][m] and raidersCount >= commands['raid'][m]['minRaidersCount']) or (not 'minRaidersCount' in commands['raid'][m]):
            self.reactToMessage(commands['raid'][m], irc)
            break
        
      else:
        print("\nUSERNOTICE\n")
        print(message)

    elif self.getType() == "USERSTATE":
      print("\nUSERSTATE\n")
      print(message)

    elif self.getType() == "NOTICE":
      print("\nNOTICE\n")
      print(message)

    else:
      if not re.match('^PING :tmi\.twitch\.tv$', self.meta) and not re.match("^:.*", self.meta):
        print("\n——— unclassified message ———\n", message)
