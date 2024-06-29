import importlib
import os
import platform
import re
import requests
import sys
import threading  # Asynchronous running of the local webserver for the token creation page.
import webbrowser # For opening the Twitch OAuth token generation page in the default web browser.

from oauthToken import startServer


##################
# Small helpers. #
##################

def inConfigMode():
  return '-sc' in sys.argv or '--set-config' in sys.argv or '-gc' in sys.argv or '--get-config' in sys.argv

def inDebugMode():
  return '-ds' in sys.argv or '--debug-single' in sys.argv or '-df' in sys.argv or '--debug-full' in sys.argv

def inHelpMode():
  return '-h' in sys.argv or '--help' in sys.argv

def inTokenMode():
  return '-t' in sys.argv or '--token' in sys.argv

def inOneshotMode():
  return inDebugMode() or inTokenMode() or inHelpMode() or inConfigMode()



######################################################
# More complex, actual CLI option related functions. #
######################################################


def createConfigFiles():
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict

  userOS = platform.system()
  if userOS == "Linux":
    configDir = os.path.join(os.path.expanduser("~"), ".config", "twitch", "willowbot")
  elif userOS == "Windows":
    configDir = os.path.join(os.getenv("APPDATA"), "twitch", "willowbot")
  elif userOS == "Darwin":
    configDir = os.path.join(os.path.expanduser("~"), "Library", "Preferences", "twitch", "willowbot")
  else:
    print(langDict['configFiles_osMismatch'].format(os = userOS))
    exit()

  if not os.path.exists(configDir):
    os.makedirs(configDir)
    os.makedirs(os.path.join(configDir, 'commands'))

  localeYes = re.match("^\[.\]", langDict['yesNo_prompt']) and re.findall("^\[(.)\]", langDict['yesNo_prompt'])[0] or "y"
  
  if os.path.exists(os.path.join(configDir, "config.py")):  
    print(langDict['configFiles_configFileAlreadyExists'].format(dir = configDir))
    answer = input(langDict['yesNo_prompt'] + ": ")
  else:
    answer = localeYes
  
  if answer == localeYes:
    # Create an empty file …
    configFile = open(os.path.join(configDir, "config.py"), 'w')
    # … and write a configuration template to it.
    configFile.write('config = {\n  \'botname\'                   : \'IAmYourFirstBot\',\n  \'clientID\'                  : \'e5kdpgd2bbnbj1u5gbjpzeq7vsgwup\',\n  \'connectionRetries\'         : 10,\n  \'disconnectCheckInterval\'   : 10,\n  \'port\'                      : 6697,\n  \'server\'                    : \'irc.chat.twitch.tv\'\n  \'cyrillicToLatinConversion\' : False}')
    configFile.close()
    # Generate the file here
    print(langDict['configFiles_newConfigFile'].format(optionalNew = langDict['new_female'] + " " if answer == localeYes else ""))
  else:
    print(langDict['configFiles_configFileUntouched'])

  if os.path.exists(os.path.join(configDir, "logins.py")):
    print(langDict['configFiles_loginsFileAlreadyExists'].format(dir = configDir))
    answer = input(langDict['yesNo_prompt'] + ": ")
  else:
    answer = localeYes
  
  if answer == localeYes:
    # Create an empty file …
    loginsFile = open(os.path.join(configDir, "logins.py"), 'w')
    # … and write a logins template to it.
    loginsFile.write('logins = {\n  \'IAmYourFirstBot\'  : \'1a2b3c4d5e6f7g8h9i\',\n  \'IAmYourSecondBot\' : \'9z8y7x6w5v4u3t2s1r\',\n}')
    loginsFile.close()
    # Generate the file here
    print(langDict['configFiles_newLoginsFile'].format(optionalNew = (answer == localeYes and (langDict['new_female'] + " ") or "")))
  else:
    print(langDict['configFiles_loginsFileUntouched'])

  exit()


def doDebugRunFull(chatMsg, commands):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict
  from debug import debugList
  for key in debugList:
    print("\n" + langDict['debug_full_testingInfo'].format(type = key))
    chatMsg.processCommands(commands, debugList[key], False)
    print("—" * 20)
  exit()


