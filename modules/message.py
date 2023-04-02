import os
import re
import sys
from random import randint  # For random answers.
from time import localtime

# Import all (*) variables and functions; needed to get all functions from optional modules loaded in the basics module.
from basics import *
from chatCommands import resolveChatCommands
from cliOptions import inOneshotMode
from cliOptions import getLanguage

# List the imported modules.
loadOptionalModules(getLanguage(), feedback = not inOneshotMode())

# Needed for evaluation of functions.
CONFIG = getConfig()


class Message():

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
    return re.sub(".+?;id=([^;]+);.*", r'\1', self.meta)

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

  def getSenderID(self):
    return re.sub(".+?;user-id=([^;]+).*", r'\1', self.meta)

  def getSenderName(self):
    return re.sub('.+?@(.*?).tmi\.twitch\.tv PRIVMSG #.*', r'\1', self.meta)

  def getSubGiftCount(self):
    return re.sub(".+?;msg-param-mass-gift-count=([^;]+).*", r'\1', self.meta)

  def getSubGiftCountTotal(self):
    return re.sub(".+?;msg-param-sender-count=([^;]+).*", r'\1', self.meta)

  def getSubGiftRecipient(self):
    return re.sub(".+?;msg-param-recipient-display-name=([^;]+).*", r'\1', self.meta)

  def getSubMonth_current(self):
    return 0 if ";subscriber=0" else re.sub("^\@badge[^/]+/([0-9]*);.*", r'\1', self.meta)
  
  def getSubMonth_new(self):
    return re.sub(".+?;msg-param-cumulative-months=([^;]+).*", r'\1', self.meta)
  
  def getText(self):
    return re.sub(".+?tmi\.twitch\.tv [A-Z]+ [^:]+:(.+)", r'\1', self.fullText)

  def getTimeSent(self):
    t_msg = re.findall(".+?;tmi-sent-ts=([0-9]+)[0-9]{3}.*", self.fullText)
    if len(t_msg) > 0:
      return localtime(int(t_msg[0]))
    else:
      return localtime()

  def getType(self):
    return re.sub(".+?tmi\.twitch\.tv ([A-Z]+) .*", r'\1', self.meta)

  def isFirstMsg(self):
    return ";first-msg=1;" in self.meta

  def isRaid(self):
    return ";msg-id=raid;" in self.meta

  def isSub(self):
    return ((";msg-id=sub;" in self.meta) or (";msg-id=resub;" in self.meta)) and not ";msg-param-sub-plan=Prime;" in self.meta

  def isSubGiftAnon(self):
    return ";login=ananonymousgifter;" in self.meta and ";msg-id=subgift;" in self.meta

  def isSubGiftContinued(self):
    return ";msg-id=giftpaidupgrade;" in self.meta

  def isSubGiftSingle(self):
    return ";msg-id=subgift;" in self.meta and not ";login=ananonymousgifter;" in self.meta and int(re.sub(".+?;msg-param-sender-count=([^;]+).*", r'\1', self.meta)) > 0

  def isSubGiftSingleFollowup(self):
    return ";msg-id=subgift;" in self.meta and not ";login=ananonymousgifter;" in self.meta and int(re.sub(".+?;msg-param-sender-count=([^;]+).*", r'\1', self.meta)) == 0

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
    return ";mod=1" in self.meta

  def senderIsSubscriber(self):
    return ";subscriber=1" in self.meta

  def senderIsVIP(self):
    return ";vip=1" in self.meta

  def startsWith(self, string):
    return re.match("^" + string, self.text)  


  ##################################
  # More complex message handling. #
  ##################################
  def resolvePlaceholders(self, answerText):
    # Message is a raid notification.
    if self.isRaid():
      answerText = answerText.replace('$raidersChannelName', self.getSenderDisplayName())
      answerText = answerText.replace('$raidersChannelID', self.getSenderID())
      answerText = answerText.replace('$raidersCount', self.getRaidersCount())
    # Message is a regular or Prime subscription.
    elif self.isSub() or self.isSubPrime():
      answerText = answerText.replace('$subMonth', self.getSubMonth_new())
      answerText = answerText.replace('$subName', self.getSenderDisplayName())
    # Message is an anonymous subscription.
    elif self.isSubGiftAnon():
      answerText = answerText.replace('$subGiftRecipient', self.getSubGiftRecipient())
    # Message is a continued subscription.
    elif self.isSubGiftContinued():
      answerText = answerText.replace('$subName', self.getSenderDisplayName())
      answerText = answerText.replace('$subGiftGifter', self.getOriginalGifter())
    # Message is a subscription gift (single).
    elif self.isSubGiftSingle() or self.isSubGiftSingleFollowup():
      answerText = answerText.replace('$subGiftGifter', self.getSenderDisplayName())
      answerText = answerText.replace('$subGiftRecipient', self.getSubGiftRecipient())
      answerText = answerText.replace('$subGiftCountTotal', self.getSubGiftCountTotal())      
    # Message is a subscription gift (multiple).
    elif self.isSubGiftMulti():
      answerText = answerText.replace('$subGiftGifter', self.getSenderDisplayName())
      answerText = answerText.replace('$subGiftCountTotal', self.getSubGiftCountTotal())
      answerText = answerText.replace('$subGiftCount', self.getSubGiftCount())
    # Message is a user’s message.
    else:
      answerText = answerText.replace('$msgText', self.text)
      answerText = answerText.replace('$msgMeta', self.meta)
      answerText = answerText.replace('$msgID', self.getID())
      answerText = answerText.replace('$senderName', self.getSenderName())
      answerText = answerText.replace('$senderDisplayName', self.getSenderDisplayName())
      answerText = answerText.replace('$senderID', self.getSenderID())

    return answerText

  
  def resolveCaptureGroups(self, pattern, replacement):
    try:
      replEncoded = re.sub("\\\\x([0-9]{2})", r"\\\\g<\1>", replacement.encode('unicode_escape').decode()).encode().decode('unicode_escape')
      # If there are no capture usages in the answer string, just return the answer string itself.
      if replEncoded == replacement:
        return replacement
      # Else capture the pattern from the sent message (self.text) and put it into the answer string, including capture group replacement.
      else:
        return re.sub(pattern, replEncoded, self.text)
    except Exception as err:
      print("  Regex resolve error! " + str(err))
      return self.text


  def resolveArguments(self, answerText):
    argsMsg = re.findall("[^ ]+", self.text)
    # Delete the command triggering the bot so that only the arguments remain.
    del argsMsg[0]

    argsAnswer = re.findall("\$arg[0-9]+", answerText)

    # If the command does not contain any arguments, but argument variables are used in the answer, …
    if len(argsMsg) == 0 and (len(argsAnswer) > 0 or re.match('.*\$arg@', answerText)):
      # … return the function-calling string with generic strings for non-resolvable arguments.
      return re.sub("\$arg[@0-9+]+", "", answerText)

    else:
      answerText = answerText.replace("$arg@", " ".join(argsMsg))

      # Resolve the argument-gathering placeholder variables first.
      argsAnswer_gathered = re.findall("\$arg[0-9]+\+", answerText)
      for a in argsAnswer_gathered:
        i = re.sub('\$arg([0-9]+)\+', r'\1', a)
        if int(i) < len(argsMsg):
          answerText = answerText.replace(a, " ".join(argsMsg[int(i):]))

      # Resolve the single arguments.
      for i in range(0, len(argsMsg)):
        answerText = answerText.replace("$arg" + str(i), argsMsg[i])
      
      # All the remaining arguments used in the answer string but not provided by the command are renamed to »missingArg«
      return re.sub("\$arg[@0-9+]+", "", answerText)


  # Added commands variable to the function as a »function« key might modify the commands.
  def reactToMessage(self, commands, subset, match, irc):
    # If the command contains an answer key, process its value.
    reaction = commands[subset][match]
    if 'answer' in reaction:
      if 'matchType' in reaction and reaction['matchType'] == 'regex':
        answer = self.resolveCaptureGroups(match, reaction['answer'])
      else:
        answer = reaction['answer']
      
      answer = self.resolveArguments(answer)
      answer = self.resolvePlaceholders(answer)

      # Prepare the answer for multi-answer responses or random answers.
      answer = answer.split('\n')
      if len(answer) > 1:
        if 'answerType' in reaction and reaction['answerType'] == 'random':
          # Choose a random answer to send.
          answer = answer[randint(0, len(answer) - 1)]
          if re.match("^/[^ ]+", answer):
            answer = resolveChatCommands(answer)
          # Turn the answer into a list of chunks with a maximum of 500 characters.
          answer = splitIntoGroupsOf(answer, 500)
          for a in answer:
            if irc:
              irc.send(a)
            else:
              print("DEBUG MODE, Willowbot’s answer:\n    " + a)
        else:
          # Defaults to »sequence«.
          for a in answer:
            if re.match("^/[^ ]+", a):
              a = resolveChatCommands(a)
            chunkList = splitIntoGroupsOf(a, 500)
            for c in chunkList:
              if irc:
                irc.send(c)
              else:
                print("DEBUG MODE, Willowbot’s answer:\n    " + c)
      else:
        answer = splitIntoGroupsOf(answer[0], 500)
        for a in answer:
          if re.match("^/[^ ]+", a):
            a = resolveChatCommands(a)
          if irc:
            irc.send(a)
          else:
            print("DEBUG MODE, Willowbot’s answer:\n    " + a)

    # Execute the string in »os-command« as a system command.
    if 'os-command' in reaction:
      os.system(reaction['os-command'])

    if 'function' in reaction:
      func = self.resolveArguments(reaction['function'])
      func = self.resolvePlaceholders(func)
      eval(func)

    # If there is a debug message provided, output this on the console.
    if 'debug' in reaction:
      if 'matchType' in reaction and reaction['matchType'] == 'regex':
        answer = self.resolveCaptureGroups(match, reaction['debug'])
      else:
        answer = reaction['debug']

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
    #print(self.fullText)
    self.text = self.getText()
    self.meta = self.getMeta()
    msgTime = self.getTimeSent()
    msgTime = ("" if msgTime.tm_hour > 9 else "0") + str(msgTime.tm_hour) + ":" + ("" if msgTime.tm_min > 9 else "0") + str(msgTime.tm_min) + ":" + ("" if msgTime.tm_sec > 9 else "0") + str(msgTime.tm_sec)

    # Response type is user’s chat message.
    if self.getType() == "PRIVMSG":
      # All the following code covers triggerType chat message.

      # Convert Cyrillic letters to Latin ones to strike scam bots.
      self.text = cyrillicToLatin(self.getText())
      senderLevel = self.getSenderLevel()
      print(self.getSenderDisplayName() + " (lvl " + str(senderLevel) + ", " + msgTime + ")\n" + self.text + "\n———————")

      # Iterate over all commands defined for this channel.
      # Using a while loop here as the number of entries in the dictionary may change during iteration.
      i = 0
      while i < len(list(commands['general'].keys())):
        c = list(commands['general'].keys())[i]
        i += 1
        
        # The following chain of checks will be either successful (»pass« in each check instance) or break at some point and »continue« with respectively jump to the next item in the commands loop. 
        
        # Check if the most recent chat message matches the command currently being processed as well as its matching type.
        if (commands['general'][c]['matchType'] == "startsWith" and self.startsWith(c)) or (commands['general'][c]['matchType'] == "contains" and self.contains(c)) or (commands['general'][c]['matchType'] == "contains_caseInsensitive" and self.contains_caseInsensitive(c)) or (commands['general'][c]['matchType'] == "endsWith" and self.endsWith(c)) or (commands['general'][c]['matchType'] == "regex" and self.matchesRegex(c)) or (commands['general'][c]['matchType'] == "is" and self.text == c) or (commands['general'][c]['matchType'] == "is_caseInsensitive" and self.text.lower() == c.lower()):
          pass
        else:
          continue

        # Check if the message that has to be reacted to has been sent by the specified user (login name), if any.
        if not 'senderName' in commands['general'][c] or ('senderName' in commands['general'][c] and self.getSenderName() in commands['general'][c]['senderName']):
          pass
        else:
          continue

        # Check if the message that has to be reacted to has been sent by the specified user (display name), if any.
        if not 'senderDisplayName' in commands['general'][c] or ('senderDisplayName' in commands['general'][c] and self.getSenderDisplayName() in commands['general'][c]['senderDisplayName']):
          pass
        else:
          continue

        # Check if the command has no cooldown or if its cooldown has already elapsed.
        if not 'cooldown' in commands['general'][c] or ('cooldown' in commands['general'][c] and timeElapsed(commands['general'][c], 'cooldown')):
          pass
        else:
          continue
        
        # Check if the user has the necessary level to use the command.
        if (not 'level' in commands['general'][c] and not 'minLevel' in commands['general'][c]) or ('level' in commands['general'][c] and senderLevel == commands['general'][c]['level']) or ('minLevel' in commands['general'][c] and senderLevel >= commands['general'][c]['minLevel']):
          pass
        else:
          continue

        # Check if the command is VIP-restricted and if the sender is indeed a VIP.
        if not 'needsVIP' in commands['general'][c] or ('needsVIP' in commands['general'][c] and commands['general'][c]['needsVIP'] and self.senderIsVIP()):
          pass
        else:
          continue

        # Checks if the command is subscription-level-restricted and if the sender meets those requirements.
        if (not 'subLevel' in commands['general'][c] and not 'minSubLevel' in commands['general'][c]) or ('subLevel' in commands['general'][c] and commands['general'][c]['subLevel'] == int(self.getSubMonth_current())) or ('minSubLevel' in commands['general'][c] and commands['general'][c]['minSubLevel'] >= int(self.getSubMonth_current())):
          pass
        else:
          continue

        # If all restrictions above have been met, the reaction is free to be executed. This point is not reached otherwise.
        self.reactToMessage(commands, 'general', c, irc)
        
    elif self.getType() == "USERNOTICE":

      # Message indicates a regular subscription.
      if self.isSub():
        subMonth = int(self.getSubMonth_new())
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'sub':
            subLevel = commands['sub'][m]['subLevel'] if 'subLevel' in commands['sub'][m] else 0 
            minSubLevel = commands['sub'][m]['minSubLevel'] if 'minSubLevel' in commands['sub'][m] else 0
            maxSubLevel = commands['sub'][m]['maxSubLevel'] if 'maxSubLevel' in commands['sub'][m] else float('inf') 
            if (subLevel == subMonth) or (minSubLevel <= subMonth and subMonth <= maxSubLevel and not 'subLevel' in commands['sub'][m]):
              self.reactToMessage(commands, 'sub', m, irc)

      # Message indicates a Prime sub.
      elif self.isSubPrime():
        subMonth = int(self.getSubMonth_new())
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subPrime':
            subLevel = commands['sub'][m]['subLevel'] if 'subLevel' in commands['sub'][m] else 0 
            minSubLevel = commands['sub'][m]['minSubLevel'] if 'minSubLevel' in commands['sub'][m] else 0
            maxSubLevel = commands['sub'][m]['maxSubLevel'] if 'maxSubLevel' in commands['sub'][m] else float('inf') 
            if (subLevel == subMonth) or (minSubLevel <= subMonth and subMonth <= maxSubLevel and not 'subLevel' in commands['sub'][m]):
              self.reactToMessage(commands, 'sub', m, irc)

      # Message indicates an anonymously gifted subscription.
      elif self.isSubGiftAnon():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftAnon':
            self.reactToMessage(commands, 'sub', m, irc)

      # Message indicates a continued gifted subscription.
      elif self.isSubGiftContinued():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftContinued':
            self.reactToMessage(commands, 'sub', m, irc)

      # Message indicates a gifted subscription.
      elif self.isSubGiftSingle():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftSingle':
            self.reactToMessage(commands, 'sub', m, irc)

      # Message indicates a followup message of a multi-gifted subscription.
      elif self.isSubGiftSingleFollowup():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftSingleFollowup':
            self.reactToMessage(commands, 'sub', m, irc)
      
      # Message indicates a sub bomb i. e. multiple gifted subs.
      elif self.isSubGiftMulti():
        for m in commands['sub']:
          if commands['sub'][m]['triggerType'] == 'subGiftMulti':
            self.reactToMessage(commands, 'sub', m, irc)

      # Message indicates a raid.
      elif self.isRaid():
        # All the following code covers triggerType raid.
        raidersCount = self.getRaidersCount()
        lowerBound = commands['raid'][m]['minRaidersCount'] if "minRaidersCount" in commands['raid'][m] else 0
        upperBound = commands['raid'][m]['maxRaidersCount'] if "maxRaidersCount" in commands['raid'][m] else float('inf')
        for m in commands['raid']:
          if  lowerBound <= raidersCount and raidersCount <= upperBound:
            self.reactToMessage(commands, 'raid', m, irc)
        
      else:
        print("\nUSERNOTICE\n")
        print(message)
  
    elif self.getType() == "CLEARCHAT":
      print("\nCLEARCHAT\n")
      print("    Message: " + message)

    elif self.getType() == "CLEARMSG":
      print("\nCLEARMSG\n")
      print("    Deleted message: " + message)

    elif self.getType() == "NOTICE":
      print("\nNOTICE\n")
      print(message)

    elif self.getType() == "RECONNECT":
      print("\nRECONNECT\n")
      print(message)

    elif self.getType() == "USERSTATE":
      print("\nUSERSTATE\n")
      print(message)

    elif self.getType() == "WHISPER":
      print("\nWHISPER\n")
      print(self.text)

    else:
      if not re.match('^PING :tmi\.twitch\.tv$', self.meta) and not re.match("^:.*", self.meta):
        print("\n——— unclassified message ———\n", message)
