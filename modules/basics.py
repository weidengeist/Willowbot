import importlib # For importing other python files, especially configuration.
import os.path   # Needed for various system path operations.
import platform  # Import module »platform« to be able to get the user’s operating system.
import re        # Regular expressions.
import requests  # Web requests.
import sys       
import time

from cliOptions import getLanguage

# Check for elapsed command time.
# Context: the dictionary entry with the command/string that triggers the answer.
# Modes: 'cooldown' (regular commands), 'interval' (timed commands).
def timeElapsed(context, mode):
  # Set the key »latestUseTime« when checking a timed command the very first time.
  if not 'latestUseTime' in context:
    if mode == "interval":
      # Timed commands are not supposed to trigger immediately after starting the bot,
      # so set the lastest use time to the currently elapsed time.
      context['latestUseTime'] = time.perf_counter()
    else:
      # Commands with cooldowns can be triggered immediately.
      context['latestUseTime'] = 0

  if time.perf_counter() - context[mode] > context['latestUseTime']:
    # Cooldown or interval time has elapsed and the command may be used/executed.
    context['latestUseTime'] = time.perf_counter()
    return 1


def indentedWithWidth(text, indent = 0, width = 80):
  indentedText = ""
  maxLineWidth = width - indent
  remainingText = re.sub(" +$", "", re.sub("^ +", "", text))
  while len(remainingText) > 0:
    chunk = remainingText[0:maxLineWidth]
    if re.match(".*[^ ]$", chunk) and " " in chunk and len(chunk) == maxLineWidth:
      chunk = re.sub("[^ ]+$", "", chunk)
    # Use .replace instead of re.sub here to prevent failure due to regex patterns in the chunk.
    remainingText = remainingText.replace(chunk, "", 1)
    remainingText = re.sub("^ *", "", remainingText)
    indentedText += " " * indent + chunk + "\n"
  return indentedText


def loadOptionalModules(lang = 'en', feedback = False):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict
  if os.path.exists("./modules_opt/activeModules"):
    activeModulesFile = open("./modules_opt/activeModules", "r")
    while True:
      line = activeModulesFile.readline()
      if line:
        line = re.findall("^[^#\n ]+", line)
        line = line[0] if len(line) > 0 else ""
        if line != "":
          feedback and print(" • " + langDict['optModules_importTrial'].format(module = line))
          if os.path.exists("./modules_opt/" + line + ".py"):
            module = importlib.import_module(line)
            # Determine a list of names to copy to the current namespace.
            names = getattr(module, '__all__', [n for n in dir(module) if not n.startswith('_')])
            # Copy those names into the current namespace.
            g = globals()
            for name in names:
              g[name] = getattr(module, name)
            feedback and print("     " + langDict['symbol_success'] + " " + langDict['optModules_loadingSuccessful'].format(module = line))
          else:
            feedback and print("     " + langDict['symbol_failure'] + " " + langDict['optModules_loadingFailed'].format(module = line))
      else:
        break
    activeModulesFile.close()


loadOptionalModules(feedback = False)


def getLogins(feedback = False):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict
  # Check the user’s operating system and set the configuration path.
  LOGINS = {}
  userOS = platform.system()
  if userOS == "Linux":
    loginsDir = os.path.join(os.path.expanduser("~"), ".config", "twitch", "willowbot")
  elif userOS == "Windows":
    loginsDir = os.path.join(os.getenv("APPDATA"), "twitch", "willowbot")
  elif userOS == "Darwin":
    loginsDir = os.path.join(os.path.expanduser("~"), "Library", "Preferences", "twitch", "willowbot")
  
  # Add the configuration path to the system paths to enable python to load configuration modules in this location.
  sys.path.append(loginsDir)
  
  # Load the logins file from the according path …
  if os.path.exists(os.path.join(loginsDir, "logins.py")):  
    loginsFromFile = importlib.import_module("logins").logins
    LOGINS = LOGINS | loginsFromFile
    feedback and print(" " + langDict['symbol_success'] + " " + langDict['logins_loadingSuccessful'].format(dir = loginsDir))
  # … or create an empty one if none exists yet.
  else:
    feedback and print(" " + langDict['symbol_failure'] + " " + langDict['logins_loadingFailed'].format(dir = loginsDir))
    exit()
  
  return LOGINS