def doDebugRunSingle(chatMsg, commands):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict
  msgIndex = sys.argv.index("-ds" in sys.argv and "-ds" or "--debug-single") + 1
  msg = len(sys.argv) > msgIndex and sys.argv[msgIndex] or ""
  if msg == "":
    print(langDict['debug_single_noMessageError'])
  else:
    # Level 0 user message.
    PRIVMSG = '@badge-info=;badges=;client-nonce=1a2b3c4d5e6f7g8h9i;color=#008000;display-name=WillowbotDebugTester;emotes=555555560:83-84/555555584:114-115/1:31-32;first-msg=1;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=0;returning-chatter=0;room-id=123456789;subscriber=0;tmi-sent-ts=1658754900000;turbo=0;user-id=987654321;user-type= :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :'
    chatMsg.processCommands(commands, PRIVMSG + msg, None) # »None« replaces the irc argument. Abscence of this argument triggers the debug mode of message processing.
    # Level 1 user message.
    PRIVMSG = PRIVMSG.replace("first-msg=1", "first-msg=0")
    chatMsg.processCommands(commands, PRIVMSG + msg, None)
    # Level 2 user message.
    PRIVMSG = PRIVMSG.replace("subscriber=0", "subscriber=1")
    chatMsg.processCommands(commands, PRIVMSG + msg, None)
    # Level 3 user message.
    PRIVMSG = PRIVMSG.replace("mod=0", "mod=1")
    chatMsg.processCommands(commands, PRIVMSG + msg, None)
    # Level 4 user message.
    PRIVMSG = PRIVMSG.replace("badges=;", "badges=broadcaster;")
    chatMsg.processCommands(commands, PRIVMSG + msg, None)
  exit()


def getAvailableLanguages():
  availableLocales = []
  with os.scandir('./lang/') as files:
    for f in files:
      if f.is_file() and re.match(".*\.py$", f.name):
        availableLocales.append(f.name[:len(f.name)-3])
  return availableLocales


def getConfigValue():
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict

  userOS = platform.system()
  if userOS == "Linux":
    configDir = os.path.join(os.path.expanduser("~"), ".config", "twitch", "willowbot")
  elif userOS == "Windows":
    configDir = os.path.join(os.getenv("APPDATA"), "twitch", "willowbot")
  elif userOS == "Darwin":
    configDir = os.path.join(os.path.expanduser("~"), "Library", "Preferences", "twitch", "willowbot")

  if os.path.exists(os.path.join(configDir, "config.py")):
    sys.path.append(configDir)
    configData = importlib.import_module("config").config
    distinctKeyIndex = sys.argv.index("-gc" in sys.argv and "-gc" or "--get-config") + 1
    if len(sys.argv) > distinctKeyIndex:
      distinctKey = sys.argv[distinctKeyIndex]
      if distinctKey in configData:
        print("  " + distinctKey + ": " + str(configData[distinctKey]))
      else:
        print(langDict['config_get_noSuchKey'].format(key = distinctKey))
    else:
      for key in configData:
        print("  " + key + ":\n      " + str(configData[key]))
  else:
    print(langDict['config_get_noFile'].format(dir = configDir))

  exit()


def getLanguage(feedback = False):
  import locale
  osLocale = (locale.getlocale()[0])[0:2]
  argLocale = ""
  availableLocales = getAvailableLanguages()

  if '-lg' in sys.argv or '--language' in sys.argv:
    argIndex = sys.argv.index("-lg" in sys.argv and "-lg" or "--language")
    if len(sys.argv) <= argIndex + 1:
      feedback and print(" × WARNING! No language abbreviation passed to -lg/--language option. Using English.")
      return 'en'
    else:
      argLocale = sys.argv[argIndex + 1]
      if argLocale in availableLocales:
        return argLocale
      else:
        feedback and print(" × WARNING! There is no language file for the language abbreviation passed to Willowbot.")
        if argLocale != osLocale:
          feedback and print("   Trying your OS locale …")
          if osLocale in availableLocales:
            return osLocale
          else:
            feedback and print(" × WARNING! There is no locale for your OS language. Using English.")
            return 'en'
        else:
          feedback and print("   Using English.")
  else:
    if osLocale in availableLocales:
      return osLocale
    else:
      feedback and print(" × WARNING! There is no locale for your OS language. Using English.")
      return 'en'


