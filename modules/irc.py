import datetime
import importlib
import socket
import ssl
import select
import time

from modules.basics import getLogins
from modules.cliOptions import getLanguage

class IRC:
  
  def __init__(self, config):  
    self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.config = config
    self.retries_curr = 0
    self.retries_timeout = 1
    self.retries_max = self.config['connectionRetries']
    self.isConnected = False

  def send(self, msg):
    self.irc.send(bytes("PRIVMSG #" + self.config['channel'] + " :" + msg + "\n", "UTF-8"))

  def sendPlain(self, text):
    self.irc.send(bytes(text + "\n", "UTF-8"))

  def connect(self):
    logins = getLogins()

    langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + self.config['language']).langDict

    botname = 'botname' in self.config and self.config['botname'] or ""
    oauth = botname in logins and logins[botname] or ""
    port = 'port' in self.config and self.config['port'] or ""
    server = 'server' in self.config and self.config['server'] or ""   

    if port == 6667:      
      self.irc.connect((server, port)) # Connects to the server.
    elif port == 6697:
      # Wrap the socket.
      self.irc = ssl.wrap_socket(self.irc, ssl_version=ssl.PROTOCOL_TLS)      
      self.irc.connect((server, port)) # Connects to the server.
    self.sendPlain("PASS oauth:" + oauth) # User authentication.
    print(" " + langDict['symbol_success'] + " " + langDict['irc_passSent'])
    self.sendPlain("NICK " + botname)
    print(" "  + langDict['symbol_success'] + " " + langDict['irc_botnameSent'].format(botname = botname))
    self.sendPlain("JOIN #" + self.config['channel']) # Join the channel.
    print(" " + langDict['symbol_success'] + " " + langDict['irc_channelEntered'].format(channel = self.config['channel']))
    self.sendPlain("CAP REQ :twitch.tv/tags")
    self.sendPlain("CAP REQ :twitch.tv/commands")

  def getResponse(self):
    langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + self.config['language']).langDict
    # To do: Reconnection still not working. 
    text = ""
    ready = select.select([self.irc], [], [], 1)
    if ready[0]:
      # Check if there is a remote address ('raddr') in the response. If so, the connection is alive.
      if ", raddr=(" in str(ready[0]):
        try:
          text = self.irc.recv(4096).decode("utf-8") # Receive the text.
        except ConnectionError:
          print(langDict['irc_connectionError'])
          text = 'EXCEPTION'
      else:
        text = 'EXCEPTION'

      if "PING :tmi.twitch.tv" in str(text):
        self.sendPlain("PONG :tmi.twitch.tv")
  
      if text == 'EXCEPTION' and self.retries_curr <= self.retries_max:
        self.isConnected = False
        print(langDict['irc_connectionError_reconnection'])
        for i in range(self.retries_timeout, 0, -1):
          # Three additional spaces at the end of the message to prevent trailing message residues.
          print(langDict['irc_reconnectionTrial'].format(currentTrial = str(self.retries_curr + 1), maxTrials = str(self.retries_max), seconds = str(i)), end='\r')
          time.sleep(1)
        print("\n")
        # Renew the connection.
        self.irc.close()
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
        self.retries_curr = self.retries_curr + 1
        # Apply the official Twitch advice to increase timeout between reconnection trials exponentially.
        self.retries_timeout = self.retries_timeout * 2
        self.getResponse()

  
    # Split the response for cases where more than one user message is in one response.
    text = text.replace("\r\n", "\n").split('\n')
    # Split command above creates an empty last entry in response list. Delete this.
    del text[-1]

    if not self.isConnected and len(text) > 0:
      print(" " + langDict['symbol_success'] + " " + langDict['irc_connectionEstablished'])
      self.isConnected = True
      # Reset the trials and the timeout.
      self.retries_curr = 0
      self.retries_timeout = 1
    
    return text
