import importlib

from cliOptions import getLanguage


# Is needed outside any function definition so that the other bot modules have access to this variable.
poll_results = {}

def poll_start(commands, irc, *args, contextString = "{pollDuration} seconds: {pollOptions}", resultString = "{votesQuantity}", languageOverride = ""):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + (getLanguage() if languageOverride == "" else languageOverride)).langDict

  # Make the global variable poll_results modifiable.
  global poll_results

  # Poll arguments are passed to the function as a blank space-separated string. Split it into an array.
  poll_options = args[0].split(" ")

  # If the first argument is not convertible to an integer, e.g. it has been forgotten to be specified, default the poll duration to 60 seconds.
  try:
    duration = int(poll_options[0])
    del poll_options[0]
  except:
    duration = 60
  
  commands['timed']['willowbot_poll'] = {
    'interval' : duration,
    'debug'    : "Poll ended.",
    'function' : ['poll_stop(commands, irc, resultString = "' + resultString + '", languageOverride = "' + languageOverride + '")']
  }

  # A string that gathers the vote options for an message that announces the beginning of a poll.
  poll_options_announcementString = ""
  
  for i in range(0, len(poll_options)):
    a = poll_options[i]
    poll_options_announcementString = poll_options_announcementString + "»" + a + "«"
    if i < len(poll_options) - 2:
      poll_options_announcementString = poll_options_announcementString + ", "
    elif i == len(poll_options) - 2:
      poll_options_announcementString = poll_options_announcementString + " " + langDict['or'] + " "
    poll_results[a] = []
    if not a in commands['general']:
      print("Adding a poll option in the commands for " + a)
      commands['general'][a] = {
        'debug'     : '$senderDisplayName added with vote ' + a,
        'function'  : ['poll_addUserVote("' + a + '", "$senderDisplayName")'],
        'matchType' : 'is_caseInsensitive'
      }
    else:
      print("Vote option already defined. Poll not started.")
      del commands['timed']['willowbot_poll']
      for o in poll_options:
        if o in commands['general']:
          if o != poll_options[i]:
            del commands['general'][o]
          del poll_results[o]
      return

  irc.send("/me " + contextString.format(pollDuration = duration, pollOptions = poll_options_announcementString))


def poll_addUserVote(vote, sender):
  # Make the global variable poll_results modifiable.
  global poll_results
  for i in poll_results:
    if i != vote:
      if sender in poll_results[i]:
        poll_results[i].remove(sender)
        print("Removed vote " + i + " for sender " + sender + " from the list.")
    else:
      if not sender in poll_results[i]:
        poll_results[i].append(sender)
        print("Added vote " + vote + " for user " + sender + ".")
      else:
        print("Sender already in the list with this vote.")


def poll_stop(commands, irc, resultString, languageOverride):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + (getLanguage() if languageOverride == "" else languageOverride)).langDict
  # Make the global variable poll_results modifiable.
  global poll_results
  votes_total = 0
  votes = {}
  # Delete the timed poll command.
  del commands['timed']['willowbot_poll']
  for c in poll_results.keys():
    votes_total += len(poll_results[c])
    votes[c] = len(poll_results[c])
    # Delete the vote options from the commands dictionary.
    del commands['general'][c]
  poll_results = {}
  votes_sorted = sorted(votes.items(), key=lambda x:x[1], reverse=True)
  irc.send(resultString.format(votesQuantity = str(votes_total), pluralMod = langDict['pluralMod1'] if votes_total != 1 else ""))
  # Prevent division by zero.
  votes_total = max(votes_total, 1)
  for v in votes_sorted:
    irc.send(v[0] + ": " + str(round(v[1]/votes_total*100)) + " %")
