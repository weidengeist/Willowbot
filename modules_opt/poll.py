poll_results = {}

def poll_start(commands, *args):

  # Poll arguments are passed to the function as a blank space-separated string. Split it into an array.
  poll_choices = args[0].split(" ")

  duration = int(poll_choices[0])
  del poll_choices[0]

  commands['timed']['willowbot_poll'] = {
    'interval' : duration,
    'debug'    : "Poll ended.",
    'function' : 'poll_stop(commands, poll_results, irc)'
  }
  
  for a in poll_choices:
    a = str(a)
    poll_results[a] = []
    if not a in commands['general']:
      print("Adding a poll choice in the commands for " + a)
      commands['general'][a] = {
        'debug'    : '$senderDisplayName added with choice ' + a,
        'function' : 'poll_addUserChoice(poll_results, "' + a + '", "$senderDisplayName")'
      }
    else:
      # To do. Finish the else branch and clear the commands from choice options.
      print("Choice option already defined. Poll not started.")
      break

  print("Poll started!")


def poll_addUserChoice(poll_results, choice, sender):
  print(poll_results)
  for i in poll_results:
    if i != choice:
      if sender in poll_results[i]:
        poll_results[i].remove(sender)
        print("Removed choice " + i + " for sender " + sender + " from the list.")
    else:
      if not sender in poll_results[i]:
        poll_results[i].append(sender)
        print("Added choice " + choice + " for user " + sender + ".")
      else:
        print("Sender already in the list with this choice.")


def poll_stop(commands, results, irc):
  votes_total = 0
  votes = {}
  # Delete the timed poll command.
  del commands['timed']['willowbot_poll']
  for c in results:
    votes_total += len(results[c])
    votes[c] = len(results[c])
    # Delete the choice options from the commands dictionary.
    del commands['general'][c]
  results = {}
  votes_sorted = sorted(votes.items(), key=lambda x:x[1], reverse=True)
  print(votes_sorted)
  irc.send(str(votes_total) + " Stimme" + (votes_total > 1 and "n" or "") + " abgegeben.")
  # Prevent division by zero.
  votes_total = max(votes_total, 1)
  for v in votes_sorted:
    irc.send(v[0] + ": " + str(round(v[1]/votes_total*100)) + " %")


