poll_results = {}

def poll_start(commands, irc, *args):

  # Poll arguments are passed to the function as a blank space-separated string. Split it into an array.
  poll_options = args[0].split(" ")

  duration = int(poll_options[0])
  del poll_options[0]

  commands['timed']['willowbot_poll'] = {
    'interval' : duration,
    'debug'    : "Poll ended.",
    'function' : 'poll_stop(commands, poll_results, irc)'
  }

  # A string that gathers the vote options for an message that announces the beginning of a poll.
  poll_options_announcementString = ""
  
  i = 0
  for i in range(0, len(poll_options)):
    a = poll_options[i]
    poll_options_announcementString = poll_options_announcementString + "»" + a + "«"
    if i < len(poll_options) - 2:
      poll_options_announcementString = poll_options_announcementString + ", "
    elif i == len(poll_options) - 2:
      poll_options_announcementString = poll_options_announcementString + " oder "
    poll_results[a] = []
    if not a in commands['general']:
      print("Adding a poll option in the commands for " + a)
      commands['general'][a] = {
        'debug'    : '$senderDisplayName added with vote ' + a,
        'function' : 'poll_addUserVote(poll_results, "' + a + '", "$senderDisplayName")'
      }
    else:
      # To do. Finish the else branch and clear the commands from vote options.
      print("Vote option already defined. Poll not started.")
      break

  print("Poll started!")  

  irc.send("/me Die Abstimmung läuft " + str(duration) + " Sekunden. Stimmt ab mit " + poll_options_announcementString + " in den Chat.")


def poll_addUserVote(poll_results, vote, sender):
  print(poll_results)
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


def poll_stop(commands, results, irc):
  votes_total = 0
  votes = {}
  # Delete the timed poll command.
  del commands['timed']['willowbot_poll']
  for c in results:
    votes_total += len(results[c])
    votes[c] = len(results[c])
    # Delete the vote options from the commands dictionary.
    del commands['general'][c]
  results = {}
  votes_sorted = sorted(votes.items(), key=lambda x:x[1], reverse=True)
  print(votes_sorted)
  irc.send(str(votes_total) + " Stimme" + (votes_total > 1 and "n" or "") + " abgegeben.")
  # Prevent division by zero.
  votes_total = max(votes_total, 1)
  for v in votes_sorted:
    irc.send(v[0] + ": " + str(round(v[1]/votes_total*100)) + " %")