def getRoleIDs(CONFIG, feedback = False):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict
  # Set some more config fields for enabling the bot to use Twitch API commands.
  # LEGACY: Check, if there is a clientID key (added on 2023-03-06) in the current configuration. Might be deleted in the long term.
  if 'clientID' in CONFIG:
    response = requests.get(CONFIG['URL_API'] + "users" + "?login=" + CONFIG['botname'] + "&login=" + CONFIG['channel'], headers = {'Authorization' : 'Bearer ' + CONFIG['oauth'], 'Client-Id' : CONFIG['clientID']})
    if response.ok:
      # Beware! Data retrieved via the request above don’t necessarily have the same order in the response as they had in the request.
      responseData = response.json()['data']
      for dataSet in responseData:
        if dataSet['login'] == CONFIG['botname'].lower():
          CONFIG['moderatorID'] = dataSet['id']
        if dataSet['login'] == CONFIG['channel'].lower():
          CONFIG['broadcasterID'] = dataSet['id']
      feedback and print(" " + langDict['symbol_success'] + " " + langDict['roles_retrievingSuccessful'].format(botname = CONFIG['botname'], moderatorID = CONFIG['moderatorID'], channel = CONFIG['channel'], broadcasterID = CONFIG['broadcasterID']))
    else:
      feedback and print(" " + langDict['symbol_failure'] + " " + langDict['roles_retrievingFailed'], response.json())
  else:
    feedback and print(" " + langDict['symbol_failure'] + " " + langDict['roles_missingClientID'])

  return CONFIG


def getConfig(feedback = False):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict
  # Check the user’s operating system and set the configuration path.
  CONFIG = {}
  CONFIG['language'] = getLanguage()
  CONFIG['URL_API'] = "https://api.twitch.tv/helix/"
  userOS = platform.system()
  if userOS == "Linux":
    CONFIG['dir'] = os.path.join(os.path.expanduser("~"), ".config", "twitch", "willowbot")
  elif userOS == "Windows":
    CONFIG['dir'] = os.path.join(os.getenv("APPDATA"), "twitch", "willowbot")
  elif userOS == "Darwin":
    CONFIG['dir'] = os.path.join(os.path.expanduser("~"), "Library", "Preferences", "twitch", "willowbot")
  
  # Add the configuration path to the system paths to enable python to load configuration modules in this location.
  sys.path.append(CONFIG['dir'])
  # Load the configuration file from the according path …
  if os.path.exists(os.path.join(CONFIG['dir'], "config.py")):  
    configFromFile = importlib.import_module("config").config
    # Check if the configuration set is complete.
    if 'port' in configFromFile and 'botname' in configFromFile and 'server' in configFromFile and 'clientID' in configFromFile:
      CONFIG = CONFIG | configFromFile
      feedback and print(" " + langDict['symbol_success'] + " " + langDict['config_loadingSuccessful'])
    else:
      print(langDict['config_loadingFailed_incomplete'].format(dir = CONFIG['dir']))
      exit()
  # … or create an empty one if none exists yet.
  else:
    print(" " + langDict['symbol_failure'] + " " + langDict['config_loadingFailed_missing'].format(dir = CONFIG['dir']))
    exit()

  LOGINS = getLogins(feedback = False)

  if '-l' in sys.argv or '--login' in sys.argv:
    potentialBotAccount = sys.argv[sys.argv.index("-l" in sys.argv and "-l" or "--login") + 1].lower()
  else:
    potentialBotAccount = CONFIG['botname']

  if potentialBotAccount != CONFIG['botname'] and not potentialBotAccount in LOGINS:
    feedback and print(" " + langDict['symbol_failure'] + " " + langDict['config_loginFailed_noOauth_tryDefault'].format(botname = potentialBotAccount))
    potentialBotAccount = CONFIG['botname']

  if potentialBotAccount in LOGINS:
    CONFIG['botname'] = potentialBotAccount
    CONFIG['oauth'] = LOGINS[potentialBotAccount]
    feedback and print(" " + langDict['symbol_success'] + " " + langDict['config_loginSuccessful'].format(botname = potentialBotAccount))
  else:
    feedback and print(" " + langDict['symbol_failure'] + " " + langDict['config_loginFailed_noOauth'].format(botname = potentialBotAccount))
    exit()
    
  if '-c' in sys.argv or '--channel' in sys.argv:
    channelIndex = sys.argv.index("-c" in sys.argv and "-c" or "--channel") + 1
    CONFIG['channel'] = len(sys.argv) > channelIndex and sys.argv[channelIndex].lower() or 'channel' in CONFIG and CONFIG['channel'].lower()

  CONFIG['channel'] = CONFIG['channel'] if 'channel' in CONFIG and CONFIG['channel'] != "" else CONFIG['botname'].lower()

  from cliOptions import inTokenMode
  if not inTokenMode():
    CONFIG = getRoleIDs(CONFIG, feedback = feedback)

  if CONFIG['channel'] != CONFIG['botname']:
    if CONFIG['channel'] in LOGINS:
      CONFIG['channelOauth'] = LOGINS[CONFIG['channel']]
      feedback and print(" " + langDict['symbol_success'] + " " + langDict['config_channelOauthFound'].format(channel = CONFIG['channel']))
    else:
      feedback and print(" " + langDict['symbol_failure'] + " " + langDict['config_channelOauthMissing'].format(channel = CONFIG['channel']))
  
  return CONFIG


