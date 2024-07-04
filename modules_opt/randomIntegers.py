import copy
import importlib
import random
import re

from cliOptions import getLanguage

# contextString may contain the following placeholders:
#   — {resultString}: comma-separated string of the results; may contain »and« or other conjunctions after second-last item in the set locale.
#   — {resultSum}: the sum of the generated random numbers.
#   — {0}, {1}, {2}, …: the first, second, third, etc. result of the number generation; numbers exceeding the quantity of generated numbers are handled and won’t crash Willowbot.
def randomIntegers_generate(irc, interval = [1, 100], quantity = 1, contextString = "{resultString}", sort = False, summarize = False, summaryFormat = "{quantity} × {number}", unique = False, finalConjunction = ", ", languageOverride = ""):
  langDict = importlib.import_module("lang.en").langDict | importlib.import_module("lang." + (getLanguage() if languageOverride == "" else languageOverride)).langDict

  finalConjunction = (" " + langDict[finalConjunction] + " " if finalConjunction != ', ' and finalConjunction in langDict else finalConjunction)

  generatedNumbers = []
  if unique:
    if interval[1] - interval[0] + 1 < quantity:
      print("Can’t generate " + str(quantity) + " unique numbers in an interval of length " + str(interval[1] - interval[0] + 1) + ".")
      return
    generatedNumbers = random.sample(range(interval[0], interval[1] + 1), quantity)
  else:
    generatedNumbers = random.choices(range(interval[0], interval[1] + 1), k = quantity)

  numbersSum = sum(generatedNumbers)

  if sort:
    generatedNumbers.sort()

  # Build the number sequence string.
  sequenceString = ""
  if summarize:
    tempList = copy.deepcopy(generatedNumbers)
    while len(tempList) > 0:
      qnt = tempList.count(tempList[0])
      if len(tempList) < quantity:
        sequenceString += finalConjunction if qnt == len(tempList) else ", "
      sequenceString += summaryFormat.format(quantity = qnt, number = tempList[0])
      tempList = list(filter(lambda x: x != tempList[0], tempList))
  else:
    for i in range(0, len(generatedNumbers)):
      a = generatedNumbers[i]
      sequenceString += str(a)
      if i < len(generatedNumbers) - 2:
        sequenceString += ", "
      elif i == len(generatedNumbers) - 2:
        sequenceString += finalConjunction

  numberedPlaceholders = re.findall("\{([0-9]+)\}", contextString)
  numericList = [int(x) for x in numberedPlaceholders]

  if len(numericList) > 0:
    if max(numericList) + 1 > quantity:
      print("Erroneous context string. Largest placeholder number exceeds quantity of generated numbers.")
      return
    else:
      irc.send(contextString.format(*generatedNumbers, resultString = sequenceString, resultSum = numbersSum))
      return
  else:
    irc.send(contextString.format(resultString = sequenceString, resultSum = numbersSum))
