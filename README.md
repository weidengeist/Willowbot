# Willowbot

— [Zur deutschen Version wechseln](https://github.com/weidengeist/Willowbot/blob/main/README_de.md)

## Contents

* [Introduction](https://github.com/weidengeist/Willowbot#introduction)
* [1 Installation](https://github.com/weidengeist/Willowbot#1-installation)
* [2 Initial setup](https://github.com/weidengeist/Willowbot#2-initial-setup)
* [3 Creating command sets](https://github.com/weidengeist/Willowbot#3-creating-command-sets)
    * [3.1 User-triggered commands](https://github.com/weidengeist/Willowbot#31-user-triggered-commands)
        * [3.1.1 Simple matching](https://github.com/weidengeist/Willowbot#311-simple-matching)
        * [3.1.2 Advanced matching: regular expressions](https://github.com/weidengeist/Willowbot#312-advanced-matching-regular-expressions)
    * [3.2 Aliases](https://github.com/weidengeist/Willowbot#32-aliases)
    * [3.3 Timed commands](https://github.com/weidengeist/Willowbot#33-timed-commands)
    * [3.4 Cooldowns](https://github.com/weidengeist/Willowbot#34-cooldowns)
    * [3.5 Level system](https://github.com/weidengeist/Willowbot#35-level-system)
        * [3.5.1 Base system](https://github.com/weidengeist/Willowbot#351-base-system)
        * [3.5.2 Further restrictions](https://github.com/weidengeist/Willowbot#352-further-restrictions)
    * [3.6 Placeholder variables](https://github.com/weidengeist/Willowbot#36-placeholder-variables)
    * [3.7 Trigger types: raids and subscriptions](https://github.com/weidengeist/Willowbot#37-trigger-types-raids-and-subscriptions)
        * [3.7.1 Raids](https://github.com/weidengeist/Willowbot#371-raids)
        * [3.7.2 Subscriptions](https://github.com/weidengeist/Willowbot#372-subscriptions)
    * [3.8 Answer types: sequential vs. random](https://github.com/weidengeist/Willowbot#38-answer-types-sequential-vs-random)
    * [3.9 OS commands](https://github.com/weidengeist/Willowbot#39-os-commands)
    * [3.10 Debug messages](https://github.com/weidengeist/Willowbot#310-debug-messages)
* [4 Optional/Custom modules](https://github.com/weidengeist/Willowbot#4-optionalcustom-modules)
    * [4.1 Accessing custom modules: the `function` key](https://github.com/weidengeist/Willowbot#41-accessing-custom-modules-the-function-key)
    * [4.2 `poll` module](https://github.com/weidengeist/Willowbot#42-poll-module)
    * [4.3 `modChannelInfo` module](https://github.com/weidengeist/Willowbot#43-modchannelinfo-module)
    * [4.4 `dateDiff` module](https://github.com/weidengeist/Willowbot#44-dateDiff-module)
* [5 Test/Debugging mode](https://github.com/weidengeist/Willowbot#5-testdebugging-mode)
* [6 Concluding words](https://github.com/weidengeist/Willowbot#6-concluding-words)
* [Appendix](https://github.com/weidengeist/Willowbot#appendix)
    * [Implemented key checks](https://github.com/weidengeist/Willowbot#implemented-key-checks)
    * [List of placeholder variables](https://github.com/weidengeist/Willowbot#list-of-placeholder-variables)
    * [List of debug message patterns](https://github.com/weidengeist/Willowbot#list-of-debug-message-patterns)
    * [List of command line options](https://github.com/weidengeist/Willowbot#list-of-command-line-options)


## Introduction

This is a chat bot intended to be used on Twitch. It allows you to configure custom commands, optionally based on regular expressions, which the bot will react to – either with an answer in the chat or by executing an OS command. It also supports timed commands and has an integrated level system to limit the usage of commands to different user groups.

The instructions and descriptions below are written especially for non-programming users to make Willowbot more accessible. Feedback for further improvements in this regard is always welcome.


## 1 Installation

You need to have installed an interpreter for the programming language [Python in at least version 3.9](https://www.python.org/downloads/) (the latest version is recommended) to use Willowbot. The recommended option for Windows users is the Windows installer (64 bit) as it will do most of the configuration for you without any difficulties to surmount. After having successfully installed Python, download the Willowbot package and unzip it to a location to your liking.


## 2 Initial setup

Open a console (on Windows: start `cmd`; on Linux/Mac: press Ctrl+Alt+T (on most desktop environments) or search for `terminal` in your application menu). Navigate to the directory where Willowbot is located by typing `cd`, followed by a blank space and the Willowbot location, e.g.
```
cd C:\Programs\Willowbot
```
on Windows or
```
cd /home/thatsme/Willowbot
```
on Linux/Mac. Now create the initial config files by typing
```
python main_cli.py --configure
```
and pressing the Enter button. Depending on your Python installation, it might be necessary to use `py` or `python3` instead of `python`.

If everything is installed correctly, you should now be presented Willowbot’s message that and where it has created a config and a logins file for you. The default directories for those files (`config.py` and `logins.py`) are the following ones:

* Windows: `%appdata%\twitch\willowbot\`
* MacOS: `/home/[user]/Library/Preferences/twitch/willowbot/`
* Linux: `/home/[user]/.config/twitch/willowbot/`

**Beware!** Aforementioned procedure has only been tested on Linux. If any information about the steps needed on Windows is incorrect and/or does not work, please let me know.

Now generate an access token for Willowbot. But before you proceed, make sure that there is no active Twitch session in your browser, so log out or even delete the according session cookie. Afterwards, you are ready to generate the token by invoking Willowbot with the `--token` option, followed by the keyword `get`:
```
python main_cli.py --token get
```
This should open your default browser will open your default web browser and present you Twitch’s authorization page for access tokens. Log into your bot’s account and click »Authorize«. Afterwards, you will be redirected to a page explaining how to add the just generated key to your logins file. Follow those instructions.

After having added the key, set Willowbot’s default login name to the name which you have just generated an access token for:
```
python main_cli.py --set-config botname iamabot
```
`iamabot` is just a placeholder; you have to provide the actual bot account name.

You can now start Willowbot by simply typing
```
python main_cli.py 
```
and it will connect to the channel you have specified as `botname`. In practice, however, you will of course want to use Willowbot on your personal broadcaster channel or – if you are a moderator – on another channel where you have moderator privileges. To do so, start Willowbot with the `--channel` option, followed by the name of the channel Willowbot is supposed to join:
```
python main_cli.py --channel myownchannel
```
Obviously, you have to replace `myownchannel` with the actual name of the appropriate channel where Willowbot is supposed to do its duty and run a specific set of commands.


### Hints on migrations (first-time users may skip this part)

If you have used Willowbot before (earlier than March 2023), you have to change a few things in your commands to ensure that they will still work with the new Twitch API. You may still use the chat commands `/ban` and `/timeout`; they have been mapped to the new API endpoints. However, their argument is no longer `$senderName`, but `$senderID`.

Moreover, Willowbot now supports API shoutouts and API announcements. To use them, simply use the legacy commands `/shoutout` or `/announce`.


## 3 Creating command sets

Besides a directory for the general Willowbot/IRC configuration, this program will create a subdirectory named `commands` in this configuration directory. This is where you have to put the command sets you want your bot to use. You can create command sets for multiple channels; each set is a separate file named by the channel where you want it to be used. (This might come in handy if you are a moderator of more than one channel.) From now on, let’s assume your bot is named IAmABot, i.e. uses the Twitch login iamabot. For testing your commands, it is highly recommended to use your bot’s own channel, so let’s create a command set for that now.

The commandsets themselves are small scripts written in the programming language Python, doing nothing but assigning a so-called [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) to a `commands` variable wherein all your command information is stored. Create a file called `iamabot.py` (as this is the channel where we want to do some tests; please note: Use small letters only!) where you can put your command checks and bot reactions.

There is a `commandsTemplate.py` file included in the Willowbot repository which contains most of the example commands mentioned in this Readme file in the sections below. However, further reading instead of just copying and pasting from the template file is *strongly recommended* as you will certainly run into difficulties when doing otherwise.


### 3.1 User-triggered commands

As a start, put the skeleton for your commands into your `iamabot.py` file:
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
`answer` is called a key in our dictionary; the actual answer is called a value. We will use those term more often in the descriptions ahead.

The value of our `answer` key works just like an ordinary [Twitch chat command](https://help.twitch.tv/s/article/chat-commands), i.e. you can precede your answer with `/me` or `/announce` to emphasize it if you like.


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
Now you can trigger the bot’s answer by e.g. `!bsg @randomtwitchuser`. Note the comma at the end of the line with `answer`! The order of the key definition does not matter; `matchType` can be set before `answer` as well.

The other `matchType` options available in Willowbot are `is` (default value; not necessary to be set explicitly), `is_caseInsensitive`, `contains`, `endsWith`, `regex` (more on that later), and `contains_caseInsensitive`. The last one is mainly for convenience reasons, however, it is recommended to use regular expressions (option `regex`) instead.


#### 3.1.2 Advanced matching: regular expressions

Most use cases should be covered by the simple matching keywords. If you feel in need of more control about the messages that are supposed to make Willowbot react in a certain way, regular expressions can be evaluated.

Regular expressions are a very powerful tool and therefore might look intimidating at first, but don’t worry. You will be shown how to use them by very simple first examples, which will probably suffice to teach you all you need for using Willowbot efficiently.

For example, you would like to have a `!multi` command to tell your viewers whom you are currently playing with. If you want this message to also be displayed when sending `!Multi`, you could of course simply input the same `!multi` command block again and replace `m` with `M`. A more elegant way is using a regular expression instead:
```
commands = {
  "^![Mm]ulti" : {
    "answer"    : "Today we are playing with someone very special.",
    "matchType" : "regex"
  }
}
```
The symbol `^` means that the message starts with the pattern following it, so `^` in the `matchType` `regex` can replace `startsWith`. The so-called character set `[Mm]` means just what we want to achieve: Either of these two letters may introduce the command.

What happens if there is a command `!multi` as well as `!multiplayer`? The command definition above would be triggered by a `!multi` command and by a `!multiplayer` command in the chat. So it is reasonable to tell Willowbot that the command is a distinct term which may not be arbitrarily extended into another word. This is realized by `( |$)`:
```
commands = {
  "^![Mm]ulti( |$)" : {
    "answer"    : "Today we are playing with someone very special.",
    "matchType" : "regex"
  }
}
```
This construction means: React to chat input that starts with `!multi` or `!Multi` and continues with a blank space (in case a user wants to, e.g., add `@anotherUser` as a ping) or is then complete and ends the message (`$`).

Willowbot’s regex feature also supports using so-called capture groups in its answers. That means that you can take out parts of the message that triggered the bot reaction to re-use them in your answer.

Some commonly used bots on Twitch which are not as flexible as Willowbot automatically delete links posted by non-subscribers, even though it is a link to a clip created on Twitch itself. To correct this behaviour, you can teach Willowbot to extract the URL leading to the clip and repost it with moderator privileges:
```
'.*(https://clips.twitch.tv/[^ ]+).*' : {
  'matchType' : 'regex',
  'answer'    : 'Thanks for your clip, $senderDisplayName. Unfortunately, links posted by non-subs are deleted by one of our bots on this channel. We repost it for you: \1',
  'level'     : 1
},
```
The pattern used here makes Willowbot react to URLs leading to a Twitch clip. But there is something special in the pattern: the parentheses. It tells the bot to »save« the expression within them. You can then access those saved parts by typing `\1`, `\2`, `\3`, etc. in your answer to match the contents within the 1st, 2nd, 3rd, etc. pair of parentheses.


### 3.2 Aliases

Knowing about regular expressions, we are now able to define aliases for our commands, i. e. multiple command triggers for one and the same reaction. A simple example should be enough to show how this works:
```
commands = {
  "^!([Mm]ods?|[Ss]kyrim|[Gg]ame)" : {
    "answer"    : "We are currently playing »Enderal: Forgotten Stories«, a total conversion mod for »The Elder Scrolls V: Skyrim«.",
    "matchType" : "regex"
  }
}
```
As this command contains multiple different regex structures, let’s break this apart a little more detailed. At first, you can see that there is a chain of words enclosed in parentheses and separated by a vertical dash (`(a|b|c)`). This means that the defined answer can be triggered by either of those words.

One section above, you have learned about character sets, and you can see those again in the command defined here. So you can trigger the answer either by `!mod`, `!Mod`, `!skyrim`, `!Skyrim`, `!game`, or `!Game`.

»But wait! There is a question mark after `![Mm]ods`!«, you might interpose now. »And why is it `!mods` now instead of `!mod`?« The question mark is a special character in the context of regular expressions. It means that the character before it is optional, i. e. you can not only trigger the answer by posting `!mod` or `!Mod`, but also by `!mods` and `!Mods`.


### 3.3 Timed commands

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
    "answer"    : "Please stay hydrated!",
    "matchType" : "startsWith"
  }
}
```
Please note the comma in line 5 after `}`! The command definition blocks (`{…}`) inside your `commands` dictionary have to be separated by commas from each other.


### 3.4 Cooldowns

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


### 3.5 Level system

#### 3.5.1 Base system

To limit the access to your commands, Willowbot provides a level system. Every user in the chat is assigned a level based on his/her role and chat experience. The following levels are implemented:

* 0: the user posts the very first time ever on this channel;
* 1: ordinary user who has been on this channel before but is no subscriber;
* 2: subscribers;
* 3: moderators;
* 4: broadcasters.

To make Willowbot check the user’s level before sending an answer, you have to use the keyword `level` or `minLevel`. A few examples shall explain this further.

The most common scenario for the levels is to determine a minimal level that is required to issue a command. For a command that can only be used by the channel moderators and the broadcaster, you have to use the `minLevel` option and set it to 3:
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
Besides a level definition, this command uses the regular expression `.*` to match messages containing *any* character (`.`) occuring 0 or more (`*`) times. We will have a closer look at such asterisk patterns and how to use them efficiently in the following section 3.6.


#### 3.5.2 Further restrictions

In addition to the aforementioned levels, a command can be restricted to be used by VIP users only by passing the key `needsVIP` and setting the boolean `True`.
```
commands = {
  "^!vip( |$)" : {
    "answer"    : "I am a VIP, so only I can use this command.",
    "matchType" : "regex",
    "needsVIP"  : True
  }
}
```
Note: Booleans (`True` and `False`) don’t have, unlike strings, quotation marks.

If you want to build your own level system besides the roles assigned by Twitch, based upon subscription months, the keys `minSubLevel`, `subLevel`, and `maxSubLevel` are available. So you can determine that a minimal number of subscriptions months is needed to use certain commands (`minSubLevel`), restrict the usage to an interval of subscription months (`minSubLevel` in conjunction with `maxSubLevel`) or intend only one specific month for the command (`subLevel`). The values for those keys are integers, so like booleans they don’t use quotation marks in the command definition.


### 3.6 Placeholder variables

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
»Why would we want to do this?«, you might ask. `$arg1+` does not only catch the second word after `!give` like `$arg1` would do, but it gathers all words from the second one onward. So in contrast to the version shown before, our new `!give` command will now catch more than just two arguments. In our first `!give` version, we could only give McFluffy »some blanket to feel cozy«. With the new command we can `!give McFluffy a very warm blanket` to feel cozy. Just a blanket is still possible, though.

Do you want to spread some love in your chat? Enable your viewers to virtually hug each other by defining a command for that action:
```
commands = {
  "!hug" : {
    "answer"    : "$senderDisplayName gives $arg0 a hug.",
    "matchType" : "startsWith"
  }
}
```
This command introduces another placeholder variable: `senderDisplayName`. On Twitch, every user has a login name and a display name. Those are almost identical; the only difference is that the login name uses only small letters whereas the display name may also contain capital letters. By putting `$senderDisplayName` into our answer we can use the name of the user who issued the command. So if user McFluffy sends the command `!hug Kittycat`, our definition above would result in the message: `McFluffy gives Kittycat a hug.` (Side note: If you use `$senderName` instead of `$senderDisplayName`, the message would read: `mcfluffy gives Kittycat a hug.`)

Another very useful purpose for placeholders is timeouting or banning scam bots entering the chat. If such a scam bot is known to use the message »Buy followers, subs, and viewers: [URL]«, you can easily ban the bot account from your channel as soon as this message shows up in your chat:
```
commands = {
  "Buy followers" : {
    "answer"    : "/ban $senderID",
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
    "answer"    : "/ban $senderID",
    "matchType" : "regex",
    "level"     : 0
  }
}
```
A short explanation for the regex used here: A user will be banned if his/her first message ever in the chat starts (`^`; cf. `^[Mm]ulti` in section 3.1.2) with »Buy«, followed by arbitrary characters (`.`) in a quantity of 0 or more (`*`) and afterwards the word »followers«. By putting `.*` before `followers`, you can catch a scam bot message even if it varies the order of words (»Buy followers, subs, and viewers«, »Buy subs, followers, and viewers«, etc.).

Another fancy example for banning scam bots:
```
commands = {
  "^(Wanna|Want to) become famou?s" : {
    "answer"    : "/ban $senderID",
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
The command definition above will delete all Messages which contain the terms/emotes »Kappa«, »failFish«, or »LUL«. For this action we need the ID of the message you want to delete. That ID is represented by the placeholder variable `msgID`. The advantage of using this method instead of the Twitch blacklist: You and your moderators will be able to see the message and its problematic content and, if necessary, take further actions in case of severe discrimination or harassment, whereas messages with Twitch blacklist terms would be suppressed before any moderator can see it and have a chance to report the user to Twitch. In the section about answer types we will see how to extend this command and make it even more useful.


### 3.7 Trigger types: raids and subscriptions

The chat messages sent on Twitch all contain special meta data and can so – among others – be differentiated between user messages, subscriptions, and raids. In contrast to the user message commands, which you define by providing a word or pattern that has to be matched by a message, raid and subscription messages can have an arbitrary name. You tell Willowbot under which circumstances the reaction is supposed to be triggered by providing a `triggerType` key.

Willowbot’s default behaviour is processing messages that appear in the chat as user messages. Invisible to the common user, special messages are sent in the background. Those contain information about raids and subscriptions, among others. If you want Willowbot to handle those, you have to include the appropriate `triggerType` value in your command definition.


#### 3.7.1 Raids

Let’s start off simple by defining a command that handles raids:
```
commands = {
  "myRaid" : {
    "answer"      : "$raidersChannelName joins us with $raidersCount viewers. Have fun!",
    "triggerType" : "raid"
  }
}
```
It is important to set `triggerType` `raid` in this definition. Otherwise, Willowbot would print the answer string to the chat as soon as someone’s complete message reads »myRaid«.

As it has been mentioned above, it is not necessary to provide a special pattern for this kind of message handlers. However, you *have* to provide a unique identifier (in this case: `myRaid`) for the handler. Non-unique, i.e. multiply used identifiers, will overwrite other already defined commands with the same identifier/pattern so that only the one defined last will exist and be able to be processed.

You can see two more placeholder variables in the answer: `raidersChannelName` and `raidersCount`. As soon as an incoming raid is detected, those placeholders will be replaced with the channel that sends you its viewers and the number of viewers, respectively.

Commands with the `raid` type also support a `minRaidersCount` key. If this key is set, the according reaction will only be triggered if the raid consists of at least the specified quantity of people.


#### 3.7.2 Subscriptions

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
The trigger types `sub`, `subPrime`, and `subGiftContinued` support the keys `subLevel`, `minSubLevel`, and `maxSubLevel`. Those allow you to differentiate even more between subscriptions by sending special messages only for a distinctive (minimal or maximal) amount of subscribed months.
```
commands = {
  "very long sub" : {
    "answer"      : "$subName has been a subscriber for more than a year now! Congratulations on $subMonth months in our community.",
    "minSubLevel" : 13,
    "triggerType" : "sub"
  },
  "any other sub month 9–12" : {
    "answer"      : "$subName has just subscribed for month $subMonth.",
    "triggerType" : "sub",
    "minSubLevel" : 10,
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


##### Supported placeholders per subscription context

* `sub`
    * `subMonth`: the quantity of months the user has already subscribed for
    * `subName`: the subscribing user’s display name
* `subPrime`
    * see `sub`
* `subGiftContinued`
    * `subGiftGifter`: the user having originally gifted the continued subscription (display name)
    * `subName`: the subscription-continuing user’s display name
* `subGiftSingle`:
    * `subGiftCountTotal`: the total amount of already gifted subscriptions by this user on this channel
    * `subGiftGifter`: the user gifting a subscription (display name)
    * `subGiftRecipient`: the user receiving a subscription (display name)
* `subGiftSingleFollowup`:
    * see `subGiftSingle`
* `subGiftMulti`
    * `subGiftCount`: the quantity of subscriptions being gifted by the user
    * `subGiftCountTotal`: the total amount of already gifted subscriptions by this user on this channel
    * `subGiftGifter`: the user gifting the subscriptions


### 3.8 Answer types: sequential vs. random

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
If user McFluffy triggers this command by sending `!loot someUser` to the chat, Willowbot will randomly pick one of the answers in the `answer` key separated by `\n` and show it in the chat, e.g. `McFluffy loots an old sock from someUser.`


### 3.9 OS commands

Besides sending messages to the chat, Willowbot allows you to execute any system command you like (unless the command requires root/administrative access to the system and Willowbot does not run with those privileges, which is *highly recommended*). You will mostly use this to play sounds or videos, but you could also make Willowbot log certain chat events to a file.

As an example, we define a command that will let your viewers cheer you for achieving something great in your gameplay by playing a sound:
```
commands = {
  "!gg" : {
    "matchType"  : "startsWith",
    "os-command" : "start C:\the\path\to\my\soundfile.mp3"
  }
}
```
Whenever a user sends `!gg` to the chat (or another message that at least starts with that term), your system will play the sound located at `C:\the\path\to\my\soundfile.mp3`. Beware that the definition above will only work on Windows systems! Unix systems will need a command like `playsound /home/[user]/where/my/soundfiles/dwell.mp3`, depending on the software installed on your system. Such OS commands are processed in addition to `answer` strings, i.e. you may combine them and send a message to the chat as well as play a sound, log an action, play a video, or whatever you want to do in your OS command.


### 3.10 Debug messages

If you want to check your command definitions, i.e. whether Willowbot will react to certain events/patterns the way you are intending, and need feedback about the reaction, but you don’t want to send messages to the chat for that purpose, you can use Willowbot’s `debug` key. The string in your `debug` key will behave as if it was an `answer`, however, it will not be sent to the chat but be output on the console. Resolving arguments and placeholder variables is also featured in the `debug` key. `answer` and `debug` (and `os-command`) are processed independently, so you may define those keys in any combination and for any purpose you like.


## 4 Optional/Custom modules

Willowbot consists of various core modules. However, there are situations that might require some more complex actions than just reacting to a chat message by sending another message to the chat. This is where custom modules come into play. Those are Python scripts as well and provide you the full capabilities of Python to extend Willowbot’s functionality.

To keep all routines and variables properly sorted and to minimize the risk of unintentionally overwriting already defined ones, it is recommended to prefix them with the module name, e.g. if you have a custom module named `giveaway`, you should name the routines and variables within this module `giveaway_doStuff()`, `giveaway_entries`, `giveaway_doSomeOtherThings()`, and so on.

Those optional modules can be activated an deactivated via a list called `activeModules`¹. Willowbot will only use the optional modules that are present on that list, so don’t forget to put your module on it. If you get into trouble with a distinct module (error, unexpected behaviour, conflicts with other modules, etc.), you don’t have to completely delete it from the list or even from the `modules_opt` directory, but you can just uncomment it by preceding its entry in `activeModules` with `#`. Those uncommented modules won’t be loaded when Willowbot starts.

¹ Windows users beware! This file has no extension, but it can be opened and edited with any text editor (e. g. Notepad). Make sure that it still has no file extension when you save your changes. If this design decision is an aspect to take very much care of and a common source of errors, please let me know.


### 4.1 Accessing custom modules: the `function` key

Calling one of the routines provided by your custom module is achieved by using the `function` key in your command definition. The value for that key is a list of strings with the routine names and the passed arguments where necessary. Those routines are processed in the same order as they appear in the list. Since writing your own modules requires profound knowledge in Python programming, it is considered a technique for experienced users. Please be aware of that if you want to extend Willowbot.


### 4.2 `poll` module

A first optional module is already provided in this repository and enables your viewers to take part in a quick poll, initiated simply by a chat command issued by moderators or the broadcaster. As mentioned in the introduction of this section, we use the poll-initiating routine provided by the module via using the `function` key in our command definition:
```
commands = {
  '!poll' : {
    'matchType' : 'startsWith',
    'debug'     : 'Poll has been started.',
    'function'  : ['poll_start(commands, irc, "$arg0+")'],
    'minLevel'  : 3
  }
}
```
Before turning to the most interesting part, let’s quickly summarize what other things than calling a `poll` routine happens in this command definition. The poll is started as soon as a user of at least level 3 (moderator or broadcaster) sends a message to the chat that `startsWith` `!poll`. As soon as that happens, there will be a short message on the console that a `Poll has been started.` The key newly introduced in this section and used in the command definition above is `function`. Its value calls the routine defined by `def poll_start(commands, irc, *args)` in the `poll` module and passes the required arguments. As the `poll` module manipulates the command set, it needs `commands` as an argument. Furthermore, we want the module to be able to send messages to the chat, so it needs access to our `irc` connection. Finally, we hand over all the arguments sent to the chat together with the `!poll` command (`"$arg0+"`).

To actually start a poll, you would send a command like `!poll 30 left right forward` to the chat. This will initiate a poll that will last 30 seconds and allow the viewers to choose where to go next in the currently played game – left, right, or forward – by sending the appropriate word to the chat. An according message will appear in the chat. Willowbot will then gather the votes sent by the users and put them into a list that will eventually be evaluated. Every user can vote only once, but he/she may change his/her vote by just sending another of the available options to the chat. After the time passed to the `!poll` command has elapsed, the poll will be summarized and Willowbot sends a list of the results to the chat, shown in percentage terms and in descending order, from the option with the most to the one with the fewest votes.

Currently, only German information messages are deposited in the module and changing them into another language requires modifying the module itself.


### 4.3 `modChannelInfo` module

This module enables your bot to both retrieve and modify the title as well as the category of a channel. The prerequisite, though – at least for modifying –, is an access token for the channel the date of which you want to change. If such an acccess token is not available when entering a channel, Willowbot will notify you about that with a message pointing that out when establishing the connection.

If you are a moderator on a channel that is not your own, but you want to use Willowbot’s ability to change channel information there, you will need the maintaining broadcaster’s Willowbot access token. <b>This bears a considerably increased risk!</b> A moderator in possession of a broadcaster’s access token is enabled to use Willowbot with another person’s identity and in turn put false colors upon another user. Only exchange tokens with persons whom you fully trust! In the event of suspected abuse of a token, revoke and invalidate it immediately (`--token revoke`)!

Following the name scheme for optional modules suggested in this chapter, the names of the routines provided by `modChannelInfo` are the following:

* `modChannelInfo_title_get`
* `modChannelInfo_title_set`
* `modChannelInfo_category_get`
* `modChannelInfo_category_set`

Each of these routines requires an instance of an IRC connection as well as the Willowbot configuration as mandatory arguments. The optional arguments are messages in case of a successful request, in case of a failed request, and arguments for the desired title or category, respectively, in case of the `set` method.

The following command definitions are examples for modifying and getting titles and categories:
```
'^!title( |$)' : {
  'matchType' : 'regex',
  'function'  : ['modChannelInfo_title_get(irc, CONFIG, "The current title is »$return«.", "Could not retrieve the title information.")'],
},
'^!title-set( |$)' : {
  'matchType' : 'regex',
  'function'  : ['modChannelInfo_title_set(irc, CONFIG, "$arg0+", "Title has been changed to »$return«.", "Could not change the title.")']
},
'^!game( |$)' : {
    'matchType' : 'regex',
    'function'  : ['modChannelInfo_category_get(irc, CONFIG, "The current category is »$return«.", "Could not retrieve the category information.")'],
},
'^!game-set( |$)' : {
  'matchType' : 'regex',
  'function'  : ['modChannelInfo_category_set(irc, CONFIG, "$arg0+", "Potential candidates: $return. Change the game by typing !game-set [number] or send a new request.", "Category has been set to »$return«.", "Could not set the category.")']
}
```
The `title_get` function may be called in a simplified way by invoking `modChannelInfo_title_get(irc, CONFIG)`, however, there will be no feedback about the title in the chat then. The first optional argument is the text being returned after a successful server request:
```
The current title is »$return«.
```
It contains the placeholder `$return`. Within the `modChannelInfo` module it is replaced with the current stream title of the queried stream. In case of a failure during the server request the second optional argument of the function will be sent to the chat.

`title_set` requires, of course, the new title that is supposed to replace the current one and is passed by the user. It is the first optional argument for the routine, used above as `$arg0+`, i.e. a placeholder that collects all text elements after `!title-set`.

The routine `category_get` works analogously to `title_get` and merely uses both a success and a failure message as optional arguments.

The most complex function in this module is `category_set`. Just like `title_set` it gathers the passed arguments (`$arg0+`) and passes them to the function in their entirety. They are handled as a string that should match one of the categories available on Twitch as much as possible. If only one category exists that matches this string, the category of the running broadcast will be set to that category. In case of an ambiguous request the module will show up to ten entries in a numbered list in the chat the context of which is determined by the second optional argument – in the example above it’s `Potential candidates: $return. Change the game by typing !game-set [number] or send a new request.` `$return` is replaced with a list with the format `Game title (1), another game title (2), […]`. This list is saved in the background by Willowbot. You may now use the `!game-set` command again, but instead of querying for a distinct category you may now choose one of the numbers of the list output before and append it to the command, e.g. `!game-set 4`, and the `modChannelInfo` module will change the broadcast category to the one associated with that number. Afterwards, that internal list will be deleted, which means that this procedure may only be repeated by a new query with a category name.


### 4.4 `dateDiff` module

A very popular command is getting the time remaining until a certain event happens, e.g. a game presentation or the streamer’s birthday. That’s what the `dateDiff` module can be used for. It allows you to calculate the difference between two dates as well as the one between the time of sending the command linked to this module and a target date.

The core function supposed to be used by the end-user is `dateDiff_send`. It uses the following parameters:
* `irc`: mandatory.
* `targetDate`: mandatory; a string in ISO format [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss] or [MM]-[DD]; if the latter variant is used, Willowbot will assume the next occurrence of this month-day combination, i.e. either the current or the next year.
* `nowDate`: optional, default: `""`; see `targetDate`; if this parameter is omitted, the actual current date and time will be used instead of the one expressed by the provided string.
* `contextString`: optional, default: `{dateDiff}`; the string you want to appear in the chat when the command associated with `dateDiff_send` is used, with `{dateDiff}` being automatically replaced by a string in a natural language, expressing the date difference in words.
* `useAccusativeMod`: optional, default: `False`; some languages, like German, use a suffix for expressing the accusative and this boolean parameter tells Willowbot if it shall be used when composing the natural language date difference string.
* `languageOverride`: optional, default: `""`; if you want Willowbot to compose the date difference string in another language than the one Willowbot is launched with, use this parameter with a language code being present in the `./lang` subdirectory.

An example definition for a command using `dateDiff_send` is the following:
```
'^!bday( |$)' : {
    'matchType' : 'regex',
    'function'  : ['dateDiff_send(irc, targetDate = "04-08", contextString = "The channel owner’s next birthday will be in {dateDiff}.")']
  }
```

When a chat participant issues the command `!bday`, the bot will (for example) answer `The channel owner’s next birthday will be in 221 days, 12 hours, 10 minutes and 17 seconds.` The date difference string is inserted where `{dateDiff}` appears in the `contextString` parameter and in this case it is the time remaining until April 8th.


## 5 Test/Debugging mode

Willowbot allows you to test your command definitions either by a specific message text or by a series of predefined message types, so you won’t have to wait for a distinct message to appear in the chat to be able to test the correctness of your command sets. To do so, you have to pass the `--debug-single` option in conjunction with a message or the `--debug-full` option when starting Willowbot. In this mode, no connection to the Twitch chat will be established and the `answer` strings will be printed to the console instead of being sent to the chat.

The first case is triggered as follows:
```
python main_cli.py --channel iamabot --debug-single "!mod @anotherUser There you go."
```
What happens here is that Willowbot will load the command set for the channel `iamabot`, process the string `!mod @anotherUser There you go.` as if it had been a user message in the chat, and show you the reaction on the command line. Please not the quotation marks wrapping the message text!

If you want to test multiple message types, e.g. Prime subscriptions, announcements, gifted subscriptions, etc., you can enter the full debug mode:
```
python main_cli.py --channel iamabot --debug-full
```
By starting Willowbot this way, it will iterate over a bunch of predefined authentic full IRC messages with certain sets of (anonymized and generic) metadata which identify them as one of the various Twitch chat message types. A list of the supported message types can be found in the appendix.


## 6 Concluding words

Willowbot has been in development for months now and is extended piece by piece whenever new scenarios to be covered arise. By no means it should be considered feature complete, but it still is and probably will be for a long time under active development, including efforts to make Willowbot more accessible.

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
* `function`
    * type: list
    * a list of callable routines and their arguments within a custom module
* `interval`
    * type: integer
    * for timed commands; in seconds
* `level`
    * type: integer
    * exact level needed to trigger the command
* `matchType`
    * type: string
    * `is` [Default], `is_caseInsensitive`, `startsWith`, `contains`, `contains_caseInsensitive`, `endsWith`, `regex`
* `maxRaidersCount`
    * type: integer
    * maximum count of raiders needed to trigger the associated message
* `maxSubLevel`
    * type: integer
    * maximum subscription count needed to trigger the associated message; can be used for chat commands as well as for subscription messages
* `minLevel`
    * type: integer
    * minimum level needed to trigger the command
* `minRaidersCount`
    * type: integer
    * minimum count of raiders needed to trigger the associated message
* `minSubLevel`
    * type: integer
    * minimum subscription count needed to trigger the associated message; can be used for chat commands as well as for subscription messages
* `needsVIP`
    * type: boolean
    * restrict the command to be used by VIP users only
* `os-command`
    * type: string
    * a system command that will be executed if the other conditions are met (level, cooldown, pattern, etc.)
* `senderName`
    * type: list
    * only execute the command if the list contains the login name of the user who has sent the triggering message
* `senderDisplayName`
    * type: list
    * only execute the command if the list contains the display name of the user who has sent the triggering message
* `subLevel`
    * type: integer
    * subscription count needed to trigger the associated message; can be used for chat commands as well as for subscription messages
* `triggerType`
    * type: string
    * `raid`, `sub`, `subGiftAnon`, `subGiftContinued`, `subGiftMulti`, `subGiftSingle`, `subGiftSingleFollowup`, `subPrime`


### List of placeholder variables

Variables for bot answers, which are resolved before Willowbot sends its message:

* `arg0`, `arg1`, `arg2`, etc.<br>the arguments passed to the command
* `arg0+`, `arg1+`, `arg2+`, etc.<br>concatenate all arguments from the *n*th one onward, separated by blank spaces
* `msgID`<br>ID of the processed message; needed for deleting specific messages
* `msgMeta` <br>the metadata of the processed message (mainly intended to be used for passing those data to an optional module)
* `msgText` <br>the full text of the processed message (mainly intended to be used for passing the message as a whole to an optional module)
* `raidersChannelID`<br>the ID of the channel the raiders are coming from
* `raidersChannelName`<br>the channel which the raiders are coming from
* `raidersCount`<br>quantity of raiders joining the channel
* `senderDisplayName`<br>processed message sender’s display name
* `senderID`<br>processed message sender’s ID number
* `senderName`<br>processed message sender’s login name
* `subGiftCount`<br>amount of subscriptions gifted in one gift action
* `subGiftCountTotal`<br>total amount of subscriptions a user has already gifted
* `subGiftGifter`<br>gifting user’s display name
* `subGiftRecipient`<br>gift-receiving user’s display name
* `subMonth`<br>number of months the user has already subscribed for
* `subName`<br>subscribing user’s display name


### List of debug message patterns

(If you see the necessity for more message patterns to check, please feel free to suggest.)

Currently, the following message types are included in Willowbot’s debugging/testing mode:

* Action (/me)
* Announcement
* Ban
* Deleted message
* Message, moderator
* Message, ordinary user
* Message, ordinary user, first post ever
* Message, subscriber
* Message, VIP user
* Raid (999 raiders)
* Subscription, Prime
* Subscription, resub, 99 months
* Subscription gift, anonymous
* Subscription gift, multi, 10 gifts, 50 gifts total
* Subscription gift, single, follow-up message for multi-subgift
* Subscription gift, single, tier 1, 50 gifts total, month 35 for recipient
* Whisper


### List of command line options

* `-c`, `--channel {channel name}`<br>Make Willowbot connect to the channel `{channel name}`.
* `-cf`, `--configure`<br>Generate a config and a logins file.
* `-df`, `--debug-full`<br>Willowbot will react to a series of predefined message patterns, using the commands set of the channel specified via the `--channel` option. If the `--channel` option is omitted, the commands of the channel set as `botname` in the config file will be used.
* `-ds`, `--debug-single '{message}'`<br>Willowbot will treat `{message}` like an ordinary chat message and react to it. Note the single quotation marks around the message.
* `-gc`, `--get-config [key]`<br>Show all keys of the Willowbot config file and their values. If you provide a distinct key `[key]` as an additional argument, only that key and its value will be shown.
* `-h`, `--help`<br>Shows an overview of how to use Willowbot and its options, similar to this section of the README.
* `-l`, `--login {account name}`<br>Make Willowbot use the account `{account name}` instead of the one stated as `botname` in the config file.
* `-lg`, `--language {locale abbreviation}`<br>Start Willowbot with the language that has the code `{locale abbreviation}` instead of with OS default language (provided it is supported). Currently supported language abbreviations can be checked in Willowbot’s `lang` directory or via Willowbot’s `--help` option.
* `-sc`, `--set-config {key} {value}`<br>Set the value of an existing key `{key}` of Willowbot’s config file to `{value}`.
* `-t`, `--token {keyword}`<br>Perform a token operation. One of the following keywords is needed:
    * `add {name} {token}`<br>Add the token `{token}` for the account `{name}` to the logins file.
    * `delete {name}`<br>Remove `{name}` and the token associated with it from the logins file.
    * `get`<br>Generate a token via Twitch.
    * `list`<br>List all tokens residing in the logins file.
    * `revoke {name}`<br>Revoke the token listed in the logins file and associated with the passed `{name}`. This operation will also delete the token from the logins file.
