import sys

# Subdirectories containing routines, class definitions and other important data.
sys.path.append('lang')
sys.path.append('modules')
sys.path.append('modules_opt')

# Load this module first to get the current language and to be able to shot the help info without having to load the actual config before.
from modules.cliOptions import *

getLanguage(feedback = True)

if '-h' in sys.argv or '--help' in sys.argv:
  showHelp()

if '-cf' in sys.argv or '--configure' in sys.argv:
  createConfigFiles()

if '-sc' in sys.argv or '--set-config' in sys.argv:
  setConfigValue()

if '-gc' in sys.argv or '--get-config' in sys.argv:
  getConfigValue()

# Load all the remaining modules.
from modules.basics import checkTimedCommands  # Import various general functions from the basics(.py) module in ./modules.
from modules.basics import getCommands    
from modules.basics import getConfig
from modules.basics import getIgnoredUsers 
from modules.basics import getLogins
from modules.irc import IRC                    # Import the IRC class from the irc(.py) module in ./modules.


# Suppress output in debug mode.
if inOneshotMode():
  globalFeedback = False
else:
  globalFeedback = True


LOGINS = getLogins(feedback = globalFeedback)   # Load all available login oauths.
CONFIG = getConfig(feedback = globalFeedback)   # Load configuration files. 


# Read the list of ignored users, i.e. users whose commands won’t be evaluated.
ignoredUsers = getIgnoredUsers(feedback = globalFeedback)


if '-t' in sys.argv or '--token' in sys.argv:
  tokenActions(CONFIG, LOGINS)


# Load the commands for the specified channel.
# Returns a dictionary with the keys 'general', 'timed', 'sub', and 'raid'.
commands = getCommands(CONFIG, feedback = globalFeedback)

from modules.message import Message            # Import the Message class.
chatMsg = Message()

# If plain IRC messages are provided as arguments, enter debug mode, do not connect, but process the messages as if Willowbot was connected.
if '-df' in sys.argv or '--debug-full' in sys.argv:
  doDebugRunFull(chatMsg, commands)

if '-ds' in sys.argv or '--debug-single' in sys.argv:
  doDebugRunSingle(chatMsg, commands)


# Create an instance of the IRC class with the loaded configuration and connect.
irc = IRC(CONFIG)
irc.connect()

# The main loop.
while 1:
  # Read full message from chat. Returns an array with zero or more messages.
  # Get this response before checking the timed commands to ensure the connection is still/already alive.
  response = irc.getResponse()
  # Needs the irc connection as an argument to enable sending reactions to the chat. Full commands are passed for »function« key, which might tamper with the commands set.
  checkTimedCommands(commands, irc)
  
  # Iterate over the received messages.
  for r in response:
    chatMsg.processCommands(commands, r, irc, ignoredUsers)
