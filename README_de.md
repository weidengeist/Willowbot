# Willowbot

— [Switch to English version](https://github.com/weidengeist/Willowbot/blob/main/README.md)

## Inhalt

* [Einleitung](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#einleitung)
* [1 Installation](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#1-installation)
* [2 Ersteinrichtung](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#2-ersteinrichtung)
* [3 Kommandosets erstellen](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#3-kommandosets-erstellen)
    * [3.1 Nutzerausgelöste Kommandos](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#31-nutzerausgel%C3%B6ste-kommandos)
        * [3.1.1 Einfaches Abgleichen](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#311-einfaches-abgleichen)
        * [3.1.2 Erweitertes Abgleichen: Reguläre Ausdrücke](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#312-erweitertes-abgleichen-regul%C3%A4re-ausdr%C3%BCcke)
    * [3.2 Aliasse](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#32-aliasse)
    * [3.3 Zeitabhängige Kommandos](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#33-zeitabh%C3%A4ngige-kommandos)
    * [3.4 Abklingzeiten](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#34-abklingzeiten)
    * [3.5 Levelsystem](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#35-levelsystem)
        * [3.5.1 Basissystem](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#351-basissystem)
        * [3.5.2 Weitere Restriktionen](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#352-weitere-restriktionen)
    * [3.6 Platzhaltervariable](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#36-platzhaltervariable)
    * [3.7 Auslösertypen: Raids und Abonnements (Subs)](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#37-ausl%C3%B6sertypen-raids-und-abonnements-subs)
        * [3.7.1 Raids](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#371-raids)
        * [3.7.2 Abonnements (Subs)](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#372-abonnements-subs)
    * [3.8 Antworttypen: sequentiell vs. zufällig](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#38-antworttypen-sequentiell-vs-zuf%C3%A4llig)
    * [3.9 Betriebssystemkommandos](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#39-betriebssystemkommandos)
    * [3.10 Nachrichten zur Fehlersuche (Debugging)](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#310-nachrichten-zur-fehlersuche-debugging)
* [4 Optionale/Eigene Module](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#4-optionaleeigene-module)
    * [4.1 Auf eigene Module zugreifen: der `function`-Schlüssel](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#41-auf-eigene-module-zugreifen-der-function-schl%C3%BCssel)
    * [4.2 `poll`-Modul (Abstimmungen)](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#42-poll-modul-abstimmungen)
    * [4.3 `modChannelInfo`-Modul (Kanalinformationen bearbeiten)](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#43-modchannelinfo-modul-kanalinformationen-bearbeiten)
    * [4.4 `dateDiff`-Modul (Datumsdifferenzen ausgeben)](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#44-dateDiff-modul-datumsdifferenzen-ausgeben)
* [5 Test-/Fehlerbehandlungsmodus](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#5-test-fehlerbehandlungsmodus)
* [6 Abschließende Worte](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#6-abschlie%C3%9Fende-worte)
* [Anhang](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#anhang)
    * [Implementierte Schlüsselprüfungen](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#implementierte-schl%C3%BCsselpr%C3%BCfungen)
    * [Liste der Platzhaltervariablen](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#liste-der-platzhaltervariablen)
    * [Liste der Fehlerbehandlungsnachrichtenmuster](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#liste-der-fehlerbehandlungsnachrichtenmuster)
    * [Liste der Kommandozeilenoptionen](https://github.com/weidengeist/Willowbot/blob/main/README_de.md#liste-der-kommandozeilenoptionen)


## Einleitung

Dies ist ein Chatbot, der für die Verwendung auf Twitch bestimmt ist. Er erlaubt die Konfiguration eigener Kommandos, optional auf Regulären Ausdrücken basierend, auf die der Bot reagieren soll – entweder durch eine Antwort im Chat oder das Ausführen eines Betriebssystembefehls. Ebenfalls werden zeitabhängige Kommandos unterstützt und ein Levelsystem zur Verfügung gestellt, womit sich die Benutzung von Kommandos auf unterschiedliche Nutzergruppen beschränken lässt.

Die Anweisungen und Beschreibungen im Folgenden wurden speziell für Nichtprogrammierer verfasst, um Willowbot zugänglicher zu gestalten. Rückmeldungen für weitere Verbesserungen in dieser Hinsicht sind stets willkommen.


## 1 Installation

Um Willowbot benutzen zu können, muss [Python in wenigstens Version 3.9](https://www.python.org/downloads/) installiert sein (die neueste Version wird empfohlen). Die für Windowsnutzer empfohlene Variante ist der Windows-Installer (64 Bit), da er den Großteil der Konfiguration ohne zu überwindende Schwierigkeiten selbständig vornehmen wird. Nachdem Python erfolgreich installiert wurde, laden Sie das Willowbotpaket herunter und entpacken Sie das Archiv in einem Verzeichnis Ihrer Wahl.


## 2 Ersteinrichtung

Öffnen Sie eine Konsole (unter Windows: starten Sie `cmd`; unter Linux/Mac: drücken Sie Strg+Alt+T (unter den meisten Desktopumgebungen) oder suchen Sie nach `Terminal` in Ihrem Anwendungsmenü). Navigieren Sie in das Verzeichnis, wo sich Willowbot befindet, indem Sie `cd` eintippen, gefolgt von einem Leerzeichen und dem Willowbotverzeichnis, z. B.
```
cd C:\Programme\Willowbot
```
unter Windows oder
```
cd /home/dasbinich/Willowbot
```
unter Linux/Mac. Erstellen Sie nun die Grundkonfigurationsdateien, indem Sie
```
python main_cli.py --configure
```
eintippen und die Entertaste drücken. Je nach Ihrer Pythoninstallation ist es möglich, dass Sie `py` oder `python3` statt `python` zum Aufrufen nutzen müssen.

Sofern alles korrekt installiert ist, sollte Ihnen Willowbot nun mitteilen, dass und wo er eine Konfigurations- sowie eine Logindatei für Sie angelegt hat. Die Standardverzeichnisse für diese Dateien (`config.py` und `logins.py`) sind die folgenden:

* Windows: `%appdata%\twitch\willowbot\`
* MacOS: `/home/[user]/Library/Preferences/twitch/willowbot/`
* Linux: `/home/[user]/.config/twitch/willowbot/`

**Achtung!** Das soeben beschriebene Vorgehen wurde nur unter Linux getestet. Falls irgendwelche der Informationen über die unter Windows benötigten Schritte inkorrekt sein oder nicht funktionieren sollten, lassen Sie es mich bitte wissen.

Erzeugen Sie nun einen Zugangsschlüssel für Willowbot. Doch bevor Sie fortfahren, stellen Sie sicher, dass in Ihrem Browser keine aktive Twitchsitzung gespeichert ist, also loggen Sie sich aus oder löschen Sie gleich das entsprechende Sitzungscookie Anschließend sind Sie bereit, einen Zugangsschlüssel zu generieren, indem Sie Willowbot mit der `--token`-Option, gefolgt vom Schlüsselwort `get`, starten:
```
python main_cli.py --token get
```
Ihr Standardbrowser sollte sich nun öffnen und Ihnen Twitchs Autorisierungsseite für Zugangsschlüssel präsentieren. Loggen Sie sich mit dem Konto Ihres Bots ein und wählen Sie »Authorize«. Sie werden anschließend auf eine Seite weitergeleitet, die Ihnen erklärt, wie Sie den soeben erzeugten Zugangsschlüssel Ihrer Logindatei hinzufügen. Folgen Sie diesen Anweisungen.

Nachdem Sie den Schlüssel hinzugefügt haben, stellen Sie Willowbots Standardloginnamen auf denjenigen ein, für den Sie gerade einen Zugangsschlüssel erzeugt haben:
```
python main_cli.py --set-config botname ichbineinbot
```
`ichbineinbot` ist hier nur ein Platzhalter; es muss der eigentliche Name des Botkontos angegeben werden.

Nun können Sie Willowbot starten, indem Sie
```
python main_cli.py 
```
eintippen, und er wird sich mit dem Kanal verbinden, den Sie als `botname` festgelegt haben. In der Praxis werden Sie Willowbot natürlich auf Ihrem Streamerkanal oder – falls Sie Moderator sind – auf einem anderen Kanal, wo Sie Moderatorenrechte besitzen, laufen lassen wollen. Dafür starten Sie Willowbot mit der `--channel`-Option, gefolgt vom Namen des Kanals, dem Willowbot beitreten soll:
```
python main_cli.py --channel meineigenerkanal
```
Natürlich müssen Sie `meineigenerkanal` durch den Namen des passenden Kanals, auf dem Willowbot seinen Dienst antreten und die von Ihnen definierten Befehle ausführen soll, ersetzen.


### Kyrillisch-Latein-Konvertierung

Willowbot enthält eine Option, kyrillische Buchstaben, die wie lateinische aussehen, tatsächlich in ihr lateinisches Pendant zu konvertieren. Diese Funktion wurde wegen Scambots, die versuchen, Maßnahmen gegen Bots dadurch zu unterlaufen, indem sie lateinische Buchstaben mit kyrillischen kombinieren und damit Mustererkennungen entgehen, eingerichtet. Der Standardwert für diese Option ist `False` (falsch), aber wenn Sie den Bot in einem hauptsächlich lateinischen Kontext respektive in einer entsprechenden Community verwenden und diese Funktion einsetzen wollen, können Sie diese mit folgendem Befehl aktivieren:
```
python main_cli.py --set-config 'cyrillicToLatinConversion' True
```


### Migrationshinweise (Erstnutzer können diesen Part überspringen)

Sollten Sie Willowbot zuvor schon einmal verwendet haben (vor März 2023), müssen Sie ggf. ein paar Ihrer Kommandos anpassen, um sicherzustellen, dass sie mit der neuen Twitch-API weiterhin funktionieren. Die Chatkommandos `/ban` sowie `/timeout` können weiterhin verwendet werden; sie werden auf die entsprechenden API-Endpunkte umgeleitet. Jedoch werden sie nicht mehr mit dem Argument `$senderName`, sondern mit `$senderID` aufgerufen.

Des Weiteren unterstützt Willowbot nun API-Shoutouts und -Ankündigungen. Um sie zu nutzen, verwenden Sie einfach die bekannten Kommandos `/shoutout` oder `/announce` in den `answer`-Schlüsseln ihrer Kommandodefinitionen.


#### Update Juni 2024

Um die Kyrillisch-Latein-Konvertierung nutzen zu können, muss der Schlüssel `cyrillicToLatinConversion` mit dem Wert `True` (Achtung! Als Wahrheitswert, nicht als Zeichenkette, d. h. ohne Anführungszeichen.) von Hand in die Konfigurationsdatei geschrieben werden.


## 3 Kommandosets erstellen

Neben einem Verzeichnis für die allgemeine Willowbot-/IRC-Konfiguration wird dieses Programm ein Unterverzeichnis namens `commands` in diesem Konfigurationsverzeichnis anlegen. Sie können Kommandosets für mehrere Kanäle anlegen; jedes Set ist eine gesonderte Datei, die nach dem Kanal benannt ist, auf dem sie benutzt werden soll. (Das ist besonders nützlich, wenn Sie Moderator auf mehr als einem Kanal sind.) Ab jetzt nehmen wir, dass Ihr Bot IchBinEinBot heißt, d. h. den Twitchlogin ichbineinbot verwendet. Um Ihre Kommandos zu testen, ist es strengstens empfohlen, den Kanal des Bots zu verwenden, also lassen Sie uns jetzt für diesen ein Kommandoset anlegen.

Die Kommandosets selbst sind kleine Skripte, die in der Programmiersprache Python geschrieben sind und nichts weiter tun, als der Variablen `commands` ein sogenanntes Wörterbuch ([dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)) zuzuordnen, worin all Ihre Kommandoinformationen gespeichert sind. Erstellen Sie eine Datei namens `ichbineinbot.py` (da dies der Kanal ist, wo wir einige Tests durchführen wollen; beachten Sie: nur Kleinbuchstaben verwenden!), worin Sie Ihre Kommandoprüfungen und Botreaktionen ablegen können.

Im Willowbotarchiv ist eine Datei `commandsTemplate.py` enthalten, worin die meisten der Beispielkommandos aus den nachfolgenden Abschnitten gesammelt sind. Allerdings ist Weiterlesen statt simples Kopieren und Einfügen aus der Vorlagedatei *strengstens empfohlen*, da Sie sicherlich auf Schwierigkeiten stoßen werden, wenn Sie anders verfahren.


### 3.1 Nutzerausgelöste Kommandos

Zu Beginn legen Sie das Gerüst für Ihre Kommandos in Ihrer `ichbineinbot.py`-Datei an:
```
commands = {
  
}
```
Vielleicht möchten Sie ein `!bsg`-Kommando, um Ihren Zuschauern mitzuteilen, wie es um Ihre Backseatgamingregelungen bestellt ist, also sagen wir unserem Bot das auslösende Kommando und was er antworten soll:
```
commands = {
  "!bsg" : {
    "answer" : "Bitte erzählt dem Streamer nicht, wie er spielen soll."
  }
}
```
`answer` wird in unserem Wörterbuch (dictionary) Schlüssel/Schlüsselwort (key) genannt; die eigentliche Antwort bezeichnet man als Wert (value). Wir werden diese Begriffe in den vor uns liegenden Beschreibungen öfter verwenden.

Der Wert unseres `answer`-Schlüssels funktioniert genau wie ein gewöhnliches [Twitchchatkommando](https://help.twitch.tv/s/article/chat-commands), d. h. Sie können der Antwort `/me` oder `/announce` voranstellen, um sie hervorzuheben, wenn Sie mögen.


#### 3.1.1 Einfaches Abgleichen

Manchmal möchten Sie vielleicht eine bestimmte Person im Chat ansprechen, wenn Sie Ihr `!bsg`-Kommando verwenden, allerdings würde der Bot auf die Art, wie es oben gezeigt wird, nichts tun, weil er prüft, ob die gesamte Nachricht aus »!bsg« besteht, nicht, ob sie »!bsg« enthält. Das ist das Standardverhalten. Um einen bestimmten Teil der Nachricht zu prüfen, müssen Sie einen `matchType` (Abgleichtyp) definieren. In diesem Fall ist `startsWith` (beginnt mit) der passende.
```
commands = {
  "!bsg" : {
    "answer"    : "Bitte erzählt dem Streamer nicht, wie er spielen soll.",
    "matchType" : "startsWith"
  }
}
```
Jetzt kann die Antwort des Bots z. B. durch `!bsg @randomtwitchuser` ausgelöst werden. Beachten Sie das Komma am Ende der Zeile mit `answer`! Die Reihenfolge der Schlüsseldefinitionen spielt keine Rolle; `matchType` kann ebensogut vor `answer` festgelegt werden.

Die anderen verfügbaren `matchType`-Optionen, die Willowbot zur Verfügung stellt, sind `is` (ist genau; Standardwert; muss nicht explizit gesetzt werden), `is_caseInsensitive` (wie `is`, aber ohne Berücksichtigung von Groß- und Kleinschreibung), `contains` (enthält), `endsWith` (endet mit), `regex` (mehr dazu später) und `contains_caseInsensitive` (wie `contains`, aber ohne Berücksichtigung von Groß- und Kleinschreibung). Die letzte besteht hauptsächlich aufgrund von Bequemlichkeitserwägungen für den Endnutzer, allerdings sei nahegelegt, stattdessen Reguläre Ausdrücke (regular expressions, Option `regex`) zu verwenden.


#### 3.1.2 Erweitertes Abgleichen: Reguläre Ausdrücke

Die meisten Einsatzzwecke sollten durch die einfachen Abgleichfunktionen abgedeckt sein. Haben Sie jedoch das Gefühl, mehr Kontrolle über die Nachrichten, auf die Willowbot in bestimmter Weise reagieren soll, haben zu wollen, können Reguläre Ausdrücke ausgewertet werden.

Reguläre Ausdrücke sind ein sehr mächtiges Werkzeug und mögen deswegen zunächst ein wenig einschüchternd wirken, aber keine Sorge. Ihnen wird anhand sehr einfacher erster Beispiele gezeigt, wie Sie sie nutzen, und diese werden wahrscheinlich völlig ausreichen, um Ihnen alles beizubringen, was Sie benötigen, um Willowbot effizient benutzen zu können.

Beispielsweise möchten Sie gern ein `!multi`-Kommando, um Ihren Zuschauern mitzuteilen, mit wem Sie aktuell spielen. Wenn Sie wollen, dass diese Nachricht auch angezeigt wird, wenn `!Multi` gesendet wird, könnten Sie natürlich einfach den gesamten `!multi`-Kommandoblock noch einmal eingeben und `m` durch `M` ersetzen. Eleganter geht es stattdessen mit einem Regulären Ausdruck:
```
commands = {
  "^![Mm]ulti" : {
    "answer"    : "Heute spielen wir mit jemand ganz Besonderem.",
    "matchType" : "regex"
  }
}
```
Das Symbol `^` bedeutet, dass die Nachricht mit dem Muster startet, das ihm folgt, also kann `^` mit Abgleichstyp `regex` die Verwendung von `startsWith` ersetzen. Das sogenannte Zeichenset (character set) `[Mm]` bedeutet genau das, was wir erreichen wollen: Jedwedes dieser beiden Zeichen darf das Kommando beginnen. 

Was passiert nun aber, wenn es bspw. sowohl ein Kommando `!multi` als auch `!multiplayer` gibt? Die obige Kommandodefinition würde bei der Eingabe von `!multi` in den Chat nicht nur diesen, sondern auch das `!multiplayer`-Kommando auslösen. Daher ist es sinnvoll, Willowbot mitzuteilen, dass das Kommando genau dieser feststehende Begriff ist und auch nicht beliebig zu einem anderen Wort verlängert werden darf. Dies wird durch `( |$)` bewerkstelligt:
```
commands = {
  "^![Mm]ulti( |$)" : {
    "answer"    : "Heute spielen wir mit jemand ganz Besonderem.",
    "matchType" : "regex"
  }
}
```
Diese Konstruktion bedeutet: Reagiere auf Chateingaben, die mit `!multi` oder `!Multi` beginnen und danach entweder ein Leerzeichen aufweisen (falls der Nutzer bspw. noch ein `@andererNutzer` als Ping hinzufügen möchte) oder aber damit vollständig und beendet sind (`$`).

Willowbots Regexfunktion unterstützt auch die Verwendung sogenannter Treffergruppen (capture groups) in seinen Antworten. Das bedeutet, dass Sie einzelne Teile der Nachricht, den den Bot zu einer Reaktion veranlasst hat, herausnehmen und für Ihre Antwort verwenden können.

Einige häufig benutze Bots auf Twitch, die nicht so flexibel wie Willowbot sind, löschen automatisch Links, die von Nichtabonnenten in den Chat geschrieben wurden, selbst wenn es sich um einen Link zu einem Clip handelt, der auf Twitch selbst erstellt wurde. Um dieses Verhalten zu korrigieren, kann Willowbot beigebracht werden, die URL, die zum Clip führt, der Nachricht zu entnehmen und sie noch einmal mit Moderatorrechten zu senden:
```
'.*(https://clips.twitch.tv/[^ ]+).*' : {
  'matchType' : 'regex',
  'answer'    : 'Danke für deinen Clip, $senderDisplayName. Leider löscht der Bot alle Links von Nonsubs. Hier dein Repost: \1',
  'level'     : 1
},
```
Das Muster, das hier benutzt wird, veranlasst Willowbot, auf URLs, die zu Twitchclips führen, zu reagieren. Aber es gibt etwas Besonderes in diesem Muster: die Klammern. Diese weisen den Bot an, den Ausdruck darin zu »speichern«. Sie können auf diese gespeicherten Teile zugreifen, indem Sie `\1`, `\2`, `\3` etc. in Ihrer Antwort verwenden, um die Inhalte des 1., 2., 3. etc. Klammernpaars aufzurufen.


### 3.2 Aliasse

Da wir nun reguläre Ausdrücke kennen, können wir für unsere Kommandos Aliasse definieren, d. h. mehrere Kommandoauslöser für ein und dieselbe Reaktion. Ein simples Beispiel sollte ausreichend sein, um zu zeigen, wie das funktioniert:
```
commands = {
  "^!([Mm]ods?|[Ss]kyrim|[Gg]ame)" : {
    "answer"    : "Wir spielen aktuell »Enderal: Forgotten Stories«, eine Total-Conversion-Mod für »The Elder Scrolls V: Skyrim«.",
    "matchType" : "regex"
  }
}
```
Da dieses Kommando mehrere verschiedene Regexstrukturen enthält, lassen Sie uns diese ein wenig detaillierter betrachten. Zunächst einmal können Sie sehen, dass wir hier eine Kette von Wörtern haben, die in runden Klammern eingeschlossen und durch senkrechte Striche voneinander getrennt sind (`(a|b|c)`). Dies bedeutet, dass die definierte Antwort durch jedes dieser Worte ausgelöst werden kann.

Einen Abschnitt zuvor haben Sie Zeichensets kennengelernt, und ebendiese Sets können Sie im hier definierten Kommando erneut sehen. Sie können die Antwort also entweder durch `!mod`, `!Mod`, `!skyrim`, `!Skyrim`, `!game` oder `!Game` auslösen.

»Aber Moment! Da ist ein Fragezeichen hinter `![Mm]ods`!«, mögen Sie jetzt einwerfen. »Und wieso heißt es jetzt `!mods` und nicht mehr `!mod`?« Das Fragezeichen ist ein spezielles Zeichen im Kontext regulärer Ausdrücke. Es bedeutet, dass das Zeichen vor ihm optional ist, d. h. Sie können die Antwort nicht nur über `!mod` or `!Mod`, sondern auch durch `!mods` und `!Mods` auslösen.


### 3.3 Zeitabhängige Kommandos

Natürlich unterstützt Willowbot auch zeitabhängige Kommandos, d. h. das automatische Versenden von Nachrichten nach Ablauf einer festgelegten Zeitspanne. In diesem Fall ist es nicht nötig, einen Befehl zu definieren, der diese Nachricht auslösen soll, und Sie können den Befehl nach Belieben benennen. Willowbot unterscheidet intern zwischen nutzerausgelösten und zeitabhängigen Kommandos, weshalb es nicht möglich ist, ein Kommando für beide Zwecke zu verwenden, also ein zeitabhängiges Kommando manuell auszulösen.

Um ein zeitabhängiges Kommando zu definieren, benötigt Willowbot das Schlüsselwort `interval`:
```
commands = {
  "drink" : {
    "answer"   : "Bitte trinkt regelmäßig!",
    "interval" : 1800
  }
}
```
Diese Definition wird aller 30 Minuten (1800 Sekunden) eine Nachricht erzeugen, die den Streamer und die Zuschauer daran erinnert, sich ein Getränk zu holen. Wenn Sie wollen, dass auch Ihre Zuschauer eine solche Nachricht auslösen können, fügen Sie Ihrem Kommandoset ein Kommando hinzu, das wie im vorherigen Abschnitt beschrieben aussieht. In seiner Gesamtheit würde dieses dann so aussehen:
```
commands = {
  "drink" : {
    "answer"   : "Bitte trinkt regelmäßig!",
    "interval" : 1800
  },
  "!drink" : {
    "answer"    : "Bitte trinkt regelmäßig!",
    "matchType" : "startsWith"
  }
}
```
Bitte beachten Sie das Komma nach `}` in Zeile 5! Die Kommandoblöcke (`{…}`) in Ihrem `commands`-Wörterbuch (-dictionary) müssen durch Kommata voneinander getrennt sein.


### 3.4 Abklingzeiten

Kommandos mit Abklingzeiten einzurichten, ist genauso simpel, wie es für zeitabhängige Kommandos ist. Es muss lediglich `interval` durch `cooldown` ersetzt werden:
```
commands = {
  "!bsg" : {
    "answer"   : "Please do not tell the streamer how to play.",
    "cooldown" : 30
  }
}
```
Der obige Code stellt Ihren Zuschauern das Kommando `!bsg` zur Verfügung und verhindert zugleich, dass der Bot erneut darauf reagieren wird, bevor 30 Sekunden vergangen sind.


### 3.5 Levelsystem

#### 3.5.1 Basissystem

Um den Zugang zu Kommandos einzuschränken, bietet Willowbot ein Levelsystem. Jedem Nutzer im Chat wird ein Level zugeordnet, basierend auf seiner Rolle und Chaterfahrung. Folgende Level sind implementiert:

* 0: der Nutzer postet das allererste Mal auf diesem Kanal;
* 1: gewöhnlicher Nutzer, der bereits zuvor auf dem Kanal war, aber kein Abonnent ist;
* 2: Abonnenten;
* 3: Moderatoren;
* 4: Streamer.

Damit Willowbot den Level des Nutzers prüft, bevor er eine Antwort sendet, müssen Sie das Schlüsselwort `level` oder `minLevel` benutzen. Ein paar Beispiele sollen das näher erläutern.

Das häufigste Szenario für die Level ist es, einen minimalen Level zu ermitteln, der zum Ausführen eines Kommandos benötigt wird. Für ein Kommando, das nur von den Kanalmoderatoren und dem Streamer genutzt werden kann, müssen Sie die `minLevel`-Option benutzen und diese auf den Wert 3 festlegen:
```
commands = {
  "!issues" : {
    "answer"   : "/announce Es gibt technische Schwierigkeiten. Bitte bleibt dran",
    "minLevel" : 3
  }
}
```

Wenn Sie Nutzern, die neu in Ihrem Chat sind, eine besondere Begrüßung zuteilwerden lassen möchten, möchten Sie sicherstellen, dass nicht alle Nutzer diese Nachricht bekommen, also beschränken Sie Willowbots Reaktion auf Level-0-Nutzer:
```
commands = {
  ".*" : {
    "answer"    : "Willkommen auf meinem Kanal! Nimm einen Keks und hab Spaß.",
    "matchType" : "regex",
    "level"     : 0
  }
}
```
Neben einer Leveldefinition benutzt dieses Kommando den Regulären Ausdruck `.*`, wodurch auf Nachrichten mit *jedem* beliebige Zeichen (`.`) reagiert wird, das 0mal oder öfter (`*`) vorkommt. Wir werden uns diese Asteriskenmuster und wie man sie effizient verwendet im folgenden Abschnitt 3.6 genauer anschauen.


#### 3.5.2 Weitere Restriktionen

Zusätzlich zu den genannten Leveln kann ein Kommando auf die ausschließliche Nutzung durch VIP-Chatteilnehmer beschränkt werden, indem der Schlüssel `needsVIP` übergeben und mit dem Wahrheitswert `True` versehen wird.
```
commands = {
  "^!vip( |$)" : {
    "answer"    : "Ich bin VIP und deswegen darf nur ich dieses Kommando nutzen.",
    "matchType" : "regex",
    "needsVIP"  : True
  }
}
```
Hier zu beachten: Wahrheitswerte (`True` und `False`) besitzen anders als Zeichenketten keine Anführungszeichen.

Möchten Sie neben den durch Twitch vergebenen Rollen ihr eigenes, auf Abonnementmonaten basierendes Levelsystem aufbauen, stehen Ihnen dafür die Schlüssel `minSubLevel`, `subLevel` sowie `maxSubLevel` zur Verfügung. Sie können also festlegen, dass eine minimale Anzahl von Abomonaten notwendig ist, um bestimmte Kommandos benutzen zu dürfen (`minLevel`), die Nutzung auf ein Intervall an Abomonaten beschränken (`minSubLevel` und `maxSubLevel`) oder nur einen bestimmten Monat für ein Kommando vorsehen (`subLevel`). Die Werte für diese Schlüssel werden jeweils als Ganzzahl (integer) angegeben und besitzen daher, wie Wahrheitswerte, keine Anführungszeichen in der Kommandodefinition.


### 3.6 Platzhaltervariable

Einige Nachrichten erfordern unter Umständen Personalisierung. Für solche Fälle bietet Willowbot diverse Variable, die ausgewertet werden, bevor die eigentliche Nachricht gesendet wird.

Um die Nutzung von Platzhaltervariablen zu illustrieren, lassen Sie uns ein Shoutoutkommando definieren:
```
commands = {
  "!so" : {
    "answer"    : "Für gute Unterhaltung besucht $arg0s Kanal: https://twitch.tv/$arg0.",
    "matchType" : "startsWith"
  }
}
```
Die obige Kommandodefinition verwendet (angezeigt durch `$`) die Platzhaltervariable `arg0`, was bedeutet, dass Willowbot `$arg0` in der Antwort durch das erste Wort nach `!so` ersetzt. `!so TollerStreamer` würde dann zu `Für gute Unterhaltung besucht TollerStreamers Kanal: https://twitch.tv/TollerStreamer.` aufgelöst werden.

Sie dürfen so viele Argumente in Ihrer Antwort verwenden, wie Sie mögen, indem Sie sie einfach in ihrer Antwort durchnumerieren. Beachten Sie jedoch, dass die Zählung bei 0, in Worten: Null, nicht bei 1 beginnt. Hier ein weiteres Beispiel:
```
commands = {
  "!give" : {
    "answer"    : "$arg0 bekommt $arg1, um sich flauschig zu fühlen.",
    "matchType" : "startsWith"
  }
}
```
Die Antwort benutzt zwei Argumente (`arg0` und `arg1`). Dies bedeutet, dass die ersten beiden Worte nach `!give` in die Antwort gesetzt werden, bevor sie an den Chat gesendet wird. `!give McFluffy Kekse` würde die Chatnachricht `McFluffy bekommt Kekse, um sich flauschig zu fühlen.` erzeugen.

Argumente, die einem Kommando übergeben werden, lassen sich auch sammeln, indem man `+` an eine numerierte `arg`-Variable anhängt. Wir benutzen das obige Beispiel und modifizieren es ein winziges bisschen, nämlich indem wir einfach `$arg1` durch `$arg1+` ersetzen:
```
commands = {
  "!give" : {
    "answer"    : "$arg0 bekommt $arg1+, um sich flauschig zu fühlen.",
    "matchType" : "startsWith"
  }
}
```
»Warum sollten wir das tun?«, fragen Sie nun vielleicht. `$arg1+` fängt nicht nur das zweite Wort nach `!give` ab, wie `$arg1` es tun würde, sondern sammelt alle Worte ab inklusive dem zweiten ein. Im Gegensatz zur vorher gezeigten Version wird unser `!give`-Kommando nun also mehr als nur zwei Argumente abfangen. In unserer ersten `!give`-Version konnten wir McFluffy »Kekse, um sich flauschig zu fühlen«, geben. Mit dem neuen Kommando können wir mittels `!give McFluffy frisch gebackene Kekse` geben, um sich flauschig zu fühlen. Lediglich Kekse sind natürlich dennoch nach wie vor möglich.

Möchten Sie etwas Liebe in Ihrem Chat verbreiten? Ermöglichen Sie Ihren Zuschauern, sich gegenseitig virtuell zu umarmen, indem Sie ein Kommando für diese Aktion definieren:
```
commands = {
  "!hug" : {
    "answer"    : "$senderDisplayName umarmt $arg0.",
    "matchType" : "startsWith"
  }
}
```
Dieses Kommando führt eine neue Platzhaltervariable ein: `senderDisplayName`. Auf Twitch besitzt jeder Nutzer einen Login- sowie einen Anzeigenamen. Diese sind beinahe identisch; der einzige Unterschied ist, dass der Loginname ausschließlich Kleinbuchstaben verwendet, wohingegen der Anzeigename auch Großbuchstaben enthalten darf. Indem wir `$senderDisplayName` in unsere Antwort integrieren, könnten wir den Namen des Nutzers, der das Kommando ausgelöst hat, benutzen. Wenn also der Nutzer McFluffy das Kommando `!hug Kittycat` sendet, würde obige Definition in der Nachricht `McFluffy umarmt Kittycat.` resultieren. (Randbemerkung: Wenn Sie `$senderName` statt `$senderDisplayName` verwenden, würde die Nachricht `mcfluffy umarmt Kittycat.` lauten.)

Ein weiterer nützlicher Zweck für Platzhalter ist das Timeouten und Bannen von Scambots, die den Chat betreten. Falls ein solcher Bot dafür bekannt ist, die Nachricht »Buy followers, subs, and viewers: [URL]« zu verwenden, können Sie den Bot einfach von Ihrem Kanal verbannen, sobald diese Nachricht im Chat auftaucht:
```
commands = {
  "Buy followers" : {
    "answer"    : "/ban $senderID",
    "matchType" : "startsWith",
    "level"     : 0
  }
}
```
Der wichtigste Aspekt dieses Kommandos ist `"level" : 0`! Sie wollen sicherlich nicht seriöse Nutzer, die »Buy followers« in anderem Kontext verwenden, verbannen.

Natürlich kann obiges Kommando durch die Verwendung von Regulären Ausdrücken verbessert werden:
```
commands = {
  "^Buy.*followers" : {
    "answer"    : "/ban $senderID",
    "matchType" : "regex",
    "level"     : 0
  }
}
```
Eine kurze Erklärung für die Regex, die hier verwendet wird: Ein Nutzer wird gebannt, wenn seine allererste Nachricht im Chat mit »Buy« beginnt (`^`; vgl. `^[Mm]ulti` in Abschnitt 3.1.2), von beliebigen Zeichen (`.`) in einer Häufigkeit von 0 oder mehr (`*`) und dem Wort »followers«. Indem Sie `.*` vor `followers` setzen, können Sie eine Scambotnachricht selbst dann abfangen, wenn er die Reihenfolge der Worte variiert (»Buy followers, subs, and viewers«, »Buy subs, followers, and viewers«, etc.).

Ein weiteres raffiniertes Beispiel, um Scambots zu bannen:
```
commands = {
  "^(Wanna|Want to) become famou?s" : {
    "answer"    : "/ban $senderID",
    "matchType" : "regex",
    "level"     : 0
  }
}
```
Egal, ob der Nutzer, der versucht, Sie zu betrügen, seine Nachricht mit »Want to« oder »Wanna« beginnt (`^`) oder ob er »famous« mit oder ohne »u« schreibt: Er wird mit der obigen Kommandodefinition sofort Ihres Kanals verbannt.

Willowbots Fähigkeiten erlauben Ihnen ebenfalls, Ihre eigene Liste verbotener Wörter/Wendungen zu definieren und Nachrichten, die sie verwenden, sofort zu löschen:
```
commands = {
  ".*(Kappa|failFish|LUL)" : {
    "answer"    : "/delete $msgID",
    "matchType" : "regex"
  }
}
```
Obige Kommandodefinition löscht alle Nachrichten, die die Worte/Emotes »Kappa«, »failFish« oder »LUL« enthalten. Für diese Aktion brauchen wir die ID der Nachricht, die Sie löschen möchten. Diese ID steckt hinter der Platzhaltervariablen `msgID`. Der Vorteil, diese Methode zu verwenden anstelle der Twitchblacklist: Sie und Ihre Moderatoren werden die Nachricht und ihren problematischen Inhalt sehen können und, falls erforderlich, weitere Schritte unternehmen, sofern es sich um schwere Fälle von Diskriminierung oder Belästigung handelt, wohingegen Nachrichten mit Twitchblacklistbegriffen nur unterdrückt werden würden, bevor ein Moderator sie sehen und ggf. den Nutzer an Twitch melden kann. Im Abschnitt über Antworttypen werden wir sehen, wie wir dieses Kommando erweitern und so sogar noch nützlicher gestalten können.


### 3.7 Auslösertypen: Raids und Abonnements (Subs)

Die auf Twitch versandten Chatnachrichten enthalten alle spezielle Metadaten und können so u. a. zwischen Nutzernachricht, Abonnement/Sub und Raid unterschieden werden. Im Gegensatz zu Nutzernachrichtenkommandos, die Sie definieren, indem Sie ein Wort oder ein Muster festlegen, dem die Nachricht entsprechen muss, können Raid- und Abonnement-/Subnachrichten einen beliebigen Namen haben. Unter welchen Umständen eine Nachricht ausgelöst werden kann, teilen Sie Willowbot durch die Angabe eines `triggerType`-Schlüssels (Auslösetyp) mit.

Willowbots Standardverhalten ist es, Nachrichten, die im Chat erscheinen, als Nutzernachrichten aufzufassen. Für den gewöhnlichen Nutzer unsichtbar, werden im Hintergrund spezielle Nachrichten gesendet. Diese enthalten u. a. Informationen über Raids und Abonnements. Wenn Sie wollen, dass Willowbot diese verarbeitet, müssen Sie den passenden `triggerType`-Wert in Ihrer Kommandodefinition festlegen.


#### 3.7.1 Raids

Beginnen wir, indem wir ein Kommando definieren, das Raids verarbeitet:
```
commands = {
  "meineRaids" : {
    "answer"      : "$raidersChannelName besucht uns mit $raidersCount Raidern. Habt Spaß!",
    "triggerType" : "raid"
  }
}
```
Es ist wichtig, in dieser Definition als `triggerType` `raid` einzutragen. Andernfalls würde Willowbot den festgelegten Antwortsatz in den Chat schreiben, sobald jemandes Nachricht im Chat "meineRaids" entspricht.

Wie weiter oben bereits erwähnt wurde, ist es nicht erforderlich, für diese Art der Nachrichten ein bestimmtes Signalwort oder Muster anzugeben. Allerdings *müssen* Sie einen eindeutigen Identifikator (in diesem Fall `meineRaids`) für diese Art der Nachrichtenverarbeitung festlegen. Nicht eindeutige, d. h. mehrfach vergebene Identifikatoren überschreiben die bereits angelegten Kommandos mit selbem Identifikator/Muster, so dass nur das zuletzt definierte existieren und auch verarbeitet werden können wird.

In der Antwort sehen Sie zwei weitere Platzhaltervariable: `raidersChannelName` und `raidersCount`. Sobald ein Raid festgestellt wird, werden diese Platzhalter durch den Kanal, der Ihnen seine Zuschauer schickt, respektive die Anzahl der herübergeschickten Zuschauer ersetzt.

Kommandos mit dem  `raid`-Typ unterstützen auch den `minRaidersCount`-Schlüssel. Wenn dieser Schlüssel gesetzt wurde, wird die entsprechende Reaktion nur ausgelöst, wenn der Raid aus mindestens der angegebenen Anzahl von Leuten besteht.


#### 3.7.2 Abonnements (Subs)

Abonnementverarbeitung ist ein wenig komplexer als die für Raids, da es verschiedene Arten von Abonnements gibt, für die Sie wiederum unterschiedliche Handhabungen festlegen können.

Definieren wir einen Verarbeiter für verlängerte Abonnements:
```
commands = {
  "meinResub" : {
    "answer"      : "$subName unterstützt den Kanal bereits seit $subMonth Monaten.",
    "triggerType" : "sub"
  }
}
```
Die Auslösertypen `sub`, `subPrime` und `subGiftContinued` unterstützen die Schlüssel `subLevel`, `minSubLevel` und `maxSubLevel`. Diese erlauben Ihnen, noch stärker zwischen Abonnements zu differenzieren, indem Sie besondere Nachrichten nur für eine bestimmte (minimale oder maximale) Anzahl von Abomonaten versenden.
```
commands = {
  "sehr langes Abo" : {
    "answer"      : "$subName ist schon seit mehr als einem Jahr Abonnent! Glückwunsch zu $subMonth Monaten in unserer Community.",
    "minSubLevel" : 13,
    "triggerType" : "sub"
  },
  "jeder andere Monat 9–12" : {
    "answer"      : "$subName hat gerade für Monat $subMonth abonniert.",
    "triggerType" : "sub",
    "minSubLevel" : 10,
    "maxSubLevel" : 12
  },
  "Twitchbaby" : {
    "answer"      : "Wir haben ein Twitchbaby mit $subName!",
    "subLevel"    : 9,
    "triggerType" : "sub"
  },
  "jeder andere Monat 3–8" : {
    "answer"      : "$subName hat gerade für Monat $subMonth abonniert.",
    "triggerType" : "sub",
    "minSubLevel" : 3,
    "maxSubLevel" : 8
  },
  "2nd month" : {
    "answer"      : "Vielen Dank, $subName, dass du bei uns bleibst.",
    "subLevel"    : 2,
    "triggerType" : "sub"
  },
  "1st month" : {
    "answer"      : "$subName entschließt sich, unserer Community beizutreten! Vielen Dank dafür.",
    "subLevel"    : 1,
    "triggerType" : "sub"
  }
}
```
Hier sehen Sie diverse Arten `subLevel`, `minSubLevel` und `maxSubLevel` zu verwenden. Willowbot wird die Kommando-/Auslöserkategorie `sub` (`sub`, `subPrime`, `subGiftContinued`, `subGiftSingle`, `subGiftMulti`) durchlaufen und *jeden* Treffer ausführen, es ist also wichtig, ihre Einschränkungen sorgsam, d. h. sich nicht überschneidend zu wählen, um zu vermeiden, dass mehr als eine Reaktion ausgeführt wird. In der obigen Definition können Sie sehen, dass die Abonnementstufen sich gegenseitig ausschließen. Obwohl sie geordnet sind, ist dies nicht erforderlich, damit Willowbot die Reaktionen korrekt ausführt. Es wird auch die Performanz nicht verbessern.


##### Unterstütze Platzhalter nach Abonnementkontext

* `sub`
    * `subMonth`: die Anzahl Monate, die ein Nutzer bereits abonniert hat
    * `subName`: Anzeigename des abonnierenden Nutzers
* `subPrime`
    * siehe `sub`
* `subGiftContinued`
    * `subGiftGifter`: der Nutzer, der das verlängerte Abonnement ursprünglich verschenkt hat (Anzeigename)
    * `subName`: der Anzeigename des abonnementverlängernden Nutzers
* `subGiftSingle`:
    * `subGiftCountTotal`: Gesamtzahl bereits verschenkter Abonnements auf diesem Kanal durch den Nutzer
    * `subGiftGifter`: der das Abonnement verschenkende Nutzer (Anzeigename)
    * `subGiftRecipient`: der das Abonnement geschenkt bekommende Nutzer (Anzeigename)
* `subGiftSingleFollowup`:
    * siehe `subGiftSingle`
* `subGiftMulti`
    * `subGiftCount`: Anzahl der durch den Nutzer verschenkten Abonnements
    * `subGiftCountTotal`: Gesamtzahl bereits verschenkter Abonnements auf diesem Kanal durch den Nutzer
    * `subGiftGifter`: der die Abonnements verschenkende Nutzer (Anzeigename)


### 3.8 Antworttypen: sequentiell vs. zufällig

Willowbots Standardverhalten ist es, einfach die Zeichenkette, die im `answer`-Schlüssel der entsprechenden Reaktion definiert ist, zu senden. Allerdings hat Twitch ein internes Zeichenlimit von 500 pro Nachricht. Im Normalfall werden Ihre Antwortsätze dieses Limit nicht überschreiten, doch was, wenn Sie umfangreichere Informationen an den Chat senden wollen, z. B. Storyzusammenfassungen für das aktuell gespielte Spiel? Nein, dafür müssen Sie nicht mehrere Kommandos, wie `!zusammenfassung1`, `!zusammenfassung2` etc.,  definieren. Stattdessen schreiben Sie einfach Ihre Antwort in eine einzige Kommandodefinition, ungeachtet der Zeichenanzahl. Willowbot hat eine eingebaute Funktion, die Ihre Antwort in Stücke von maximal 500 Zeichen aufteilen (weniger, wenn das letzte Wort eines Stücks das 500. Zeichen überschreitet oder wenn, selbstverständlich, nicht mehr genügend Zeichen übrig sind, um das Limit zu erreichen) und stückweise sowie ohne erwähnenswerte Verzögerung dazwischen an den Chat senden wird.

Es gibt Situationen, in denen Sie möglicherweise bewusst sequentielle Nachrichten versenden möchten. Eine solche wurde im Kontext des Blacklistens von Wörtern/Wendungen erwähnt. Manche Emotes blinken sehr stark und können potentiell bei photosensitiven Menschen zu unerwünschten Reaktionen führen. Wenn Sie solche Emotes also von Ihrem Kanal ausschließen, möchten Sie vielleicht nicht nur entsprechende Nachrichten löschen, sondern zugleich Ihre Zuschauer darüber informieren, warum ihre Nachricht gelöscht wurde. So würden Sie das bewerkstelligen:
```
commands = {
  "colorFlash" : {
    "answer"    : "/delete $msgID\n/announce Bitte beachtet, dass wir Emotes, die photosensitive Menschen triggern könnten, vermeiden wollen. Vielen Dank.",
    "matchType" : "contains"
  }
}
```
Angenommen, `colorFlash` ist ein buntes und flackerndes Emote, wird die obige Reaktionsdefinition zwei Dinge tun, sobald eine Nachricht, die dieses Emote enthält, im Chat erscheint: Zuerst wird Willowbot die Nachricht löschen (`/delete $msgID`). Anschließend wird er eine neue Nachricht beginnen (`\n`) und eine Ankündigung über die gelöschte Nachricht versenden (`/announce Bitte beachtet, dass …`). Wie Sie sehen können, ist es möglich, eine einzige Antwort in einzelne Nachrichten aufzuteilen, indem Sie das Neue-Zeile-Zeichen (`\n`) verwenden. Dies können Sie beliebig oft tun und auf diese Weise so viele aufeinanderfolgende Nachrichten generieren, wie Sie möchten.

Es gibt einen zweiten Antwortmodus, der von Willowbot unterstützt wird, nämlich zufällige Antworten. Ein vorstellbarer Einsatzzweck ist ein kleines Communityspiel:
```
commands = {
  "!mopsen" : {
    "matchType"  : "startsWith",
    "answer"     : "$senderDisplayName mopst $arg0 Kekse.\n$senderDisplayName mopst $arg0 40 Münzen.\n$senderDisplayName mopst $arg0 eine alte Socke.\n$senderDisplayName mopst $arg0 stinkigen Käse.\n$senderDisplayName mopst $arg0 Unterhosen.",
    "answerType" : "random"
  }
}
```
Wenn Nutzer McFluffy dieses Kommando auslöst, indem er `!mopsen einnutzer` an den Chat sendet, wird Willowbot zufällig eine der durch `\n` getrennten Antworten im `answer`-Schlüssel auswählen und im Chat anzeigen, z. B. `McFluffy mopst einnutzer eine alte Socke.`


### 3.9 Betriebssystemkommandos

Neben dem Senden von Nachrichten an den Chat erlaubt Willowbot Ihnen, jedes beliebige Betriebssystemkommando auszuführen (sofern das Kommando keine Root-/Administratorrechte erfordert und Willowbot nicht mit diesen Rechten läuft, was *strengstens empfohlen* wird). Sie werden das hauptsächlich nutzen, um Geräusche oder Videos abzuspielen, aber Sie könnten Willowbot damit auch bestimmte Chatereignisse in eine Protokolldatei schreiben lassen.

Als Beispiel definieren wir ein Kommando, das Ihre Zuschauer jubeln lassen kann, wenn Sie in Ihrem Spiel einen Erfolg erringen, indem eine Tondatei abgespielt wird:
```
commands = {
  "!gg" : {
    "matchType"  : "startsWith",
    "os-command" : "start C:\der\pfad\zu\meiner\tondatei.mp3"
  }
}
```
Wann immer ein Nutzer `!gg` (oder eine andere Nachricht, die zumindest mit dieser Wendung beginnt) an den Chat sendet , wird Ihr System die Tondatei abspielen, die sich unter `C:\der\pfad\zu\meiner\tondatei.mp3` befindet. Beachten Sie, dass obige Definition nur auf Windowssystemen funktionieren wird! Unixsysteme benötigen ein Kommando wie `playsound /home/[Nutzer]/wo/meine/tondateien/liegen.mp3`, abhängig von der auf Ihrem System installierten Software. Solche Betriebssystemkommandos werden zusätzlich zum `answer`-Schlüssel ausgeführt, d. h. Sie können sie kombinieren und sowohl eine Nachricht an den Chat senden als auch eine Tondatei abspielen, ein Ereigbnis protokollieren, ein Video abspielen oder was auch immer Sie mit Ihrem Betriebssystemkommando anstellen wollen.


### 3.10 Nachrichten zur Fehlersuche (Debugging)

Möchten Sie Ihre Kommandos prüfen, d. h. eruieren, ob Willowbot auf bestimmte Ereignisse/Muster so wie von Ihnen vorgesehen reagieren wird, und entsprechende Rückmeldung über die Reaktionen bekommen, wollen zu diesem Zweck aber keine Nachricht in den Chat schreiben lassen, können Sie Willowbots `debug`-Schlüssel benutzen. Die Zeichenkette in Ihrem `debug`-Schlüssel wird sich genau so verhalten, als wäre es ein `answer`-Wert, allerdings wird es nicht an den Chat gesendet, sondern auf Ihrer Konsole ausgegeben. Das Auflösen von Argumenten und Platzhaltervariablen ist ebenfalls Bestandteil des `debug`-Schlüssels. `answer` und `debug` (und ebenso `os-command`) werden unabhängig voneinander verarbeitet, also können Sie diese Schlüssel in beliebiger Kombination für beliebige Zwecke definieren.


## 4 Optionale/Eigene Module

Willowbot besteht aus diversen Kernmodulen. Allerdings können Situationen auftreten, die etwas komplexere Aktionen als das Reagieren auf eine Chatnachricht durch das Absenden einer anderen Nachricht erfordern. Hier kommen dann eigene Module ins Spiel. Diese sind ebenfalls Pythonskripte und stellen Ihnen so Pythons komplettes Potential zur Verfügung, um Willowbots Funktionalität zu erweitern.

Um alle Routinen und Variablen säuberlich sortiert zu halten und das Risiko des ungewollten Überschreibens bereits definierter Routinen/Variablen zu minimieren, wird empfohlen, sie jeweils mit dem Modulnamen als Präfix zu versehen. Wenn Sie also bspw. ein Modul namens `verschenken` schreiben, sollten Sie die Routinen und Variablen innerhalb des Moduls `verschenken_tueDinge()`, `verschenken_teilnehmer`, `verschenken_tueIrgendetwasAnderes()` und so weiter nennen.

Diese optionalen Module können mittels einer Liste `activeModules`¹ aktiviert und deaktiviert werden. Willowbot wird nur die Module verwenden, die auf dieser Liste vertreten sind, also vergessen Sie nicht, Ihr Modul daraufzusetzen. Wenn Sie Schwierigkeiten mit einem bestimmten Modul haben (Fehler, unerwartetes Verhalten, Konflikte mit anderen Modulen etc.), müssen Sie es nicht vollständig aus der Liste oder gar dem `modules_opt`-Verzeichnis entfernen, sondern Sie können es einfach auskommentieren, indem Sie vor seinen Eintrag in `activeModules` ein `#` setzen. Diese auskommentieren Module werden nicht geladen, wenn Willowbot startet.

¹ Achtung, Windowsnutzer! Diese Datei hat keine Dateierweiterung/-endung, kann jedoch mit einem beliebigen Texteditor (z. B. Notepad) geöffnet und bearbeitet werden. Stellen Sie sicher, dass sie auch weiterhin keine Endung hat, wenn Sie Ihre Änderungen daran speichern. Falls diese Designentscheidung ein Punkt, der besonderer Aufmerksamkeit bedarf, und eine häufige Fehlerquelle ist, teilen Sie mir dies bitte mit.


### 4.1 Auf eigene Module zugreifen: der `function`-Schlüssel

Eine Routine aufzurufen, die Ihnen durch Ihr eigenes Modul zur Verfügung gestellt wird, erreichen Sie durch das Benutzen des `function`-Schlüssels in Ihrer Kommandodefinition. Der Wert für diesen Schlüssel ist eine Liste (list) aus Namen der Routinen und den ggf. zu übergeben nötigen Parametern. Diese Routinen werden in derselben Reihenfolge abgearbeitet, wie sie in der Liste stehen. Da das Schreiben eigener Module fundierte Kenntnis in der Programmiersprache Python erfordert, sollten sich nur erfahrene Nutzer daran wagen. Bitte seien Sie dessen gewahr, wenn Sie Willowbot erweitern wollen.


### 4.2 `poll`-Modul (Abstimmungen)

Ein erstes optionales Modul ist bereits in diesem Paket enthalten und erlaubt Ihren Zuschauern, an einer schnellen Umfrage teilzunehmen, die schlicht durch ein Chatkommando von Moderatoren oder dem Streamer gestartet werden kann. Wie in der Einführung dieses Kapitels erwähnt, nutzen wir die Routine, die die Abstimmung startet und im entsprechenden Modul hinterlegt ist, indem wir den `function`-Schlüssel in unserer Kommandodefinition verwenden:
```
commands = {
  '!abstimmung' : {
    'matchType' : 'startsWith',
    'debug'     : 'Abstimmung wurde gestartet.',
    'function'  : ['poll_start(commands, irc, "$arg0+", contextString = "Abstimmung offen für {pollDuration} Sekunden. Stimmt ab mit {pollOptions}.", resultString = "{votesQuantity} Stimme{pluralMod} wurde{pluralMod} abgegeben.", languageOverride = "en")'],
    'minLevel'  : 3
  }
}
```
Bevor wir uns dem interessantesten Part zuwenden, fassen wir kurz die anderen Dinge, die neben dem Aufruf einer Routine aus dem `poll`-Modul geschehen, zusammen. Die Abstimmung wird gestartet, sobald ein Nutzer mit wenigstens Level 3 (Moderator oder Streamer) eine Nachricht an den Chat sendet, die mit `!abstimmung` startet (`startsWith`). Sobald dies erfolgt ist, wird auf der Konsole die kurze Nachricht `Abstimmung wurde gestartet.` ausgegeben. Der in diesem Abschnitt neu eingeführte und in der Kommandodefinition genutzte Schlüssel ist `function`. Sein Wert ruft die Routine auf, die im Umfragemodul durch `def poll_start(commands, irc, *args, […])` definiert ist, und übergibt ihr die notwendigen Argumente. Da das `poll`-Modul das Kommandoset manipuliert, benötigt es `commands` als Argument. Des Weiteren wollen wir, dass das Modul in der Lage sein soll, Nachrichten an den Chat zu senden, also braucht es Zugriff auf unsere `irc`-Verbindung. Schließlich übergeben wird alle Argumente (`"$arg0+"`), die zusammen mit dem `!abstimmung`-Kommando in den Chat geschrieben wurden.

Das Modul akzeptiert auch einige optionale Argumente. Dass diese optional sind, lässt sich an ihren in der Funktionsdefinition vorgegebenen Standardwerten erkennen. In diesem Fall sind die optionalen Argumente `contextString`, `resultString` und `languageOverride`. Bitte beachten Sie, dass diese **nach** `$arg0+` **gesetzt werden müssen**, sollten Sie sich dafür entscheiden, sie zu nutzen. Deren Reihenfolge hingegen ist nicht von Belang.

Das `contextString`-Argument ist die Zeichenkette, die Willowbot an den Chat sendet, sobald eine Umfrage gestartet wird. Diese Zeichenkette darf die Platzhalter `{pollDuration}` und `{pollOptions}` enthalten. Ersterer wird bei der Auswertung des Befehls durch die Dauer der Abstimmung in Sekunden (d. h. durch das erste Argument nach dem `!abstimmung`-Befehl) ersetzt und Letzterer ist eine Zeichenkette, die das Modul automatisch erzeugt, indem es die Abstimmoptionen mittels Komma respektive »oder« in der von Willowbot genutzten Sprache zusammenfügt.

Welche Phrase zur Zusammenfassung der Abstimmergebnisse genutzt wird, wird durch `resultString` bestimmt. Dieses Argument akzeptiert den Platzhalter `{votesQuantity}`, der durch die Anzahl der Nutzer, die abgestimmt haben, ersetzt wird. Zusätzlich kann `{pluralMod}` genutzt werden, um das Wort »Stimme« (wie in »1 Stimme wurde abgegeben«) zu in Abhängigkeit davon, ob eine oder mehrere Stimmen abgegeben wurden, zu modifizieren.

Das letzte optionale Argument der `poll_start`-Routine ist `languageOverride`. Es wird verwendet, um die Sprache, in der die Konjuktion zwischen der vorletzten und letzten Abstimmoption in der generierten `{pollOptions}`-Zeichenkette erscheint, zu bestimmen. Dies bedeutet, dass Sie Willowbot bspw. auf Englisch starten, aber dennoch eine Ausgabe auf Deutsch erzeugen können, indem Sie `languageOverride = "de"` setzen.

Um nun tatsächlich eine Umfrage zu starten, würden Sie ein Kommando wie `!abstimmung 30 links rechts geradeaus` an den Chat senden. Dieses startet eine Abstimmung, die 30 Sekunden dauern und den Zuschauern erlauben wird, auszuwählen, wo es im derzeit gespielten Spiel als Nächstes langgehen soll – nach links, rechts oder geradeaus –, indem sie das passende Wort in den Chat schreiben. (Hinweis: Es ist ebenso möglich, die Abstimmdauer im `!abstimmung`-Befehl wegzulassen. Dann wird diese mit 60 Sekunden festgelegt.) Willowbot wird die Stimmen einsammeln und in einer Liste ablegen, die schließlich ausgewertet wird. Jeder Nutzer kann nur einmal abstimmen, jedoch seine Stimme ändern, indem er eine andere der verfügbaren Optionen in den Chat schreibt. Nachdem die Zeit, die dem `!abstimmung`-Kommando übergeben wurde, abgelaufen ist, wird die Abstimmung zusammengefasst und Willowbot schickt eine List mit den Ergebnissen an den Chat, angezeigt in Prozent und absteigender Reihenfolge, von der Option mit den meisten zu derjenigen mit den wenigsten Stimmen.

Umfragen abzubrechen ist ebenfalls möglich und kann durch die Verwendung von `poll_cancel(commands, irc)` als Wert für den Schlüssel `function` eingerichtet werden. Diese Routine wird darüber informieren, dass der Abbruch erfolgreich war, indem »Poll aborted.« in den Chat geschrieben wird. Soll Willowbot eine andere Bestätigungsnachricht abschicken, kann `cancelMessage` als optionaler Parameter beim Aufruf von `poll_cancel` gesetzt werden, was folgendermaßen aussehen würde:
```
commands = {
  '^!abstimmung abbrechen$' : {
    'matchType' : 'regex',
    'debug'     : 'Abstimmung wurde abgebrochen.',
    'function'  : ['poll_cancel(commands, irc, cancelMessage = "Keine Stimmen mehr abgeben. Die Abstimmung wurde abgebrochen."'],
    'minLevel'  : 3
  }
}
```


### 4.3 `modChannelInfo`-Modul (Kanalinformationen bearbeiten)

Dieses Modul erlaubt dem Bot, sowohl den Titel als auch die Kategorie eines Kanals abzurufen und zu bearbeiten. Die Voraussetzung dafür – zumindest für das Bearbeiten – ist jedoch, dass Willowbot über einen Zugangsschlüssel für den Kanal, dessen Daten er ändern möchte, verfügt. Fehlt ein solcher Zugangsschlüssel beim Betreten eines Kanals, wird Willowbot beim Verbindungsaufbau mit einer Meldung darauf hinweisen.

Sind Sie Moderator auf einem nicht von Ihnen betreuten Kanal, möchten Willowbots Funktion zum Ändern der Kanaldaten jedoch dort nutzen, benötigen Sie also einen Willowbotzugangsschlüssel des Streamers. <b>Dies ist mit einem gewissen Risiko verbunden!</b> Ein Moderator, der über einen anderen Zugangsschlüssel als seinen eigenen verfügt, kann Willowbot mit fremder Identität nutzen und so bspw. andere Nutzer in Misskredit bringen. Tauschen Sie Zugangsschlüssel also nur mit Personen aus, denen Sie genügend vertrauen. Bei Verdacht auf Missbrauch eines Zugangsschlüssels sollte dieser umgehend zurückgerufen und damit invalidiert werden (`--token revoke`)!

Dem in diesem Kapitel empfohlenen Namensschema für optionale Module folgend, sind die Namen der Routinen, die das `modChannelInfo`-Modul bereitstellt:

* `modChannelInfo_title_get`
* `modChannelInfo_title_set`
* `modChannelInfo_category_get`
* `modChannelInfo_category_set`

Jede dieser Routinen benötigt eine Instanz einer IRC-Verbindung sowie die Willowbotkonfiguration als obligatorische Argumente. Die optionalen Argumente sind jeweils eine Meldung bei erfolgreicher Anfrage, eine bei fehlgeschlagener Anfrage und bei den `set`-Routinen der gewünschte Titel bzw. die Kategorie.

Die folgenden Kommandodefinitionen stellen jeweils ein Beispiel für das Bearbeiten bzw. Abfragen eines Titels respektive einer Kategorie dar:
```
'^!title( |$)' : {
  'matchType' : 'regex',
  'function'  : ['modChannelInfo_title_get(irc, CONFIG, "Der aktuelle Titel ist »$return«.", "Konnte Titelinfo nicht abrufen.")'],
},
'^!title-set( |$)' : {
  'matchType' : 'regex',
  'function'  : ['modChannelInfo_title_set(irc, CONFIG, "$arg0+", "Der Titel wurde auf »$return« geändert.", "Konnte den Titel nicht ändern.")']
},
'^!game( |$)' : {
    'matchType' : 'regex',
    'function'  : ['modChannelInfo_category_get(irc, CONFIG, "Die aktuelle Kategorie ist »$return«.", "Konnte Kategorieinfo nicht abrufen.")'],
},
'^!game-set( |$)' : {
  'matchType' : 'regex',
  'function'  : ['modChannelInfo_category_set(irc, CONFIG, "$arg0+", "Mögliche Kandidaten: $return. Ändere das Spiel mit !game-set [Nummer] oder suche neu.", "Kategorie wurde auf »$return« geändert.", "Konnte die Kategorie nicht ändern.")']
}
```
Die `title_get`-Funktion kann vereinfacht als `modChannelInfo_title_get(irc, CONFIG)` aufgerufen werden, jedoch wird es dann im Chat keinerlei Rückmeldungen über den Titel geben. Das erste optionale Argument ist der Text, der bei erfolgreicher Serveranfrage zurückgegeben wird:
```
Der aktuelle Titel ist »$return«.
```
Dieser enthält den Platzhalter `$return`. Innerhalb des `modChannelInfo`-Moduls wird dieser durch den aktuellen Titel des abgefragten Streams ersetzt. Im Falle eines Fehlschlags der Serveranfrage wird der Text im zweiten optionalen Argument der Funktion ausgegeben.

`title_set` benötigt selbstverständlich einen vom Nutzer übergebenen Titel, der den alten ersetzen soll; dieser ist das erste optionale Argument in dieser Routine, oben als `$arg0+` verwendet, also als Platzhalter, der alle nach `!title-set` eingegebenen Textbestandteile einsammelt.

Die Routine `category_get` funktioniert analog zu `title_get` und bekommt lediglich eine Erfolgs- sowie eine Misserfolgsnachricht als optionale Argumente.

Die komplexeste Funktion in diesem Modul ist `category_set`. Wie `title_set` sammelt auch diese die eingegebenen Argumente (`$arg0+`) und übergibt sie in Gänze der Funktion. Hierbei handelt es sich um eine Zeichenkette, die einer auf Twitch verfügbaren Kategorie möglichst genau entsprechen sollte. Existiert nur eine Kategorie, worauf die übergebene Zeichenkette passt, wird die Kategorie des laufenden Streams auf ebendiese geändert. Ist die Anfrage jedoch nicht eindeutig, wird das Modul bis zu zehn Treffer in einer numerierten Liste im Chat ausgeben, deren Kontext durch das zweite optionale Argument bestimmt wird – in obigem Fall `Mögliche Kandidaten: $return. Ändere das Spiel mit !game-set [Nummer] oder suche neu.` Dabei wird `$return` mit einer Liste im Format `Spieltitel (1), weiterer Spieltitel (2), […]` ausgegeben. Diese Liste wird von Willowbot zwischengespeichert. Nun kann der Befehl `!game-set` erneut abgesetzt werden, jedoch kann nun anstelle eines konkreten Titels eine Nummer aus der zuvor ausgegebenen Liste gewählt und angefügt werden, also bspw. `!game-set 4`, und das `modChannelInfo`-Modul wird die Kategorie des Streams auf die mit entsprechender Nummer assoziierte ändern. Anschließend wird diese interne Liste gelöscht, so dass sich der Vorgang nur durch eine erneute Anfrage mit einem Kategorienamen wiederholen lässt.


### 4.4 `dateDiff`-Modul (Datumsdifferenzen ausgeben)

Ein sehr beliebter Chatbefehl ist die Ausgabe der verbleibenden Zeit, bis ein bestimmtes Ereignis eintritt, bspw. eine Spielepräsentation oder der Geburtstag des Streamers resp. der Streamerin. Dafür kann das `dateDiff`-Modul verwendet werden. Es erlaubt die Berechnung der Differenz zweier Daten sowie diejenige zwischen dem Zeitpunkt des Abschickens des Befehls, der mit diesem Modul verbunden ist, und einem Zieldatum.

Die Kernfunktion, die vom Endnutzer verwendet werden soll, ist `dateDiff_send`. Sie verwendet die folgenden Parameter:
* `irc`: Pflichtargument.
* `targetDate`: Pflichtargument; eine Zeichenkette im ISO-Format [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss] oder [MM]-[DD]; wird letztere Variante verwendet, wird Willowbot vom nächsten Eintreten dieser Monat-Tag-Kombination ausgehen, d. h. entweder im aktuellen oder im Folgejahr.
* `nowDate`: optional, Standardwert: `""`; siehe `targetDate`; wird dieser Parameter weggelassen, werden das tatsächliche aktuelle Datum sowie die aktuelle Uhrzeit anstelle derjenigen, die durch die angegebene Zeichenkette ausgedrückt wird, verwendet.
* `contextString`: optional, Standardwert: `{dateDiff}`; die Zeichenkette, die im Chat erscheinen soll, sobald das Chatkommando, das mit `dateDiff_send` verknüpft ist, verwendet wird, wobei `{dateDiff}` automatisch durch eine Zeichenkette in natürlicher Sprache ersetzt wird, die eine Zeitdifferenz in Worten angibt.
* `useAccusativeMod`: optional, Standardwert: `False`; einige Sprachen, wie bspw. Deutsch, verwenden einen Suffix, um den Akkusativ auszudrücken, und dieser Wahrheitswertparameter teilt Willowbot mit, ob jener Suffix verwendet werden soll, wenn die Datumsdifferenzzeichenkette in natürlicher Sprache erstellt wird.
* `languageOverride`: optional, Standardwert: `""`; soll Willowbot die Datumsdifferenzzeichenkette in einer anderen Sprache als derjenigen, mit der Willowbot gestartet wurde, ausgeben soll, verwenden Sie diesen Parameter mit dem Code einer Sprache, die im Unterverzeichnis `./lang` hinterlegt ist.

Eine Beispieldefinition für einen Chatbefehl, der `dateDiff_send` verwendet, ist die folgende:
```
'^!geb( |$)' : {
    'matchType' : 'regex',
    'function'  : ['dateDiff_send(irc, targetDate = "04-08", contextString = "In {dateDiff} hat die Streamerin Geburtstag.", useAccusativeMod = True, languageOverride = "de")']
  }
```

Schickt ein Chatteilnehmer den Befehl `!geb` ab, gibt der Bot (bspw.) die Antwort `In 221 Tagen, 12 Stunden, 10 Minuten und 17 Sekunden hat die Streamerin Geburtstag.` aus. Die Datumsdifferenzzeichenkette wird dort eingefügt, wo `{dateDiff}` in `contextString` auftaucht, und in diesem Fall ist es die bis 08. April verbleibende Zeit. In den meisten Fällen wird bei deutscher Sprache erforderlich sein, die Verwendung der Akkusativendungen via `useAccusativeMod = True` zuzuschalten, damit der Satz grammatisch korrekt ist. Wird Willowbot nicht ohnehin schon in deutscher Sprache gestartet, soll aber eine auf Deutsch formulierte Datumsdifferenz ausgeben, ist obendrein `languageOverride = "de"` als Funktionsparameter notwendig.


## 5 Test-/Fehlerbehandlungsmodus

Willowbot erlaubt Ihnen, Ihre Kommandodefinitionen entweder anhand eines spezifischen Nachrichtentexts oder mit einer Reihe vordefinierter Nachrichtentypen zu testen, damit Sie nicht auf das Erscheinen einer bestimmten Nachricht im Chat warten müssen, um die Korrektheit Ihrer Kommandosets prüfen zu können. Dazu muss die Option `--debug-single` zusammen mit einer Nachricht bzw. `--debug-full` als Option beim Start von Willowbot übergeben werden. In diesem Modus wird keine Verbindung zum Twitch-Chat hergestellt und die `answer`-Zeichenketten werden auf der Konsole ausgegeben, statt an den Chat gesendet zu werden.

Der erste Fall wird folgendermaßen ausgelöst:
```
python main_cli.py --channel ichbineinbot --debug-single "!mod @einandererNutzer Bitte schön."
```
Was hier geschieht, ist, dass Willowbot das Kommandoset für den Kanal `ichbineinbot` lädt, die Zeichenkette `!mod @einandererNutzer Bitte schön.` verarbeitet, als wäre sie eine Nutzernachricht im Chat gewesen, und Ihnen die Reaktion auf der Kommandozeile anzeigt. Achten Sie unbedingt auf die Anführungszeichen, die diese Nachricht einschließen!

Falls Sie mehrere Nachrichtentypen testen möchten, z. B. Primeabonnements, Ankündigungen, verschenkte Abonnements etc., können Sie den vollständigen Fehlerbehandlungsmodus verwenden:
```
python main_cli.py --channel ichbineinbot --debug-full
```
Indem Sie Willowbot auf diese Art starten, wird er einen Stapel vordefinierter authentischer, vollständiger Chatnachrichten mit bestimmten (anonymisierten und generischen) Metadaten, die sie als einen der verschiedenen Nachrichtentypen auf Twitch identifizieren, durchlaufen. Eine Liste der unterstützten Nachrichtentypen findet sich im Anhang.


## 6 Abschließende Worte

Willowbot ist nun seit einigen Monaten in Entwicklung und wird Stück für Stück erweitert, wann immer neue Szenarien, die abgedeckt werden müssen, auftauchen. Unter keinen Umständen sollte er als vollständig hinsichtlich seiner Funktionen betrachtet werden, aber er befindet sich nach wie vor in aktiver Entwicklung – einschließlich Bemühungen, Willowbot zugänglicher zu gestalten – und wird es wahrscheinlich lange Zeit bleiben.

Fühlen Sie sich frei, den Code als Inspiration für Ihre eigenen IRC-Projekte zu verwenden und Fehler/Auffälligkeiten, die auftauchen, zu melden. Ich werde versuchen, diese so bald wie möglich zu beseitigen.


## Anhang

### Implementierte Schlüsselprüfungen

* `answer`
    * Typ: Zeichenkette (string)
    * Antwort des Bots auf ein Kommando bzw. ein Nachrichtenmuster
* `answerType`
    * Typ: Zeichenkette (string)
    * `sequence` [Standardwert], `random`
* `cooldown`
    * Typ: Ganzzahl (integer)
    * erlaube dem Kommando nicht, erneut ausgelöst zu werden, bevor diese Zeitspanne abgelaufen ist; in Sekunden
* `debug`
    * Typ: Zeichenkette (string)
    * Fehlersuchmeldung; wird nur auf der Textkonsole angezeigt und nicht an den Chat gesendet
* `function`
    * Typ: Liste (list)
    * eine Liste aus Zeichenketten von Namen und deren Argumenten aufrufbarer Routinen aus eigenen Modulen
* `interval`
    * Typ: Ganzzahl (integer)
    * für zeitabhängige Kommandos; in Sekunden
* `level`
    * Typ: Ganzzahl (integer)
    * exakter benötigter Level, um das Kommando auszulösen
* `matchType`
    * Typ: Zeichenkette (string)
    * `is` [Standardwert], `is_caseInsensitive`, `startsWith`, `contains`, `contains_caseInsensitive`, `endsWith`, `regex`
* `maxRaidersCount`
    * Typ: Ganzzahl (integer)
    * maximale Anzahl an Raidern, die benötigt wird, um die zugehörige Nachricht auszulösen
* `maxSubLevel`
    * Typ: Ganzzahl (integer)
    * maximale Abomonatszahl, die benötigt wird, um die zugehörige Nachricht auszulösen; kann für Chatbefehle sowie für Abonnementnachrichten verwendet werden
* `minLevel`
    * Typ: Ganzzahl (integer)
    * minimaler Level, der benötigt wird, um das Kommando auszulösen
* `minRaidersCount`
    * Typ: Ganzzahl (integer)
    * minimale Anzahl an Raidern, die benötigt wird, um die zugehörige Nachricht auszulösen
* `minSubLevel`
    * Typ: Ganzzahl (integer)
    * minimale Abomonatszahl, die benötigt wird, um die zugehörige Nachricht auszulösen; kann für Chatbefehle sowie für Abonnementnachrichten verwendet werden
* `needsVIP`
    * Typ: Wahrheitswert (boolean)
    * beschränkt den Befehl auf die Nutzung durch VIP-Nutzer
* `os-command`
    * Typ: Zeichenkette (string)
    * ein Betriebssystemkommando, das ausgeführt wird, falls die anderen Bedingungen erfüllt sind (Level, Abklingzeit, Muster etc.)
* `senderName`
    * Typ: Liste (list)
    * führt den Befehl nur aus, wenn einer der in der Liste enthaltenen Nutzer mit dem angegebenen Loginnamen die auslösende Nachricht gesendet hat
* `senderDisplayName`
    * Typ: Liste (list)
    * führt den Befehl nur aus, wenn einer der in der Liste enthaltenen Nutzer mit dem angegebenen Anzeigenamen die auslösende Nachricht gesendet hat
* `subLevel`
    * Typ: Ganzzahl (integer)
    * exakte Abomonatszahl, die benötigt wird, um die zugehörige Nachricht auszulösen; kann für Chatbefehle sowie für Abonnementnachrichten verwendet werden
* `triggerType`
    * Typ: Zeichenkette (string)
    * `raid`, `sub`, `subGiftAnon`, `subGiftContinued`, `subGiftMulti`, `subGiftSingle`, `subGiftSingleFollowup`, `subPrime`


### Liste der Platzhaltervariablen

Variable für Botantworten, die ausgewertet werden, bevor Willowbot seine Antwort sendet:

* `arg0`, `arg1`, `arg2` etc.<br>die Argumente, die an das Kommando übergeben werden
* `arg0+`, `arg1+`, `arg2+` etc.<br>alle Argumente ab dem *n*ten werden zusammengeschlossen, getrennt durch Leerzeichen
* `msgID`<br>ID der verarbeiteten Nachricht; benötigt, um gezielt Nachrichten zu löschen
* `msgMeta` <br>die Metadaten der verarbeiteten Nachricht (hauptsächlich dazu gedacht, diese Daten an ein optionales Modul weiterreichen zu können)
* `msgText` <br>der komplette Text der verarbeiteten Nachricht (hauptsächlich dazu gedacht, die Nachricht in Gänze an ein optionales Modul weiterreichen zu können)
* `raidersChannelID`<br>die ID-Nummer des Kanals, von dem die Raider kommen
* `raidersChannelName`<br>der Kanal, von dem die Raider kommen
* `raidersCount`<br>Anzahl der Raider, die auf den Kanal kommen
* `senderDisplayName`<br>Anzeigename des Verfassers der verarbeiteten Nachricht
* `senderID`<br>ID-Nummer des Verfassers der verarbeiteten Nachricht
* `senderName`<br>Accountname des Verfassers der verarbeiteten Nachricht
* `subGiftCount`<br>Anzahl der verschenkten Abonnements bei einem Verschenkeereignis
* `subGiftCountTotal`<br>Gesamtzahl der vom verschenkenden Nutzer bereits verschenkten Abonnements
* `subGiftGifter`<br>Anzeigename des verschenkenden Nutzers
* `subGiftRecipient`<br>Anzeigename des Nutzers, der ein Geschenkabonnement erhält
* `subMonth`<br>Anzahl der Monate, die der Nutzer bereits abonniert hat
* `subName`<br>Anzeigename des abonnierenden Nutzers


### Liste der Fehlerbehandlungsnachrichtenmuster

(Sollten Sie die Notwendigkeit für weitere Nachrichtenmuster sehen, schlagen Sie diese gern vor.)

Derzeit sind folgende Nachrichtentypen in Willowbots Test-/Fehlerbehandlungsmodus enthalten:

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


### Liste der Kommandozeilenoptionen

* `-c`, `--channel {Kanalname}`<br>Zwingt Willowbot, sich mit dem Kanal `{Kanalname}` zu verbinden..
* `-cf`, `--configure`<br>Generiert eine Konfigurations- sowie eine Logindatei.
* `-df`, `--debug-full`<br>Willowbot wird auf eine Reihe vordefinierter Nachrichtenmuster reagieren und dabei Kommandos des mittels `--channel`-Option festgelegten Kanals verwenden. Wird die `--channel`-Option weggelassen, werden die Kommandos des als `botname` in der Konfigurationsdatei festgelegten Kanals verwendet.
* `-ds`, `--debug-single '{Nachricht}'`<br>Willowbot wird die Nachricht `{Nachricht}` wie eine gewöhnliche Chatnachricht behandeln und darauf reagieren. Beachten Sie die einfachen Anführungszeichen um die Nachricht.
* `-gc`, `--get-config [Schlüssel]`<br>Gibt alle Schlüssel der Willowbotkonfigurationsdatei und deren Werte aus. Wird ein bestimmter Schlüssel `[Schlüssel]` als zusätzliches Argument übergeben, wird nur eben dieser Schlüssel und dessen Wert angezeigt.
* `-h`, `--help`<br>Zeigt eine Übersicht an, wie Willowbot und seine Optionen benutzt werden, ähnlich der in diesem Abschnitt der Dokumentation.
* `-l`, `--login {Kontoname}`<br>Willowbot benutzt das Nutzerkonto `{Kontoname}` anstelle des als `botname` in der Konfigurationsdatei festgelegten.
* `-lg`, `--language {Sprachkürzel}`<br>Startet Willowbot mit der als {Sprachkürzel} übergebenen Sprache statt mit der Betriebssystemsprache (sofern diese unterstützt wird). Derzeit unterstützte Sprachkürzel können in Willowbots `lang`-Verzeichnis oder über die Nutzung der `--help`-Option in Willowbot selbst nachgesehen werden.
* `-sc`, `--set-config {key} {value}`<br>Setzt den in der Willowbotkonfigurationsdatei existierenden Schlüssel `{Schlüssel}` auf den Wert `{Wert}`.
* `-t`, `--token {keyword}`<br>Führt Zugansschlüsselaktionen aus. Benötigt eines der folgenden Schlüsselworte:
    * `add {Name} {Zugangsschlüssel}`<br>Fügt der Logindatei den Zugangsschlüssel `{Zugangsschlüssel}` für das Nutzerkonto `{Name}` hinzu.
    * `delete {Name}`<br>Entfernt den Namen `{Name}` sowie den damit assoziierten Zugangsschlüssel aus der Logindatei.
    * `get`<br>Generiert einen Zugangsschlüssel über Twitch.
    * `list`<br>Listet alle in der Logindatei hinterlegten Zugangsschlüssel auf.
    * `revoke {Name}`<br>Widerruft den mit dem Namen `{Name}` in der Logindatei hinterlegten Zugangsschlüssel. Dies entfernt entsprechenden Zugangsschlüssel zugleich aus der Logindatei.