def getCommands(config, feedback = False):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict

  commands = {}
  commands_timed = {}
  commands_sub = {}
  commands_raid = {}

  # A return status. 0 = import successful, 1 = no commands configuration file.
  status = 1

  # Load the command configuration file of the channel passed as an argument.
  if os.path.exists(os.path.join(config['dir'], 'commands', config['channel'] + ".py")):
    status = 0
    regexErrors = []
    sys.path.append(os.path.join(config['dir'], 'commands'))
    commandsModule = importlib.import_module(config['channel'])
    commands = commandsModule.commands
    
    # Create separate lists for timed commands, subscription messages, and raid messages.
    for c in commands.keys():
      # Check if the user’s regex in the command definition is correct.
      if 'matchType' in commands[c] and commands[c]['matchType'] == 'regex':
        try:
          re.compile(c)
        except Exception as ex:
          regexErrors.append([c,ex])
      if 'interval' in commands[c]:
        commands_timed[c] = {}
        for k in commands[c].keys():
          commands_timed[c][k] = commands[c][k]
      if 'triggerType' in commands[c] and re.match("^sub", commands[c]['triggerType']):
        commands_sub[c] = {}
        for k in commands[c].keys():
          commands_sub[c][k] = commands[c][k]
      if 'triggerType' in commands[c] and commands[c]['triggerType'] == 'raid':
        commands_raid[c] = {}
        for k in commands[c].keys():
          commands_raid[c][k] = commands[c][k]
    
    if len(regexErrors) > 0:
      print(langDict['regexError_listPrefix'])
      for e in regexErrors:
        print(langDict['regexError_listItem'].format(expression = e[0], error = str(e[1])))
      print(langDict['regexError_exitMessage'])
      exit()

    # Delete the various commands from the general commands list.
    # Not performed within the loop above as the list size must not change during iteration.
    for c in commands_timed:
      del commands[c]
    for c in commands_sub:
      del commands[c]
    for c in commands_raid:
      del commands[c]

    # Set a default match type for all general commands, if none has been provided.
    for c in commands:
      if not 'matchType' in commands[c]:
        commands[c]['matchType'] = "is"

    feedback and print(" " + langDict['symbol_success'] + " " + langDict['commands_loadingSuccessful'].format(channel = config['channel']))
  else:
    feedback and print(" " + langDict['symbol_failure'] + " " + langDict['commands_loadingFailed'].format(channel = config['channel']))

  return {'general' : commands, 'timed' : commands_timed, 'sub' : commands_sub, 'raid' : commands_raid, 'status' : status}
  

