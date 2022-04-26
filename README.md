# Willowbot

This is a chat bot intended to be used on Twitch. It allows you to configure custom commands, optionally based on regular expressions, which the bot will react to – either with an answer in the chat or by executing an OS command. It also supports timed commands and has an integrated level system to limit the usage of commands to different user groups.


The instructions and descriptions below are written especially for non-programming users to make Willowbot more accessible. Feedback for further improvements in this regard is always welcome.


## 1 Installation

You need to have installed Python 3 to use Willowbot. Download the package and just unzip it to a location to your liking.


## 2 Initial setup

Open a console (on Windows: start `cmd`, on Linux/Mac: press Ctrl+Alt+T (on most desktop environments) or search for `terminal` in your application menu). Navigate to the directory where Willowbot is located by typing `cd`, followed by a blank space and the Willowbot location, e.g. `cd C:\Programs\Willowbot` on Windows or `cd /home/thatsme/Willowbot` on Linux/Mac. Now start the bot by typing `python main_cli.py`. If everything is installed correctly, you should now be presented Willowbot’s message that there is no configuration file for its connection. It will create a template configuration file in an appropriate directory, which Willowbot will tell you in this message.

**Beware!** The procedure has only been tested on Linux. If any information about the steps needed on Windows is incorrect and/or does not work, please let me know.

