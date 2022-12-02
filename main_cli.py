import sys

# Subdirectories containing routines, class definitions and other important data.
sys.path.append('modules')
sys.path.append('modules_opt')

from modules.basics import checkTimedCommands # Import various general functions from the basics(.py) module in ./modules.
from modules.basics import getCommands        
from modules.basics import getConfig
from modules.irc import IRC                   # Import the IRC class from the irc(.py) module in ./modules.
from modules.message import Message           # Import the Message class.


CONFIG = getConfig()                  # Load configuration files. 

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
  print("No commands available for channel " + CONFIG['channel'] + ".")

# Create an instance of the IRC class with the loaded configuration, …
irc = IRC(CONFIG)
# … and show feedback information to the user.
if CONFIG['port'] == 6667:
  print("Connecting INSECURELY to " + CONFIG['server'] + " …")
elif CONFIG['port'] == 6697:
  print("Connecting securely to " + CONFIG['server'] + " on port " + str(CONFIG['port']) + " …")


chatMsg = Message()
chatMsg.channel = CONFIG['channel']

# If plain IRC messages are provided as arguments, enter debug mode, do not connect, but process the messages as if Willowbot was connected.
if len(sys.argv) == 3:
  if sys.argv[2] == "DEBUG":
    from debug import debugList
    for key in debugList:
      print("\nTesting IRC message of type " + key + ".")
      chatMsg.processCommands(commands, debugList[key], False)
  else:
    PRIVMSG = '@badge-info=;badges=;client-nonce=1a2b3c4d5e6f7g8h9i;color=#008000;display-name=WillowbotDebugTester;emotes=555555560:83-84/555555584:114-115/1:31-32;first-msg=0;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=0;returning-chatter=0;room-id=123456789;subscriber=0;tmi-sent-ts=1658754900000;turbo=0;user-id=987654321;user-type= :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :' + sys.argv[2]
    chatMsg.processCommands(commands, PRIVMSG, False)

else:
  # Connect to Twitch IRC.
  irc.connect()

  # The main loop.
  while 1:
    # Read full message from chat. Returns an array with zero or more messages.
    # Get this response before checking the timed commands to ensure the connection is still/already alive.
    response = irc.getResponse()
    
    # Needs the irc connection as an argument to enable sending reactions to the chat. Full commands are passed for »function« key, which might tamper with the commands set.
    checkTimedCommands(commands, commands['timed'], irc)
    
    # Iterate over the received messages.
    for r in response:
      chatMsg.processCommands(commands, r, irc)
