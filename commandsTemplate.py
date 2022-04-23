commands = {
  "!bsg" : {
    "answer"    : "Please do not tell the streamer how to play.",
    "matchType" : "startsWith",
    "cooldown"  : 30
  },
  "^![Mm]ulti" : {
    "answer"    : "Today we are playing with someone very special.",
    "matchType" : "regex"
  },
  "drink" : {
    "answer"   : "Please stay hydrated!",
    "interval" : 1800
  },
  "!drink" : {
    "answer"   : "Please stay hydrated!",
    "matchType": "startsWith"
  },
  "!issues" : {
    "answer"   : "/announce There are technical difficulties. Please stand by.",
    "minLevel" : 3
  },
  "!give" : {
    "answer"    : "$arg0 gets some $arg1+ to feel cozy.",
    "matchType" : "startsWith"
  },
  "!so" : {
    "answer"    : "For some nice entertainment, pay $arg0’s channel a visit: https://twitch.tv/$arg0.",
    "matchType" : "startsWith"
  },
  "!hug" : {
    "answer"    : "$senderDisplayName gives $arg0 a hug.",
    "matchType" : "startsWith"
  },
  "^Buy.*followers" : {
    "answer"    : "/ban $senderName",
    "matchType" : "regex",
    "level"     : 0
  },
  "^(Wanna|Want to) become famou?s" : {
    "answer"    : "/ban $senderName",
    "matchType" : "regex",
    "level"     : 0
  },
  ".*(Kappa|failFish|LUL)" : {
    "answer"    : "/delete $msgID",
    "matchType" : "regex"
  },
  "myRaid" : {
    "answer"      : "$raidersChannel joins us with $raidersCount viewers. Have fun!",
    "triggerType" : "raid"
  },
  "very long sub" : {
    "answer"      : "$subName has been a subscriber for more than a year now! Congratulations on $subMonth months in our community",
    "minSubLevel" : 13,
    "triggerType" : "sub"
  },
  "any other sub month 10–12" : {
    "answer"      : "$subName has just subscribed for month $subMonth.",
    "minSubLevel" : 10,
    "maxSubLevel" : 12,
    "triggerType" : "sub"
  },
  "Twitch baby" : {
    "answer"      : "We’re having a Twitch baby with $subName!",
    "subLevel"    : 9,
    "triggerType" : "sub"
  },
  "any other sub month 3–8" : {
    "answer"      : "$subName has just subscribed for month $subMonth.",
    "minSubLevel" : 3,
    "maxSubLevel" : 8,
    "triggerType" : "sub"
  },
  "2nd month" : {
    "answer"      : "Thank you so much, $subName, for staying with us.",
    "subLevel"    : 2,
    "triggerType" : "sub"
  },
  "1st month" : {
    "answer"      : "$subName decides on joining our community! Thank you very much.",
    "subLevel"    : 1,
    "triggerType" : "sub"
  },
  "myMultiSubGiftHandler" : {
    "answer"                  : "$subGiftGifter has just gifted $subGiftCount subs to the community with a total of $subGiftCountTotal on this channel.",
    "triggerType"             : "subGiftMulti",
    "suppressFollowupSingles" : True
  },
  "!loot" : {
    "matchType"  : "startsWith",
    "answer"     : "$senderDisplayName loots cookies from $arg0.\n$senderDisplayName loots 40 coins from $arg0.\n$senderDisplayName loots an old sock from $arg0.\n$senderDisplayName loots stinky cheese from $arg0.\n$senderDisplayName loots underpants from $arg0.",
    "answerType" : "random"
  },
  "!gg" : {
    "matchType"  : "startsWith",
    "os-command" : "start C:\the\path\to\my\soundfile.mp3"
  },  
  ".*" : {
    "answer"    : "Welcome to my channel! Take a cookie and have fun.",
    "matchType" : "regex",
    "level"     : 0
  }
}