Now edit the configuration file template. Only two values have to be changed: `botname` and `oauth`. `botname` equals your bot’s account name (which means that using the bot requires a dedicated Twitch account for it, but you may also use it with your broadcaster account); `oauth` is [an access token for Twitch](https://twitchapps.com/tmi/) you must have generated.

After having edited the configuration file accordingly, start the bot again the way described above and it should now successfully connect to your bot’s own Twitch channel. In practice, you will want Willowbot to run on your broadcaster channel or – if you are a moderator – on some other channel where you have moderator privileges. In this case, you just pass that channel as the first argument when running Willowbot, meaning that you extend the line
```
python main_cli.py
```
to
```
python main_cli.py myownchannel
```
Of course, you have to replace `myownchannel` with the appropriate channel name where you want Willowbot to do its duty and run a specific set of commands.


## 3 Creating command sets

Besides a directory for the general Willowbot/IRC configuration, this program will create a subdirectory named `commands` in this configuration directory. This is where you have to put the command sets you want your bot to use. You can create command sets for multiple channels; each set is a separate file named by the channel where you want it to be used. (This might come in handy if you are a moderator of more than one channel.) From now on, let’s assume your bot is named IAmABot, i.e. uses the Twitch account »IAmABot«. For testing purposes, it is highly recommended to use your bot’s own channel, so let’s create a command set for that now.

The commandsets themselves are small Python scripts, doing nothing but assigning a [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) to a `commands` variable. Create a file called `iamabot.py` (as this is the channel where we want to do some tests; please note: Use small letters only!) where you can put your command checks and bot reactions.

There is a `commandsTemplate.py` file included in this repository which contains most of the example commands mentioned in this Readme file in the sections below. However, further reading instead of just copying and pasting from the template file is *strongly recommended* as you will certainly run into difficulties when doing so.


### 3.1 User-triggered commands

As a start, put the skeleton for your commands into this file:
```
commands = {
  
}
```
Maybe you’d like to have a `!bsg` command to tell your viewers about your backseat gaming policy, so we tell our bot the triggering chat command and what it is supposed to answer:
```
commands = {
  "!bsg" : {
    "answer" : "Please do not tell the streamer how to play."
  }
}
```
The answer works just like an ordinary [Twitch chat command](https://help.twitch.tv/s/article/chat-commands), i.e. you can add `/me` or `/announce` to the answer to emphasize it.


#### 3.1.1 Simple matching

Sometimes you might want to ping a specific chat member when using your `!bsg` command, but the way it is shown above, the bot would do nothing, because it checks if the whole message is »!bsg«, not if it contains »!bsg«. This is the default behaviour. To check a specific part of the message, you have to define a `matchType`. In this case, the `startsWith` is the appropriate one.
```
commands = {
  "!bsg" : {
    "answer"    : "Please do not tell the streamer how to play.",
    "matchType" : "startsWith"
  }
}
```
Now you can trigger the bot’s answer with e.g. `!bsg @randomtwitchuser`. Note the comma at the end of the line with `answer`! The order of the key definition does not matter; `matchType` can be defined before `answer` as well.

The other `matchType` options available in Willowbot are `contains`, `endsWith`, `regex`, and `contains_caseInsensitive`. The last one is mainly for convenience reasons, however, it is recommended to use regular expressions (option `regex`) instead.


#### 3.1.2 Advanced matching: regular expressions

Most use cases should be covered by the simple matching keywords. If you feel in need of more control about the messages that are supposed to make Willowbot react in a certain way, regular expressions can be evaluated.

For example, you would like to have a `!multi` command to tell your viewers whom you are currently playing with. If you want this message to also be displayed when sending `!Multi`, you could of course simply input the same command block again and replace `m` with `M`. A more elegant way is using a regular expression instead:
```
commands = {
  "^![Mm]ulti" : {
    "answer"    : "Today we are playing with someone very special.",
    "matchType" : "regex"
  }
}
```
The symbol `^` means that the message starts with the pattern following it, so `^` in the `matchType` `regex` can replace `startsWith`. The so-called character set `[Mm]` means just what we want to achieve: Either of these two letters may introduce the command.


### 3.2 Timed commands

Of course, Willowbot also supports timed commands, i.e. sending a message automatically after a distinctive period of time has elapsed. In this case, there is no need to define an actual chat message that is supposed to trigger the command and you may name it whatever you like. Internally, Willowbot differentiates between timed and user-triggered commands, so it is not possible to use one command for both purposes, i.e. to execute a timed command manually.

To define a timed command, Willowbot needs the `interval` keyword:
```
commands = {
  "drink" : {
    "answer"   : "Please stay hydrated!",
    "interval" : 1800
  }
}
```
This will create a message to remind the streamer and viewers of grabbing a drink every 30 minutes (1800 seconds). If you want to enable your viewers to trigger this message, add a command like described in the previous section to your commands set, which in its completeness would eventually look like this:
```
commands = {
  "drink" : {
    "answer"   : "Please stay hydrated!",
    "interval" : 1800
  },
  "!drink" : {
    "answer"   : "Please stay hydrated!",
    "matchType": "startsWith"
  }
}
```


### 3.3 Cooldowns

Implementing commands with cooldowns is just as simple as doing so for timed commands. You only have to replace `interval` with `cooldown`:
```
commands = {
  "!bsg" : {
    "answer"   : "Please do not tell the streamer how to play.",
    "cooldown" : 30
  }
}
```
The code above will enable the command `!bsg` for your users and prevent the bot from reacting to it again before 30 seconds have elapsed.


### 3.4 Level system

To limit the access to your commands, Willowbot provides a level system. Every user in the chat is assigned a level based on his/her role and chat experience. The following levels are implemented:

* 0: the user posts the very first time ever on this channel;
* 1: ordinary user who has been on this channel before but is no subscriber;
* 2: subscribers;
* 3: moderators;
* 4: broadcasters.

To make Willowbot check the user’s level before sending an answer, you have to use the keyword `level` or `minLevel`. A few examples shall explain this further.

The most common scenario for the levels is to determine a minimal level that is required to issue a command. For a command that can only be used by the channel moderators and the broadcaster, you would have to use the `minLevel` option and set it to 3:
```
commands = {
  "!issues" : {
    "answer"   : "/announce There are technical difficulties. Please stand by.",
    "minLevel" : 3
  }
}
```

If you want to give users new to your chat a special greeting, you want to ensure that not all users get this message, so you restrict Willowbot’s reaction to level-0 users:
```
commands = {
  ".*" : {
    "answer"    : "Welcome to my channel! Take a cookie and have fun.",
    "matchType" : "regex",
    "level"     : 0
  }
}
```
Besides a level definition, this command uses the regular expression `.*` to match *any* character (`.`) occuring 0 or more (`*`) times posted by a new user. We will have a closer look at such asterisk patterns and how to use them efficiently in the following section.


### 3.5 Placeholder variables

Some messages might demand personalization. For such cases, Willowbot provides various variables that are resolved before the actual message is sent.

To illustrate the usage of placeholder variables, let’s define a shoutout command:
```
commands = {
  "!so" : {
    "answer"    : "For some nice entertainment, pay $arg0’s channel a visit: https://twitch.tv/$arg0.",
    "matchType" : "startsWith"
  }
}
```
The command definition above uses (indicated by `$`) the placeholder variable `arg0`, which means that Willowbot will replace `$arg0` within in the answer with the first word after the `!so` command. So `!so GreatStreamer` would resolve to: `For some nice entertainment, pay GreatStreamer’s channel a visit: https://twitch.tv/GreatStreamer.`

You may use as many arguments as you like in your answer just by enumerating them in your answer. Note that counting begins at 0, in words: zero, not at 1. Here is another example:
```
commands = {
  "!give" : {
    "answer"    : "$arg0 gets some $arg1 to feel cozy.",
    "matchType" : "startsWith"
  }
}
```
The answer above uses two arguments (`arg0` and `arg1`). This means that the first two words after `!give` will be put into the answer before it is sent to the chat. `!give McFluffy cookies` would result in the chat message: `McFluffy gets some cookies to feel cozy.`

You may also gather arguments passed to a command by appending `+` to a numbered `arg` variable. We use the example above and modify it in a tiny way, namely by just replacing `$arg1` with `$arg1+`:
```
commands = {
  "!give" : {
    "answer"    : "$arg0 gets some $arg1+ to feel cozy.",
    "matchType" : "startsWith"
  }
}
```
»Why would we want to do this?«, you might ask. `$arg1+` does not only catch the second word after `!give` like `$arg1` would do, but it gathers all words from the second one onwards. So in contrast to the version shown before, our new `!give` command will now catch more than just two arguments. In our first `!give` version, we could only give McFluffy »some blanket to feel cozy«. With the new command we can `!give McFluffy a very warm blanket` to feel cozy. Just a blanket is still possible, though.

Do you want to spread some love in your chat? Enable your viewers to virtually hug each other by defining a command for that action:
```
commands = {
  "!hug" : {
    "answer"    : "$senderDisplayName gives $arg0 a hug.",
    "matchType" : "startsWith"
  }
}
```
This command introduces another placeholder variable: `senderDisplayName`. On Twitch, every user has a login name and a display name. Those are almost identical; the only difference is that the login name uses only small letters whereas the display name may also contain capital letters. By putting `$senderDisplayName` into our answer we can use the name of the user who issued the command. So if user McFluffy sends the command `!hug Kittycat`, our command definition above would result in the message: `McFluffy gives Kittycat a hug.` (Side note: If you use `$senderName` instead of `$senderDisplayName`, the message would read: `mcfluffy gives Kittycat a hug.`)

Another very useful purpose for placeholders is timeouting or banning scam bots entering the chat. If such a scam bot is known to use the message »Buy followers, subs, and viewers: [URL]«, you can easily ban the bot account from your channel as soon as this message shows up in your chat:
```
commands = {
  "Buy followers" : {
    "answer"    : "/ban $senderName",
    "matchType" : "startsWith",
    "level"     : 0
  }
}
```
The most important aspect of this command is `"level" : 0`! You surely don’t want to ban legitimate users in your chat who use »Buy followers« in another context.

Of course, the command above can be improved by using regular expressions:
```
commands = {
  "^Buy.*followers" : {
    "answer"    : "/ban $senderName",
    "matchType" : "regex",
    "level"     : 0
  }
}
```
A short explanation for the regex used here: A user will be banned if his/her first message ever in the chat starts (`^`) with »Buy«, followed by arbitrary characters (`.`) in a quantity of 0 or more (`*`) and afterwards the word »followers«. By putting `.*` before `followers`, you can catch a scam bot message even if it changes the order of words (»Buy followers, subs, and viewers«, »Buy subs, followers, and viewers«, etc.).

Another fancy example for banning scam bots:
```
commands = {
  "^(Wanna|Want to) become famou?s" : {
    "answer"    : "/ban $senderName",
    "matchType" : "regex",
    "level"     : 0
  }
}
```
No matter if the user trying to scam you starts (`^`) his/her message with »Want to« or »Wanna« or if he/she writes »famous« with or without »u«: He/She will be banned immediately from your channel with the command definition above.

Willowbot’s capabilities also allow you to define your own list of forbidden terms and to immediately delete messages using them:
```
commands = {
  ".*(Kappa|failFish|LUL)" : {
    "answer"    : "/delete $msgID",
    "matchType" : "regex"
  }
}
```
The command definition above will delete all Messages which contain the terms/emotes »Kappa«, »failFish«, or »LUL«. For this action we need the ID of the message you want to delete. That ID is hidden behind the placeholder variable `msgID`. The advantage of using this method instead of the Twitch blacklist: You and your moderators will be able to see the message and its problematic content and, if necessary, take further actions in case of severe discrimination or harassement, whereas messages with Twitch blacklist terms would be suppressed before any moderator can see it and have a chance to report the user to Twitch. In the section about answer types we will see how to extend this command and make it even more useful.


### 3.6 Trigger types: raids and subscriptions

The chat messages sent on Twitch all contain special meta data and can so – among others – be differentiated between user messages, subscriptions, and raids. In contrast to the user messages, which you define by providing a word or pattern that has to be matched by a message, subscription and raid messages can have an arbitrary name. You tell Willowbot under which circumstances the reaction is supposed to be triggered by providing a `triggerType` key.

Willowbot’s default behaviour is processing messages that appear in the chat, i.e. user messages. Invisible to the common user, special messages are sent in the background. Those messages contain information about raids and subscriptions, among others. If you want Willowbot to handle those, you have to include a `triggerType` key in your command definition.

Side note: Willowbot has its own handlers for the currently implemented special message types and will present you information about is on the console via a debug message. Those fallback handlers will not be triggered if you have defined your own ones.


#### 3.6.1 Raids

Let’s start off simple by defining a command that handles raids:
```
commands = {
  "myRaid" : {
    "answer"      : "$raidersChannel joins us with $raidersCount viewers. Have fun!",
    "triggerType" : "raid"
  }
}
```
It is important to set `triggerType` `raid` in this definition. Otherwise, Willowbot would print the answer string to the chat as soon as someone’s complete message reads »raids«.

As it has been mentioned above, it is not necessary to provide a special pattern for this kind of message handlers. However, you *have* to provide a unique identifier for the handler. Non-unique identifiers will overwrite other already defined commands with the same identifier/pattern.

You can see two more placeholder variables in the answer: `raidersChannel` and `raidersCount`. As soon as an incoming raid is detected, the placeholders will be replaced with the channel that sends you its viewers and the number of viewers, respectively.

Commands with the `raid` type also support a `minRaidersCount` key. If this key is set, the according reaction will only be triggered if the raid consists of at least the specified quantity of people.


#### 3.6.2 Subscriptions

Subscription handling is a little more complex than raid handling, as there are various types of subscriptions for each of which you may provide a special treatment.

Let’s define a simple handler for renewed subscriptions:
```
commands = {
  "myResub" : {
    "answer"      : "$subName has already supported this channel for $subMonth months.",
    "triggerType" : "sub"
  }
}
```
The trigger types `sub`, `subPrime`, and `subGiftContinued` support the keys `subLevel`, `minSubLevel`, and `maxSubLevel`. Those allow you to differentiate even more between subscriptions by sending special messages only for a distinctive (minimal) amount of subscribed months.
```
commands = {
  "very long sub" : {
    "answer"      : "$subName has been a subscriber for more than a year now! Congratulations on $subMonth months in our community",
    "minSubLevel" : 13,
    "triggerType" : "sub"
  },
  "any other sub month 9–12" : {
    "answer"      : "$subName has just subscribed for month $subMonth.",
    "triggerType" : "sub",
    "minSubLevel" : 9,
    "maxSubLevel" : 12
  },
  "Twitch baby" : {
    "answer"      : "We’re having a Twitch baby with $subName!",
    "subLevel"    : 9,
    "triggerType" : "sub"
  },
  "any other sub month 3–8" : {
    "answer"      : "$subName has just subscribed for month $subMonth.",
    "triggerType" : "sub",
    "minSubLevel" : 3,
    "maxSubLevel" : 8
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
  }
}
```
Here you can see the various ways of using `subLevel`, `minSubLevel`, and `maxSubLevel`. Willowbot will process the `sub` category commands (`sub`, `subPrime`, `subGiftContinued`, `subGiftSingle`, `subGiftMulti`) and execute *every* match, so it is important to set their restrictions carefully, i.e. disjunctive to prevent that more than one reaction will be executed. In the definitions above you can see that the subscription levels exclude each other. Although they are ordered, it is not necessary to do so to make Willowbot execute the reactions correctly. It won’t increase performance either.

Whenever a multi-subscription gift occurs on the channel, there are always followup messages about single-subscription gifts with the same gifter in the respective quantity. As you might not want Willowbot to react to those messages with its defined single-subscription gift answers, the trigger type `subGiftMulti` has a special key: `suppressFollowupSingles`. It is a boolean, so the values `True` and `False` are allowed for this key. If you set this to `True`, Willowbot will do as described above and not react to the next single-subscription gift messages from this user until the amount of gifted subscriptions in the multi-subscription gift is reached. A little code sample just to clarify and leave no questions unanswered:
```
commands = {
  "myMultiSubGiftHandler" : {
    "answer"                  : "$subGiftGifter has just gifted $subGiftCount subs to the community with a total of $subGiftCountTotal on this channel.",
    "triggerType"             : "subGiftMulti",
    "suppressFollowupSingles" : True
  }
}
```

##### Supported placeholders per subscription context

* `sub`
    * `subMonth`: the quantity of months the user has already subscribed for
    * `subName`: the subscribing user’s display name
* `subPrime`
    * see `sub`
* `subGiftContinued`
    * `subGiftGifter`: the user gifting a subscription
    * `subName`: the subscribing user’s display name
* `subGiftSingle`:
    * `subGiftCountTotal`: the total amount of already gifted subscriptions by this user on this channel
    * `subGiftGifter`: the user gifting a subscription
    * `subGiftRecipient`: the user receiving a subscription
* `subGiftMulti`
    * `subGiftCount`: the quantity of subscriptions beeing gifted by the user
    * `subGiftCountTotal`: the total amount of already gifted subscriptions by this user on this channel
    * `subGiftGifter`: the user gifting a subscription


### 3.7 Answer types: sequential vs. random

Willowbot’s default behaviour is just sending the string that is defined in the `answer` key of the respective matching reaction. However, Twitch has an internal message limit of 500 characters. Usually, this limit will not be exceeded by your answer strings, but what if you want to send more comprehensive information to the chat, e.g. a story recap for the currently played game? No, you will not have to define multiple commands for that, like `recap1`, `recap2`, etc. Instead, you just put your answer into one command definition, no matter how many characters. Willowbot has a built-in function that will split your answer string into chunks of at most 500 characters (less, if the last word in a chunk exceeds the 500th character or if, of course, there are not enough characters in the remaining string to reach the limit) and send one at a time with no considerable delay in between.

There are situations where you might want to send sequential reactions on purpose. One has been mentioned in the context of blacklisting terms. Some emotes are very flashy and can potentially trigger photosensitive people. So if you ban such emotes from your channel, you might not just want to delete messages containing them, but also inform your viewers about why their message has been deleted. This is how you would do that:
```
commands = {
  "colorFlash" : {
    "answer"    : "/delete $msgID\n/announce Please be aware that we want to avoid emotes in the chat that could trigger photosensitive people. Thank you.",
    "matchType" : "contains"
  }
}
```
Assuming that `colorFlash` is a colourful and flashy emote, the reaction definition above will do two things as soon as a message that contains this emote appears in the chat: At first, Willowbot will delete the message (`/delete $msgID`). Afterwards, it starts a new own message (`\n`) and makes an announcement about the deleted chat message (`/announce Please be aware …`). As you can see, we can split one answer string into separate chat messages by using the newline character (`\n`). This can be done as often as you want and you can so generate as many consecutive messages as you want.

There is a second answer mode supported by Willowbot, namely random answers. One imaginable use case is a little community game:
```
commands = {
  "!loot" : {
    "matchType"  : "startsWith",
    "answer"     : "$senderDisplayName loots cookies from $arg0.\n$senderDisplayName loots 40 coins from $arg0.\n$senderDisplayName loots an old sock from $arg0.\n$senderDisplayName loots stinky cheese from $arg0.\n$senderDisplayName loots underpants from $arg0.",
    "answerType" : "random"
  }
}
```
If user McFluffy triggers this command by sending `!loot someUser` to the chat, Willowbot will randomly pick one of the answers in the `answer` key and show it in the chat, e.g. `McFluffy loots and old sock from someUser.`


### 3.8 OS commands

Besides sending messages to the chat, Willowbot allows you to execute any system command you like (unless the command requires root/administrative access to the system and Willowbot does not run with those privileges, which is *highly recommended*). You will mostly use this to play sounds or videos, but you could also make Willowbot log certain events to a file.

As an example, we define a command that will let your viewers cheer you for achieving something great in your gameplay and play a sound:
```
commands = {
  "!gg" : {
    "matchType"  : "startsWith",
    "os-command" : "start C:\the\path\to\my\soundfile.mp3"
  }
}
```
Whenever a user sends `!gg` to the chat (or another message that at least starts with that term), your system will play the sound located at `C:\the\path\to\my\soundfile.mp3`. Beware that the definition above will only work on Windows systems! Unix systems will need a command like `playsound /home/[user]/where/my/soundfiles/dwell.mp3`, depending on the software installed on your system. Such OS commands are processed in addition to `answer` strings, i.e. you may combine them and send a message to the chat as well as play a sound, log an action, play a video, or whatever you want to do in your OS command.


### 3.9 Debug messages

If you want to check your commands without sending messages to the chat, you can use Willowbot’s `debug` key. It behaves just like your normal `answer` key string, including resolved arguments and placeholder variables, but the result will not be sent to the chat and instead be printed to the console. `answer` and `debug` (and `os-command`) are processed independently, so you may define those keys in any combination and for any purpose you like.


## 4 Concluding words

Willowbot has been in development for months and extended piece by piece whenever new scenarios to be covered arose. By no means it should be considered feature complete, but it still is and probably will be for a long time under active development, including efforts to make Willowbot more accessible.

Feel free to use the code as an inspiration for your own IRC projects and to report any issues that arise. I will try to fix them as soon as possible.


## Appendix

### Implemented key checks

* `answer`
    * type: string
    * bot’s answer to a command/message pattern
* `answerType`
    * type: string
    * `sequence` [Default], `random`
* `cooldown`
    * type: integer
    * do not allow the command to be triggered again before this timespan has elapsed; in seconds
* `debug`
    * type: string
    * debug message; will be displayed on the console only and will not be sent via IRC
* `interval`
    * type: integer
    * for timed commands; in seconds
* `level`
    * type: integer
    * exact level needed to trigger the command
* `matchType`
    * type: string
    * `is` [Default], `startsWith`, `contains`, `contains_caseInsensitive`, `endsWith`, `regex`
* `maxSubLevel`
    * type: integer
    * maximum subscription count needed to trigger the associated message
* `minLevel`
    * type: integer
    * minimum level needed to trigger the command
* `minRaidersCount`
    * type: integer
    * minimum count of raiders needed to trigger the associated message
* `minSubLevel`
    * type: integer
    * minimum subscription count needed to trigger the associated message
* `os-command`
    * type: string
    * a system command that will be executed if the other conditions are met (level, cooldown, pattern, etc.)
* `subLevel`
    * type: integer
    * subscription count needed to trigger the associated message
* `suppressFollowupSingles`
    * type: boolean
    * used in conjunction with `triggerType` `subGiftMulti` only; suppresses the evaluation of single-subscription gift messages showing up after the multi-subscription gift until the according quantity of the multi-subscription gifts is reached
* `triggerType`
    * type: string
    * `raid`, `sub`, `subGiftContinued`, `subGiftMulti`, `subGiftSingle`, `subPrime`


### List of placeholder variables

Variables for bot answers, which are resolved before Willowbot sends its message:

* `arg0`, `arg1`, `arg2`, etc.<br>the arguments passed to the command
* `arg0+`, `arg1+`, `arg2+`, etc.<br>concatenate all arguments from the *n*th one onwards, separated by blank spaces
* `msgID`<br>ID of the processed message; needed for deleting specific messages
* `raidersChannel`<br>the channel which the raiders are coming from
* `raidersCount`<br>quantity of raiders joining the channel
* `senderDisplayName`<br>sender’s display name
* `senderName`<br>sender of the processed message
* `subGiftCount`<br>amount of subscriptions gifted in one gift action
* `subGiftCountTotal`<br>total amount of subscriptions a user has already gifted
* `subGiftGifter`<br>gifting user’s display name
* `subGiftRecipient`<br>gift-receiving user’s display name
* `subMonth`<br>number of months the user has already subscribed for
* `subName`<br>subscribing user’s display name