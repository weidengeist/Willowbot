import datetime
import importlib
import re

from cliOptions import getLanguage


# Returns the date difference between two dates, both provided as ISO format date strings.
# If no second date is provided, the difference between now and the first date is returned.
# If only one argument is passed and it contains no year, the current one is assumed. If that date is in the past, the next year is selected.
def dateDiff_fromStrings(a, b = ""):
  if b == "":
    b = datetime.datetime.now()
    if len(a) == 5:
      tempYear = b.year
      if (datetime.datetime.fromisoformat(str(tempYear) + "-" + a) - b).total_seconds() < 0:
        tempYear += 1
      a = str(tempYear) + "-" + a
  else:
    b = datetime.datetime.fromisoformat(b)
  return abs(datetime.datetime.fromisoformat(a) - b)


def dateDiff_contextString(targetDate, nowDate = "", contextString = "{dateDiff}", useAccusativeMod = False, languageOverride = ""):
  # Transform the date component keywords into the used language.
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + (getLanguage() if languageOverride == "" else languageOverride)).langDict
  accusativeMod = langDict['accusativeMod'] if useAccusativeMod else ""
  day = langDict['day'].format(accusativeMod = accusativeMod)
  days = langDict['days'].format(accusativeMod = accusativeMod)
  hour = langDict['hour'].format(accusativeMod = accusativeMod)
  hours = langDict['hours'].format(accusativeMod = accusativeMod)
  minute = langDict['minute'].format(accusativeMod = accusativeMod)
  minutes = langDict['minutes'].format(accusativeMod = accusativeMod)
  second = langDict['second'].format(accusativeMod = accusativeMod)
  seconds = langDict['seconds'].format(accusativeMod = accusativeMod)
  and_ = langDict['and']
  
  diff = dateDiff_fromStrings(targetDate, nowDate)
  diffComponents = re.findall("^([0-9]+|).*?([0-9]+):([0-9]+):([0-9]+)", str(diff))[0]
  dateDiffString = ""
  if int(diffComponents[3]) > 0:
    dateDiffString = str(int(diffComponents[3])) + " " + (seconds if int(diffComponents[3]) > 1 else second)
  if int(diffComponents[2]) > 0:
    if len(dateDiffString) == 0:
      dateDiffString = str(int(diffComponents[2])) + " " + (minutes if int(diffComponents[2]) > 1 else minute)
    else:
      dateDiffString = str(int(diffComponents[2])) + " " + (minutes if int(diffComponents[2]) > 1 else minute) + " " + and_ + " " + dateDiffString
  if int(diffComponents[1]) > 0:
    if len(dateDiffString) == 0:
      dateDiffString = str(int(diffComponents[1])) + " " + (hours if int(diffComponents[1]) > 1 else hour)
    else:
      dateDiffString = str(int(diffComponents[1])) + " " + (hours if int(diffComponents[1]) > 1 else hour) + ("," if and_ in dateDiffString else " " + and_) + " " + dateDiffString
  # Checking the presence of days is needed because date differences smaller than a full day don’t contain »0 day(s)«.
  if diffComponents[0] != "" and int(diffComponents[0]) > 0:
    if len(dateDiffString) == 0:
      dateDiffString = str(int(diffComponents[0])) + " " + (days if int(diffComponents[0]) > 1 else day)
    else:
      dateDiffString = str(int(diffComponents[0])) + " " + (days if int(diffComponents[0]) > 1 else day) + ("," if and_ in dateDiffString else " " + and_) + " " + dateDiffString

  return contextString.format(dateDiff = dateDiffString)


def dateDiff_send(irc, targetDate, nowDate = "", contextString = "{dateDiff}", useAccusativeMod = False, languageOverride = ""):
  s = dateDiff_contextString(targetDate, nowDate, contextString, useAccusativeMod, languageOverride)
  irc.send(s)