def setConfigValue():
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict

  userOS = platform.system()
  if userOS == "Linux":
    configDir = os.path.join(os.path.expanduser("~"), ".config", "twitch", "willowbot")
  elif userOS == "Windows":
    configDir = os.path.join(os.getenv("APPDATA"), "twitch", "willowbot")
  elif userOS == "Darwin":
    configDir = os.path.join(os.path.expanduser("~"), "Library", "Preferences", "twitch", "willowbot")

  if os.path.exists(os.path.join(configDir, "config.py")):
    sys.path.append(configDir)
    configData = importlib.import_module("config").config
    distinctKeyIndex = sys.argv.index("-sc" in sys.argv and "-sc" or "--set-config") + 1
    if len(sys.argv) > distinctKeyIndex:
      distinctKey = sys.argv[distinctKeyIndex]
      if distinctKey in configData:
        if len(sys.argv) > distinctKeyIndex + 1:
          with open(os.path.join(configDir, "config.py"), "r") as f:
            content = f.read()
            # Replace the old value with the new one.
            content = re.sub('(\n *\')' + distinctKey + '(\'[^:]+:.*)' + str(configData[distinctKey]) + '(\'?,?\n)', '\g<1>' + distinctKey + '\g<2>' + str(sys.argv[distinctKeyIndex + 1]) + '\g<3>', content)
            # Write to a temporary file instead of to the original one so that the config file has a higher protection from corruption in case of writing errors.
            with open(os.path.join(configDir, "config_tmp.py"), "w") as tempFile:
              tempFile.write(content)
            # Delete the original config file and rename the new, formerly temporary one.
            os.remove(os.path.join(configDir, "config.py"))
            os.rename(os.path.join(configDir, "config_tmp.py"), os.path.join(configDir, "config.py"))
            print(langDict['config_set_valueUpdated'].format(key = distinctKey, oldValue = str(configData[distinctKey]), newValue = str(sys.argv[distinctKeyIndex + 1])))
        else:
          print(langDict['config_set_noNewValue'].format(key = distinctKey))
      else:
        print(langDict['config_set_noSuchKey'].format(key = distinctKey))
    else:
      print(langDict['config_set_noKeyProvided'])
  else:
    print(langDict['config_set_noFile'].format(dir = configDir))

  exit()


