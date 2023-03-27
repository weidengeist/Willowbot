import re
import requests

from basics import getConfig

CONFIG = getConfig(feedback = False)

def resolveChatCommands(answerText):
  if re.match("^/announce ", answerText):
    announcement = re.sub("^/announce +", "", answerText)
    response = requests.post(\
      CONFIG['URL_API'] + "chat/announcements",\
      params = {'broadcaster_id' : CONFIG['broadcasterID'], 'moderator_id' : CONFIG['moderatorID']},\
      headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID'], 'Content-Type' : 'application/json'},\
      json = {"message" : announcement, "color" : "primary"}\
    )
    if not response.ok:
      print("WARNING! Could not announce!", response.json())
  
  elif re.match("^/ban ", answerText):
    args = re.findall("[^ ]+", answerText) # 0: /ban; 1: [user-id]; 2: [optional reason]
    banReason = args[2] if len(args) > 2 else ""
    response = requests.post(\
      CONFIG['URL_API'] + "moderation/bans",\
      params = {'broadcaster_id' : CONFIG['broadcasterID'], 'moderator_id' : CONFIG['moderatorID']},\
      headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID'], 'Content-Type' : 'application/json'},\
      json = {"user_id" : args[1], "reason" : banReason}\
    )
    if not response.ok:
      print("WARNING! Could not ban!", response.json())
  
  elif re.match("^/delete ", answerText):
    args = re.findall("[^ ]+", answerText) # 0: /delete; 1: [msgID]
    response = requests.delete(\
      CONFIG['URL_API'] + "moderation/chat",\
      params = {'broadcaster_id' : CONFIG['broadcasterID'], 'moderator_id' : CONFIG['moderatorID'], 'message_id' : args[1]},\
      headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID']}\
    )
    if not response.ok:
      print("WARNING! Could not delete message!", response.json())
  
  elif re.match("^/shoutout ", answerText):
    args = re.findall("[^ ]+", answerText) # 0: /shoutout; 1: [raidersChannelID]
    response = requests.post(\
      CONFIG['URL_API'] + "chat/shoutouts",\
      params = {'from_broadcaster_id' : CONFIG['broadcasterID'], 'to_broadcaster_id' : args[1], 'moderator_id' : CONFIG['moderatorID']},\
      headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID']}\
    )
    if not response.ok:
      print("WARNING! Could not shoutout!", response.json())
  
  elif re.match("^/timeout ", answerText):
    args = re.findall("[^ ]+", answerText) # 0: /timeout; 1: [userID]; 2: [optional duration]
    timeoutDuration = args[2] if len(args) > 2 else 10 # 10 seconds of fallback/default timeout duration.
    response = requests.post(\
      CONFIG['URL_API'] + "moderation/bans",\
      params = {'broadcaster_id' : CONFIG['broadcasterID'], 'moderator_id' : CONFIG['moderatorID']},\
      headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID'], 'Content-Type' : 'application/json'},\
      json = {"user_id" : args[1], "duration" : timeoutDuration}\
    )
    if not response.ok:
      print("WARNING! Could not timeout!", response.json())
  
  else:
    print("Unknown how to resolve this command. Processing normally.")
    return answerText
  
  # This point is only reached in case of a successful chat command evaluation.
  return ""
