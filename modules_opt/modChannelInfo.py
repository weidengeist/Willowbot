import re
import requests


# Replace special characters for easy comparison of search term and results.
# Time will tell if this function needs some extension.
def normalizeString(s):
  return re.sub("[,;.:]", "", s.lower()).replace("é", "e").replace("è", "e").replace("ñ", "n").replace("’", "'").replace("\'", "")


def modChannelInfo_title_get(irc, CONFIG, successMsg = "", failMsg = ""):
  response = requests.get(\
    CONFIG['URL_API'] + "channels/",\
    params = {'broadcaster_id' : CONFIG['broadcasterID']},\
    headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID']}\
  )
  if not response.ok:
    print("WARNING! Could not get channel info!", response.json())
    if len(failMsg) > 0:
      irc.send(failMsg)
  else:
    currentTitle = response.json()['data'][0]['title']
    print("Current title:", currentTitle)
    if len(successMsg) > 0:
      irc.send(successMsg.replace("$return", currentTitle))


def modChannelInfo_title_set(irc, CONFIG, title, successMsg = "", failMsg = ""):
  # Either the user has the privileges to change the category or the bot account is the broadcaster.
  if 'channelOauth' in CONFIG or CONFIG['channel'] == CONFIG['botname']:
    bearer = 'channelOauth' in CONFIG and CONFIG['channelOauth'] or CONFIG['oauth']
    response = requests.patch(\
      CONFIG['URL_API'] + "channels/",\
      params = {'broadcaster_id' : CONFIG['broadcasterID']},\
      headers = {"Authorization" : "Bearer " + bearer, "Client-Id" : CONFIG['clientID'], "Content-Type" : "application/json"},\
      json = {"title" : title}\
    )
    if not response.ok or len(title) == 0:
      print("WARNING! Could not set channel title!", response.json())
      if len(failMsg) > 0:
        irc.send(failMsg)
    else:
      print("New title:", title)
      if len(successMsg) > 0:
        irc.send(successMsg.replace("$return", title))
  else:
    print("WARNING! Could not set channel title!", response.json())
    if len(failMsg) > 0:
      irc.send(failMsg)


def modChannelInfo_category_get(irc, CONFIG, successMsg = "", failMsg = ""):
  response = requests.get(\
    CONFIG['URL_API'] + "channels/",\
    params = {'broadcaster_id' : CONFIG['broadcasterID']},\
    headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID']}\
  )
  if not response.ok:
    print("WARNING! Could not get channel info!", response.json())
    if len(failMsg) > 0:
      irc.send(failMsg)
  else:
    gameName = response.json()['data'][0]['game_name']
    print("Game name:", gameName)
    if len(successMsg) > 0:
      irc.send(successMsg.replace("$return", gameName))


def modChannelInfo_category_set(irc, CONFIG, searchTerm = "", listMsg = "$return", successMsg = "", failMsg = ""):
  # Either the user has the privileges to change the category or the bot account is the broadcaster.
  if 'channelOauth' in CONFIG or CONFIG['channel'] == CONFIG['botname']:
    bearer = 'channelOauth' in CONFIG and CONFIG['channelOauth'] or CONFIG['oauth']
    # This branch is used when a category query has already been submitted and the user may choose from a numbered list.
    if 'modChannelInfo_category_candidatesList' in CONFIG:
      try:
        catNumber = int(searchTerm)
        if catNumber > 0 and catNumber <= len(CONFIG['modChannelInfo_category_candidatesList']):
          response = requests.patch(\
            CONFIG['URL_API'] + "channels/",\
            params = {'broadcaster_id' : CONFIG['broadcasterID']},\
            headers = {"Authorization" : "Bearer " + bearer, "Client-Id" : CONFIG['clientID'], "Content-Type" : "application/json"},\
            json = {"game_id" : CONFIG['modChannelInfo_category_candidatesList'][catNumber-1]['id']}\
          )
          if not response.ok:
            print("WARNING! Failed to set the category!", response.json())
            if len(failMsg) > 0:
              irc.send(failMsg)
          else:
            print("New category:", CONFIG['modChannelInfo_category_candidatesList'][catNumber-1]['name'])
            if len(successMsg) > 0:
              irc.send(successMsg.replace("$return", CONFIG['modChannelInfo_category_candidatesList'][catNumber-1]['name']))
            del CONFIG['modChannelInfo_category_candidatesList']
      except:
        del CONFIG['modChannelInfo_category_candidatesList']
        modChannelInfo_category_set(irc, CONFIG, searchTerm, listMsg, successMsg, failMsg)
    else:
      if not searchTerm == "":
        candidates = []
        # Limit the list of results to 5 entries ('first' : 10).
        response = requests.get(\
          CONFIG['URL_API'] + "search/categories/",\
          params = {'query' : searchTerm, 'first' : 10},\
          headers = {"Authorization" : "Bearer " + CONFIG['oauth'], "Client-Id" : CONFIG['clientID']}\
        )
        if not response.ok:
          print("WARNING! No such category was found.", response.json())
          if len(failMsg) > 0:
            irc.send(failMsg)
        else:
          print(response.json())
          searchTerm_normalized = normalizeString(searchTerm)
          print("searchTerm_normalized", searchTerm_normalized)
          results = response.json()['data']
          for r in results:
            r_name_normalized = normalizeString(r['name'])
            print("r_name_normalized", r_name_normalized)
            if searchTerm_normalized == r_name_normalized:
              del candidates
              break
            elif searchTerm_normalized in r_name_normalized:
              candidates.append({'name' : r['name'], 'id' : r['id']})
            else:
              continue
      
          if not 'candidates' in locals() or len(candidates) == 1:
            print("Perfect match found!", r['id'], r['name'])
            response = requests.patch(\
              CONFIG['URL_API'] + "channels/",\
              params = {'broadcaster_id' : CONFIG['broadcasterID']},\
              headers = {"Authorization" : "Bearer " + bearer, "Client-Id" : CONFIG['clientID'], "Content-Type" : "application/json"},\
              json = {"game_id" : r['id']}\
            )
            if not response.ok:
              print("WARNING! Failed to set the category!", response.json())
              if len(failMsg) > 0:
                irc.send(failMsg)
            else:
              print("New category:", r['name'])
              if len(successMsg) > 0:
                irc.send(successMsg.replace("$return", r['name']))
          else:
            candidatesListString = ""
            for i in range(0, len(candidates)):
              candidatesListString += "»" + candidates[i]['name'] + "« (" + str(i+1) + ")"
              if i < len(candidates) - 1:
                candidatesListString += ", "
            irc.send(listMsg.replace("$return", candidatesListString))
            CONFIG['modChannelInfo_category_candidatesList'] = candidates
      else:    
        response = requests.patch(\
          CONFIG['URL_API'] + "channels/",\
          params = {'broadcaster_id' : CONFIG['broadcasterID']},\
          headers = {"Authorization" : "Bearer " + bearer, "Client-Id" : CONFIG['clientID'], "Content-Type" : "application/json"},\
          json = {"game_id" : 0}\
        )
        if not response.ok:
          print("WARNING! Failed to unset the category!", response.json())
        else:
          print("Category has been reset.")
          if len(successMsg) > 0:
            irc.send(successMsg.replace("$return", "{empty}"))
  else:
    print("WARNING! Failed to set the category! No oauth available for this channel.", response.json())
    if len(failMsg) > 0:
      irc.send(failMsg)  
