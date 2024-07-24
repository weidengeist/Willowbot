import datetime
import importlib
import platform  # Import module »platform« to be able to get the user’s operating system.
import socket
import ssl
import select
import time

# Nur fürs Debugging. Später entfernen.
import os

from modules.basics import getLogins
from modules.cliOptions import getLanguage

class IRC:

  def __init__(self, config):  
    self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.irc.settimeout(10)
    self.config = config
    self.retries_curr = 0
    self.retries_timeout = 1
    self.isConnected = False
    self.latestDisconnectCheckTime = time.time()
    self.langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + self.config['language']).langDict

    print(" ✔ Loaded configuration:\n      ", self.config)


  def send(self, msg):
    self.irc.send(bytes("PRIVMSG #" + self.config['channel'] + " :" + msg + "\n", "UTF-8"))


  def sendPlain(self, text):
    self.irc.send(bytes(text + "\n", "UTF-8"))


  def connect(self):
    logins = getLogins()

    botname = self.config['botname'] if 'botname' in self.config else ""
    oauth = logins[botname] if botname in logins else ""
    port = self.config['port'] if 'port' in self.config else ""
    server = self.config['server'] if 'server' in self.config else ""   

    if port == 6667:      
      self.irc.connect((server, port)) # Connects to the server.
    elif port == 6697:
      # Wrap the socket.
      # Python versions prior 3.11.
      if hasattr(ssl, "wrap_socket"):
        self.irc = ssl.wrap_socket(self.irc, ssl_version=ssl.PROTOCOL_TLS)
      # Python versions 3.11 and above.
      else:
        self.irc = ssl.SSLContext().wrap_socket(self.irc)
      try:
        self.irc.connect((server, port)) # Connects to the server.
      except:
        print(self.langDict['irc_connectionError_deadConnection'])
        exit()

    self.sendPlain("PASS oauth:" + oauth) # User authentication.
    print(" " + self.langDict['symbol_success'] + " " + self.langDict['irc_passSent'])
    self.sendPlain("NICK " + botname)
    print(" "  + self.langDict['symbol_success'] + " " + self.langDict['irc_botnameSent'].format(botname = botname))
    self.sendPlain("JOIN #" + self.config['channel']) # Join the channel.
    print(" " + self.langDict['symbol_success'] + " " + self.langDict['irc_channelEntered'].format(channel = self.config['channel']))
    self.sendPlain("CAP REQ :twitch.tv/tags")
    self.sendPlain("CAP REQ :twitch.tv/commands")


  def tryReconnect(self):
    if platform.system() == "Linux":
      os.system('notify-send "RECONNECT" "IRC reconnect for Willowbot"')

    self.isConnected = False
    print(self.langDict['irc_connectionError_reconnection'])
    for i in range(self.retries_timeout, 0, -1):
      # Three additional spaces at the end of the message to prevent trailing message residues.
      print(self.langDict['irc_reconnectionTrial'].format(currentTrial = str(self.retries_curr + 1), maxTrials = str(self.config['connectionRetries']), seconds = str(i)), end='\r')
      time.sleep(1)
    print("\n")
    # Renew the connection.
    self.irc.close()
    self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connect()
    self.retries_curr += 1
    # Apply the official Twitch advice to increase timeout between reconnection trials exponentially.
    self.retries_timeout *= 2
    self.getResponse()


  def getResponse(self):
    # To do: Reconnection still not working. 
    text = ""
    # Set up the IRC module for receiving for new messages. Timeout is 1 second.
    ready = select.select([self.irc], [], [], 1)
    if ready[0]:
      # Set the latest disconnect check time to the current time, because there is no need to ping the Twitch server as long as messages are received.
      self.latestDisconnectCheckTime = time.time()
      # Check if there is a remote address ('raddr') in the response. If so, the connection is alive.
      if ", raddr=(" in str(ready[0]):
        try:
          text = self.irc.recv(4096).decode("utf-8") # Receive the text.
        except ConnectionError:
          print(self.langDict['irc_connectionError'])
          text = 'EXCEPTION'
      else:
        text = 'EXCEPTION'

      # Twitch sent a ping to check if you are still there.
      if "PING :tmi.twitch.tv" in str(text):
        self.sendPlain("PONG :tmi.twitch.tv")

      # You have sent a ping to Twitch to check if your connection is still alive and Twitch has (hopefully) answered with a pong.
      #if "PONG tmi.twitch.tv :tmi.twitch.tv" in str(text):
      #  self.latestDisconnectCheckTime = time.time()

      if (text == 'EXCEPTION' or text == "") and self.retries_curr <= self.config['connectionRetries']:
        self.tryReconnect()

    else:
      # If there is no message waiting to be processed and the disconnectCheckInterval has elapsed since the latest check, send Twitch a ping to check if the connection is still alive.
      elapsedSinceLatestCheck = time.time() - self.latestDisconnectCheckTime
      if elapsedSinceLatestCheck >= self.config['disconnectCheckInterval']:
        self.sendPlain('PING :tmi.twitch.tv')
      if elapsedSinceLatestCheck >= 2 * self.config['disconnectCheckInterval']:
        print("WARNING! Connection seems dead. Trying to reconnect.")
        self.tryReconnect()

    # Split the response for cases where more than one user message is in one response.
    text = text.replace("\r\n", "\n").split('\n')
    # Split command above creates an empty last entry in response list. Delete this.
    del text[-1]

    if not self.isConnected and len(text) > 0:
      print(" " + self.langDict['symbol_success'] + " " + self.langDict['irc_connectionEstablished'])
      print("\n", "—" * 25, "\n")
      self.isConnected = True
      # Reset the trials and the timeout.
      self.retries_curr = 0
      self.retries_timeout = 1

    return text