def showHelp():
  class markup:
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
  #os.system('echo "' + "Test" * 1000 + '" | ' + (os.name == 'posix' and 'less' or 'more'))

  from importlib import import_module
  
  langDict = import_module("lang.en").langDict | import_module("lang." + getLanguage()).langDict
  from basics import indentedWithWidth
  
  helpPages = markup.bold + langDict['usage'] + markup.end + "\n"
  helpPages += indentedWithWidth("main_cli.py [" + langDict['option'] + "]", 4)
  helpPages += "\n"
  helpPages += markup.bold + langDict['options'] + markup.end + "\n"
  helpPages += indentedWithWidth(markup.bold + "-c, --channel" + markup.end + " {" + langDict['channelName'] + "}", 4)
  helpPages += indentedWithWidth(langDict['help_info_channel'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-cf, --configure" + markup.end, 4)
  helpPages += indentedWithWidth(langDict['help_info_configure'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-df, --debug-full" + markup.end, 4)
  helpPages += indentedWithWidth(langDict['help_info_debug_full'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-ds, --debug-single" + markup.end + " '{" + langDict['message'] + "}'", 4)
  helpPages += indentedWithWidth(langDict['help_info_debug_single'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-gc, --get-config" + markup.end + " [" + langDict['configKey'] + "]", 4)
  helpPages += indentedWithWidth(langDict['help_info_config_get'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-h, --help" + markup.end, 4)
  helpPages += indentedWithWidth(langDict['help_info_help'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-l, --login" + markup.end + " {" + langDict['accountName'] + "}", 4)
  helpPages += indentedWithWidth(langDict['help_info_login'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-lg, --language" + markup.end + " {" + langDict['localeAbbreviation'] + "}", 4)
  helpPages += indentedWithWidth(langDict['help_info_language'].format(langList = ", ".join(getAvailableLanguages())), 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-sc, --set-config" + markup.end + " {" + langDict['configKey'] + "} {" + langDict['configValue'] + "}" , 4)
  helpPages += indentedWithWidth(langDict['help_info_config_set'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "-t, --token" + markup.end + " {" + langDict['keyword'] + "}", 4)
  helpPages += indentedWithWidth(langDict['help_info_token'], 8)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "add" + markup.end + " {" + langDict['name'] + "} {" + langDict['token'] + "}", 8)
  helpPages += indentedWithWidth(langDict['help_info_token_add'], 12)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "delete" + markup.end + " {" + langDict['name'] + "}", 8)
  helpPages += indentedWithWidth(langDict['help_info_token_delete'], 12)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "get" + markup.end, 8)
  helpPages += indentedWithWidth(langDict['help_info_token_get'], 12)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "list" + markup.end, 8)
  helpPages += indentedWithWidth(langDict['help_info_token_list'], 12)
  helpPages += "\n"
  helpPages += indentedWithWidth(markup.bold + "revoke" + markup.end + " {" + langDict['name'] + "}", 8)
  helpPages += indentedWithWidth(langDict['help_info_token_revoke'], 12)
  print(helpPages)
  exit()



def tokenActions(CONFIG, LOGINS):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + CONFIG['language']).langDict

  availableKeywords = ['add', 'delete', 'get', 'list', 'revoke']
  argIndex = sys.argv.index('-t' in sys.argv and '-t' or '--token')
  if len(sys.argv) > argIndex + 1:
    keyword = sys.argv[argIndex + 1]
    if not keyword in availableKeywords:
      print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_unknownOption'].format(options = ", ".join(availableKeywords)))

    elif keyword == "add":
      if len(sys.argv) <= argIndex + 2:
        print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_add_needName'].format(pythonExec = os.path.split(sys.executable)[-1], willowbotMain = sys.argv[0]))
      elif len(sys.argv) <= argIndex + 3:
        print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_add_needToken'].format(pythonExec = os.path.split(sys.executable)[-1], willowbowMain = sys.argv[0], name = sys.argv[argIndex + 2]))
      else:
        loginName = sys.argv[argIndex + 2]
        localeYes = re.match("^\[.\]", langDict['yesNo_prompt']) and re.findall("^\[(.)\]", langDict['yesNo_prompt'])[0] or "y"
        if loginName in LOGINS:
          print(langDict['tokenActions_add_loginAlreadyExists'].format(name = loginName))
          answer = input(langDict['yesNo_prompt'] + ": ")
        else:
          answer = localeYes
        if answer == localeYes:
          # Get the longest key in the logins file to be able to align the colons in the logins file later.
          maxExistingKeyLength = len(loginName)
          for l in LOGINS:
            maxExistingKeyLength = max(maxExistingKeyLength, len(l))
          with open(os.path.join(CONFIG['dir'], "logins.py"), "r") as f:
            content = f.read()
            # Remove the potentially present old key.
            content = re.sub('\n  \'' + sys.argv[argIndex + 2] + '\'[^\n]+\n', '\n', content)
            # Insert the new one.
            content = re.sub('\n *}.*', '\n  \'' + sys.argv[argIndex + 2] + '\' : \'' + sys.argv[argIndex + 3] + '\',\n}', content)
            # Eye candy: Aligning the colons in the logins file. {
            content = re.sub('\n  \'([^\']+)\' *', '\n  \'\g<1>\' ', content)
            matches = re.findall('\n  \'([^\']+)\'', content)
            for m in matches:
              content = re.sub('\n  \'' + m + '\'', '\n  \'' + m + '\'' + (" " * (maxExistingKeyLength - len(m))), content)
            # }
            # Write to a temporary file instead of to the original one so that the logins file has a higher protection from corruption in case of writing errors.
            with open(os.path.join(CONFIG['dir'], "logins_tmp.py"), "w") as tempFile:
              tempFile.write(content)
          # Delete the original logins file and rename the new, formerly temporary one.
          os.remove(os.path.join(CONFIG['dir'], "logins.py"))
          os.rename(os.path.join(CONFIG['dir'], "logins_tmp.py"), os.path.join(CONFIG['dir'], "logins.py"))
          print(langDict['tokenActions_add_successful'].format(name = sys.argv[argIndex + 2], token = sys.argv[argIndex + 3]))
        else:
          print(langDict['tokenActions_add_cancelled'])

    elif keyword == "delete":
      if len(sys.argv) <= argIndex + 2:
        print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_delete_needName'])
      else:
        loginName = sys.argv[argIndex + 2]
        if loginName in LOGINS:
          print(langDict['tokenActions_delete_revocationWarning'])
          answer = input(langDict['yesNo_prompt'] + ": ")
          localeYes = re.match("^\[.\]", langDict['yesNo_prompt']) and re.findall("^\[(.)\]", langDict['yesNo_prompt'])[0] or "y"
          if answer == localeYes:
            with open(os.path.join(CONFIG['dir'], "logins.py"), "r") as f:
              content = f.read()
              content = re.sub('\n *["\']' + loginName + '[\'"] +: +["\']' + LOGINS[loginName] + '["\'],? *\n', '\n', content)
              # Write to a temporary file instead of to the original one so that the logins file has a higher protection from corruption in case of writing errors.
              with open(os.path.join(CONFIG['dir'], "logins_tmp.py"), "w") as tempFile:
                tempFile.write(content)
            os.remove(os.path.join(CONFIG['dir'], "logins.py"))
            os.rename(os.path.join(CONFIG['dir'], "logins_tmp.py"), os.path.join(CONFIG['dir'], "logins.py"))
            print(langDict['tokenActions_delete_successful'])
          else:
            print(langDict['tokenActions_delete_cancelled'])
        else:
          print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_delete_nameNotFound'].format(name = loginName))
          
    elif keyword == "get":
      from modules.oauthToken import scopes
      from modules.oauthToken import baseURL
      fullURL = baseURL + "&client_id=" + CONFIG['clientID'] + "&scope=" + ("+".join(scopes))
      webbrowser.open(fullURL)
      serverThread = threading.Thread(target = startServer, args=("localhost", 3000))
      serverThread.start()

    elif keyword == "list":
      for l in LOGINS:
        print("  — " + l + ": " + LOGINS[l])

    elif keyword == "revoke":
      if len(sys.argv) <= argIndex + 2:
        print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_revoke_needName'])
      else:
        loginName = sys.argv[argIndex + 2]
        if loginName in LOGINS:
          response = requests.post(\
            "https://id.twitch.tv/oauth2/revoke",\
            headers = {"Content-Type" : "application/x-www-form-urlencoded"},\
            params = {"client_id" : CONFIG['clientID'], 'token': LOGINS[loginName]}\
          )
          if response.ok:
            with open(os.path.join(CONFIG['dir'], "logins.py"), "r") as f:
              content = f.read()
              content = re.sub('\n *["\']' + loginName + '[\'"] +: +["\']' + LOGINS[loginName] + '["\'],? *\n', '\n', content)
              with open(os.path.join(CONFIG['dir'], "logins_tmp.py"), "w") as tempFile:
                tempFile.write(content)
            os.remove(os.path.join(CONFIG['dir'], "logins.py"))
            os.rename(os.path.join(CONFIG['dir'], "logins_tmp.py"), os.path.join(CONFIG['dir'], "logins.py"))
            print(langDict['tokenActions_revoke_successful'])
          else:
            print(langDict['tokenActions_revoke_failed'], response.json())
        else:
          print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_revoke_nameNotFound'].format(name = loginName))

  else:
    print(" " + langDict['symbol_failure'] + " " + langDict['tokenActions_missingKeyword'].format(keywords = ", ".join(availableKeywords)))
  exit()
