from os import path
import importlib
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer

class LocalServer(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    htmlFile = open("./modules/oauthTokenRedirectPage.html", "r")
    htmlCode = htmlFile.read().replace("PYTHON_EXEC", path.split(sys.executable)[-1]).replace("WILLOWBOT_MAIN", sys.argv[0])
    htmlFile.close()

    from cliOptions import getLanguage
    langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + getLanguage()).langDict
    for key in langDict:
      htmlCode = htmlCode.replace(key, langDict[key])
    self.wfile.write(bytes(htmlCode, "utf-8"))

    exit()


  # By using a simple »return« in this function, every output in the terminal is suppressed.
  def log_message(self, format, *args):
    return


def startServer(host, port):        
  webServer = HTTPServer((host, port), LocalServer)
  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass
  webServer.server_close()


scopes = (
  "channel_editor", "channel_commercial",
  "channel:manage:broadcast", "channel:manage:moderators", "channel:manage:vips", "channel:manage:raids",
  "channel:moderate",
  "channel:read:redemptions", "channel:read:subscriptions",
  "chat:edit", "chat:read", 
  "moderator:manage:announcements", "moderator:manage:automod", "moderator:manage:banned_users", "moderator:manage:blocked_terms", "moderator:manage:chat_messages", "moderator:manage:chat_settings", "moderator:manage:shoutouts", 
  "moderator:read:blocked_terms",
  "user:manage:chat_color", "user:manage:whispers",
  "user:read:follows",
  "whispers:edit", "whispers:read"
)

baseURL =  "https://id.twitch.tv/oauth2/authorize?response_type=token&redirect_uri=http://localhost:3000"