def channelIsOnline(channel, oauth, clientID):
  streamData = requests.get("https://api.twitch.tv/helix/streams/" , params = {"user_login" :  channel}, headers = {"Authorization" : "Bearer " + oauth, "Client-Id" : clientID}).json()
  if 'data' in streamData:
    if len(streamData['data']) > 0 and 'game_name' in streamData['data'][0]:
      return True
    else:
      return False
  else:
    print("TWITCH ERROR", "Could not get online status.")
    return False


def checkTimedCommands(commands_timed, irc):  
  # Check for elapsed intervals in timed commands.
  for c in list(commands_timed.keys()):
    if timeElapsed(commands_timed[c], 'interval'):
      if channelIsOnline(irc.config['channel'], irc.config['oauth'], irc.config['clientID']):
        reaction = commands_timed[c]
         # If the command contains an answer key, process its value.
        if 'answer' in reaction:
          answer = commands_timed[c]['answer'].split('\n')
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
    
        if 'function' in reaction:
          eval(reaction['function'])
    
        # If there is a debug message provided, output this on the console.
        if 'debug' in reaction:
          answer = reaction['debug'].split('\n')
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
      else:
        print("Channel offline. Skipping timed commands.")


# Used to split too long bot messages into chunks of a distinct character limit.
def splitIntoGroupsOf(s, length):
  finalStringsList = []
  while len(s) > 0:
    # Get the first $length characters.
    first = re.sub('^(.{0,' + str(length) + '}).*', r'\1', s)
    # If this string ends with a blank space or the the rest starts with a blank space, …
    if re.match(".* $", first) or re.match("^ +", s.replace(first, "")) or first == s:
      # … delete the last (potentially present) blank space(s) from this string.
      first = re.sub("(.*) +$", r'\1', first)
    else:
      # Only check further if the first string does not match the full one.
      if first != s:
        # If the »first« string contains spaces (i. e. contains of multiple words), just delete the last letters from this string.
        if " " in first:
          first = re.sub("(.*) +[^ ]+$", r'\1', first)
        # Otherwise, the word is too long to fit the restrictions, so omit it by setting it an empty string.
        else:
          first = ""
        
    # Only append the string of length at max 12 characters to the string if it actually exists.
    # Prevents infinite loops by words being longer than the character limit.
    if len(first) > 0:
      finalStringsList.append(first)
    else:
      # Delete the very first word in the remaining input string s if it is too long.
      first = re.sub("^([^ ]+).*", r'\1', s)
    
    # Use string.replace instead of re.sub to ensure replacement without stumbling over special regex patterns/characters.
    s = re.sub("^ *", "", s.replace(first, ""))

  return finalStringsList


# Convert Latin-like Cyrillic letters to real Latin ones to strike scam bots.
# Only apply those replacements in case of a mixture of Latin and Cyrillic letters.
def cyrillicToLatin(s):
  # Second regex match contains Cyrillic letters looking like Latin ones.
  if re.match(".*[A-Za-z]+.*", s) and re.match(".*[Ѕ-ј].*", s):
    replacementTable = [ ["А", "A"], ["В", "B"], ["С", "C"], ["Е", "E"],  ["Н", "H"], ["І", "I"], ["Ј", "J"], ["К", "K"], ["О", "O"], ["Р", "P"], ["Ѕ", "S"], ["Т", "T"], ["Х", "X"],
      ["а", "a"], ["с", "c"], ["е", "e"], ["і", "i"], ["ј", "j"], ["о", "o"], ["р", "p"], ["ѕ", "s"], ["х", "x"], ["у", "y"] ]
    for r in replacementTable:
      s = s.replace(r[0], r[1])
  return s
