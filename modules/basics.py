import importlib # For importing other python files, especially configuration.
import os.path   # Needed for various system path operations.
import platform  # Import module »platform« to be able to get the user’s operating system.
import re        # Regular expressions.
import sys       
import time


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
    context['latestUseTime'] = time.perf_counter()
    return 1


def loadOptionalModules(verbose):
  if os.path.exists("./modules_opt/activeModules"):
    activeModulesFile = open("./modules_opt/activeModules", "r")
    while True:
      line = activeModulesFile.readline()
      if line:
        line = re.findall("^[^#\n ]+", line)
        line = line[0] if len(line) > 0 else ""
        if line != "":
          verbose and print("Trying to import module " + line + ".")
          if os.path.exists("./modules_opt/" + line + ".py"):
            module = importlib.import_module(line)
            # Determine a list of names to copy to the current name space
            names = getattr(module, '__all__', [n for n in dir(module) if not n.startswith('_')])
            # Copy those names into the current name space
            g = globals()
            for name in names:
              g[name] = getattr(module, name)
            verbose and print("  " + line + " loaded successfully " + ".")
          else:
            verbose and print("  Could not load " + line + ". Not found.")
      else:
        break
    activeModulesFile.close()

# Initially load optional modules.
loadOptionalModules(True)

def getConfig():
  # Check the user’s operating system and set the configuration path.
  CONFIG = {}
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
    if 'port' in configFromFile and 'botname' in configFromFile and 'server' in configFromFile and 'oauth' in configFromFile:
      CONFIG = CONFIG | configFromFile
      CONFIG['status'] = 0
    else:
      CONFIG['status'] = 1
  # … or create an empty one if none exists yet.
  else:
    CONFIG['status'] = 2
    if not os.path.exists(CONFIG['dir']):
      os.makedirs(CONFIG['dir'])
      os.makedirs(os.path.join(CONFIG['dir'], 'commands'))
    # Create an empty file …
    configFile = open(os.path.join(CONFIG['dir'], "config.py"), 'w')
    # … and write a configuration template to it.
    configFile.write('config = {\n  "server"           : "irc.chat.twitch.tv",\n  "port"             : 6697,\n  "botname"          : "IHaveNoName",\n  "oauth"            : "1a2b3c4d5e6f7g8h9i",\n  "connectionRetries": 10\n}')
    configFile.close()

  # Channel where the bot is supposed to be used. Bot’s own channel as fallback (i.e. no argument passed).
  # 'channel' default may be set in the config.py file.
  if not 'channel' in CONFIG:
    CONFIG['channel'] = len(sys.argv) > 1 and sys.argv[1].lower() or ('botname' in CONFIG and CONFIG['botname'].lower())
  
  return CONFIG


def getCommands(config):
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
    
    # Create a separate list for timed commands.
    for c in commands.keys():
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
      print("There are errors in your following regular expressions:")
      for e in regexErrors:
        print("  — " + e[0] + "\n    Error: " + str(e[1]))
      print("\nWillowbot can only be run with correct patterns. Exit.")
      exit()

    # Delete the various commands from the general commands list.
    # Not performed within the loop above as the list size must not change during iteration.
    for c in commands_timed:
      del commands[c]
    for c in commands_sub:
      del commands[c]
    for c in commands_raid:
      del commands[c]

  return {'general' : commands, 'timed' : commands_timed, 'sub' : commands_sub, 'raid' : commands_raid, 'status' : status}
  

def checkTimedCommands(commands, commands_timed, irc):
  # Check for elapsed intervals in timed commands.
  for c in list(commands_timed.keys()):
    if timeElapsed(commands_timed[c], 'interval'):
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
        print("function", reaction['function'])
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


# Used to split too long bot messages into chunks of a distinct character limit.
def splitIntoGroupsOf(s, length):
  finalStringsList = []
  while len(s) > 0:
    # Get the first $length characters.
    first = re.sub('^(.{0,' + str(length) + '}).*', r'\1', s)
    # If this string ends with a blank space or the the rest starts with a blank space, …
    if re.match(".* $", first) or re.match("^ +", re.sub(first, "", s)) or first == s:
      # … delete the last (potentially present) blank space(s) from this string.
      first = re.sub("(.*) +$", r'\1', first)
    else:
      # Only check further if the first string does not match the full one.
      if first != s:
        # If the first string contains spaces, just delete the last letters from this string.
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
      
    s = re.sub("^" + first + " *", "", s)
    
  return finalStringsList

# Convert Latin-like Cyrillic letters to real Latin ones to strike scam bots.
def cyrillicToLatin(s):
  return s.replace("а", "a").replace("е", "e").replace("о", "o").replace("р", "p").replace("с", "c").replace("ѕ", "s").replace("і", "i").replace("ј", "j")
