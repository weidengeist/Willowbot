import sys

# Subdirectories containing routines, class definitions and other important data.
sys.path.append('modules')

from basics import checkTimedCommands # Import various general functions from the basics(.py) module in ./modules.
from basics import getCommands        
from basics import getConfig
from irc import IRC                   # Import the IRC class from the irc(.py) module in ./modules.
from message import Message           # Import the Message class.

CONFIG = getConfig()        # Load configuration files. 

# Check if a configuration could be loaded.
if CONFIG['status'] == 0:
  print("Successfully loaded the IRC configuration file!")
else:
  if CONFIG['status'] == 1:
    print("The configuration file at " + CONFIG['dir'] + " is incomplete. Please check.")
  elif CONFIG['status'] == 2:
    print("There is no configuration file for this bot yet. An empty configuration file has been created at " + CONFIG['dir'] + ". Please modify it and enter valid data to be able to use the bot.\n\nFor a valid access token, go to https://twitchapps.com/tmi/ and login to your bot’s account. Copy the generated token into the configuration file as value of the »oauth« key and change the value of the »botname« key to your bot’s account name.")
  exit()
  
# Load the commands for the specified channel.
# Returns a dictionary with the keys 'general', 'timed', 'sub', and 'raid'.
commands = getCommands(CONFIG)

if commands['status'] == 0:
  print("Successfully loaded commands for channel " + CONFIG['channel'] + ".")
else:
  print("No commands available for channel " + CONFIG['channel'] + ". Only raid and subscription defaults are available.")

# Create an instance of the IRC class with the loaded configuration, …
irc = IRC(CONFIG)
# … show feedback information to the user, …
if CONFIG['port'] == 6667:
  print("Connecting INSECURELY to " + CONFIG['server'] + " …")
elif CONFIG['port'] == 6697:
  print("Connecting securely to " + CONFIG['server'] + " on port " + str(CONFIG['port']) + " …")

# … and connect.
irc.connect()

chatMsg = Message()
chatMsg.channel = CONFIG['channel']

# The main loop.
while 1:
  # Read full message from chat. Returns an array with zero or more messages.
  # Get this response before checking the timed commands to ensure the connection is still/already alive.
  response = irc.getResponse()
  
  # Needs the irc connection as an argument to enable sending reactions to the chat.
  checkTimedCommands(commands['timed'], irc)
  
  # Iterate over the received messages.
  for r in response:
    chatMsg.processCommands(commands, r, irc)
