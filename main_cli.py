import requests
import sys

# For automatically opening the Twitch OAuth token generation page. 
import webbrowser

URL_TOKEN = "https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=e5kdpgd2bbnbj1u5gbjpzeq7vsgwup&redirect_uri=http://localhost:3000&scope=channel:manage:moderators+channel:read:subscriptions+channel:manage:vips+chat:edit+moderator:manage:announcements+user:read:follows+user:manage:whispers+whispers:read+channel:moderate+channel:read:redemptions+channel_editor+channel_commercial+moderator:manage:chat_settings+channel:manage:raids+channel:manage:broadcast+whispers:edit+moderator:manage:automod+moderator:manage:blocked_terms+moderator:manage:chat_messages+moderator:manage:banned_users+user:manage:chat_color+chat:read+moderator:read:blocked_terms+moderator:manage:shoutouts"

# Subdirectories containing routines, class definitions and other important data.
sys.path.append('modules')
sys.path.append('modules_opt')

from modules.basics import checkTimedCommands # Import various general functions from the basics(.py) module in ./modules.
from modules.basics import getCommands        
from modules.basics import getConfig
from modules.irc import IRC                   # Import the IRC class from the irc(.py) module in ./modules.
from modules.message import Message           # Import the Message class.

CONFIG = getConfig(feedback = True)           # Load configuration files. 


# Check if a configuration could be loaded.
if CONFIG['status'] == 0:
  print("✔ Successfully loaded the IRC configuration file!")
else:
  if CONFIG['status'] == 1:
    print("ERROR! The configuration file at " + CONFIG['dir'] + " is incomplete. Please check.")
  elif CONFIG['status'] == 2:
    print("There is no configuration file for this bot yet. An empty configuration file has been created at " + CONFIG['dir'] + ". Please modify it and enter valid data to be able to use the bot.\n")
    input("If you press [Enter] now, your default browser will open https://id.twitch.tv/oauth2/authorize and let you create an access token. Afterwards, return to this window.")
    webbrowser.open(URL_TOKEN)
    print("Now copy the generated token (can be found in the URL bar of your browser; it’s the string after »#access_token=«: …#access_token=[Your access token]&scope=…) into the configuration file as value of the »oauth« key and change the value of the »botname« key to your bot’s account name.\n\nThe program will exit now. Modify your configuration accordingly and restart Willowbow.")
  exit()


# Load the commands for the specified channel.
# Returns a dictionary with the keys 'general', 'timed', 'sub', and 'raid'.
commands = getCommands(CONFIG)


# Options for revoking and getting access tokens.
if len(sys.argv) == 2 and sys.argv[1] == "TOKEN_REVOKE":
  if 'clientID' in CONFIG:
    response = requests.post(\
      "https://id.twitch.tv/oauth2/revoke",\
      headers = {"Content-Type" : "application/x-www-form-urlencoded"},\
      params = {"client_id" : CONFIG['clientID'], 'token': CONFIG['oauth']}\
    )
    if response.ok:
      print("Successfully revoked your access token.")
    else:
      print("An error occurred while trying to revoke your token!", response.json())
  else:
    print("Your current token does not contain a client ID, so you don’t have to revoke it. Simply create a new one.")
  exit()

if len(sys.argv) == 2 and sys.argv[1] == "TOKEN_GET":
  webbrowser.open(URL_TOKEN)
  exit()


if commands['status'] == 0:
  print("✔ Successfully loaded commands for channel " + CONFIG['channel'] + ".")
else:
  print("✖ FAILED! No commands available for channel " + CONFIG['channel'] + ".")

# Create an instance of the IRC class with the loaded configuration, …
irc = IRC(CONFIG)
# … and show feedback information to the user.
if CONFIG['port'] == 6667:
  print("  Will try to connect INSECURELY to " + CONFIG['server'] + " on port " + str(CONFIG['port']) + " after having retrieved more data …")
elif CONFIG['port'] == 6697:
  print("  Will try to connect securely to " + CONFIG['server'] + " on port " + str(CONFIG['port']) + " after having retrieved more data …")


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
