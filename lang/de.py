langDict = {
  'commands_loadingFailed'                : 'WARNUNG! Keine Kommandos für Kanal {channel} verfügbar.',
  'commands_loadingSuccessful'            : 'Erfolgreich die Kommandos für den Kanal {channel} geladen.',
  'config_channelOauthFound'              : 'Zugangsschlüssel für den Kanal {channel} geladen.',
  'config_channelOauthMissing'            : 'WARNUNG! Kein Zugangsschlüssel für den Kanal {channel} gefunden. Einige Kommandos sind möglicherweise wegen fehlender Berechtigungen nicht verfügbar.',
  'config_loadingFailed_incomplete'       : 'FEHLER! Die Konfigurationsdatei unter\n       {dir}\n   ist unvollständig. Bitte prüfen.',
  'config_loadingFailed_missing'          : 'In Willowbots Konfigurationsverzeichnis befindet sich keine Konfigrationsdatei:\n       {dir}\n   Programm beendet. Wurde Willowbot bereits konfiguriert (--configure)?',
  'config_loadingSuccessful'              : 'Erfolgreich IRC-Konfiguration geladen.',
  'config_loginFailed_noOauth'            : 'FEHLER! Es gibt keinen Zugangsschlüssel für {botname}. Bitte Konfigurations- und Logindatei prüfen.',
  'config_loginFailed_noOauth_tryDefault' : 'WARNUNG! Es gibt keinen Zugangsschlüssel für {botname}. Prüfe den Standardbotnamen …',
  'config_loginSuccessful'                : 'Erfolgreich den Zugangsschlüssel für {botname} geladen.',
  'config_get_noFile'                     : 'Keine Konfigurationsdatei unter\n    {dir}\n\ngefunden, um deren Daten zu lesen. Wurde Willowbot bereits konfiguriert (--configure)?',
  'config_get_noSuchKey'                  : 'Der Schlüssel {key} existiert in der Konfigurationsdatei nicht, kann folglich auch nicht gelesen werden.',
  'config_set_noFile'                     : 'Keine Konfigurationsdatei unter\n    {dir}\n\ngefunden, deren Daten verändert werden könnten. Wurde Willowbot bereits konfiguriert (--configure)?',
  'config_set_noKeyProvided'              : 'Bitte geben Sie einen Schlüssel an, dessen Wert Sie ändern möchten.',
  'config_set_noNewValue'                 : 'Bitte geben Sie einen neuen Wert für den Schlüssel {key} an.',
  'config_set_noSuchKey'                  : 'Der Schlüssel {key} existiert in der Konfigurationsdatei nicht, kann folglich auch nicht verändert werden.',
  'config_set_valueUpdated'               : 'Der Schlüssel {key} wurde aktualisiert!\n    alter Wert: {oldValue}\n    neuer Wert: {newValue}',
  'configFiles_configFileAlreadyExists'   : 'Eine Konfigurationsdatei existiert im Verzeichnis\n    {dir}\nbereits. Überschreiben?',
  'configFiles_configFileUntouched'       : 'Konfigurationsdatei bleibt unverändert.',
  'configFiles_loginsFileAlreadyExists'   : 'Eine Logindatei existiert im Verzeichnis\n    {dir}\nbereits. Überschreiben?',
  'configFiles_loginsFileUntouched'       : 'Logindatei bleibt unverändert.',
  'configFiles_newConfigFile'             : 'Eine {optionalNew}Konfigurationsdatei wurde angelegt.',
  'configFiles_newLoginsFile'             : 'Eine {optionalNew}Logindatei wurde angelegt.',
  'configFiles_osMismatch'                : 'Das erkannte Betriebssystem, {os}, scheint nicht unterstützt zu werden. Beende.',
  'debug_full_testingInfo'                : 'Teste IRC-Nachricht des Typs {type}.',
  'debug_single_noMessageError'           : 'FEHLER! Der Option -ds/--debug-single muss eine Nachricht übergeben werden.',
  'irc_botnameSent'                       : 'Botaccountname {botname} erfolgreich übermittelt.',
  'irc_channelEntered'                    : 'Kanal\n       {channel}\n   erfolgreich betreten.',
  'irc_connectionError'                   : 'Verbindungsfehler.',
  'irc_connectionError_reconnection'      : 'Verbindungsfehler. Versuche Wiederaufbau der Verbindung.\n\n——————————————————————————————————\n\n',
  'irc_connectionEstablished'             : 'Erfolgreich verbunden. Warte auf Nachrichten auf dem Server.',
  'irc_passSent'                          : 'Zugangsschlüssel erfolgreich übermittelt.',
  'irc_reconnectionTrial'                 : 'Verbindungsversuch {currentTrial} von {maxTrials} in {seconds} Sekunden …   ',
  'logins_loadingFailed'                  : 'In Willowbots Konfigurationsverzeichnis befindet sich keine Logindatei:\n       {dir}\n   Programm beendet. Wurde Willowbot bereits konfiguriert (--configure)?',
  'logins_loadingSuccessful'              : 'Logindatei erfolgreich geladen.',
  'optModules_importTrial'                : 'Versuche, das Modul {module} zu importieren.',
  'optModules_loadingFailed'              : '{module} konnte nicht geladen werden. Nicht gefunden.',
  'optModules_loadingSuccessful'          : '{module} erfolgreich geladen.',
  'regexError_exitMessage'                : '\nWillowbot läuft nur mit korrekten Ausdrücken. Beende.',
  'regexError_listItem'                   : '— {expression}\n    Fehler: {error}',
  'regexError_listPrefix'                 : 'In den folgenden regulären Ausdrücken befinden sich Fehler:',
  'roles_missingClientID'                 : 'WARNUNG! Konnte Moderator- und Streamer-ID wegen einer fehlenden Client-ID in Ihrer Konfiguration nicht beziehen, weshalb das Verarbeiten von Chatkommandos (mit Schrägstrich beginnend) nicht möglich ist! Bitte erneuern Sie Ihren Zugangsschlüssel, indem Sie Willowbot zunächst mit der Option »--token revoke«, um Ihren aktuellen Zugangsschlüssel zu widerrufen, und anschließend zum Generieren eines neuen Zugangsschlüssels mit »--token get« starten. Willowbot fährt jetzt im eingeschränkten Modus fort.',
  'roles_retrievingFailed'                : 'WARNUNG! Konnte Moderator- und Streamer-ID nicht beziehen, weshalb das Verarbeiten von Chatkommandos (mit Schrägstrich beginnend) nicht möglich ist! Fehlermeldung:\n     ',
  'roles_retrievingSuccessful'            : 'Erfolgreich\n       Moderator-({botname}-)ID: {moderatorID} und\n       Streamer-({channel}-)ID: {broadcasterID}.\n   empfangen.',
  # Token stuff.
  'tokenPage_clickInfo'                   : 'Sie können auf den nun folgenden Zugangsschlüssel klicken, um ihn in die Zwischenablage zu kopieren.',
  'tokenPage_copyStatus'                  : 'Schlüssel in die Zwischenablage kopiert.',
  'tokenPage_commandInfo1'                : 'Fügen Sie diesen Schlüssel wie folgt in Ihre Kommandozeile ein:',
  'tokenPage_commandInfo2'                : 'und drücken Sie Enter, um diesen Zugangsschlüssel<br>Ihrer Willowbotlogindatei hinzuzufügen.',
  'tokenPage_h2'                          : 'Ihr Zugangsschlüssel wurde erstellt.',
  'tokenPage_title'                       : 'Twitchzugangsschlüssel empfangen',
  'tokenActions_add_cancelled'            : 'ENDE. Der Logindatei wurde nichts hinzugefügt.',
  'tokenActions_add_loginAlreadyExists'   : 'Ein Zugangsschlüssel für {name} existiert in Ihrer Logindatei bereits. Überschreiben?',
  'tokenActions_add_needName'             : 'FEHLER! Die add-Option benötigt einen Accountnamen sowie den hinzuzufügenden Zugangsschlüssel:\n      {pythonExec} {willowbotMain} --token add [Accountname] [Zugangsschlüssel]',
  'tokenActions_add_needToken'            : 'FEHLER! Die add-Option benötigt einen Zugangsschlüssel für den angegebenen Accountnamen:\n      {pythonExec} {willowbotMain} --token add {name} [Zugangsschlüssel]',
  'tokenActions_add_successful'           : 'Erfolgreich\n    {name}: {token}\nder Logindatei hinzugefügt.',
  'tokenActions_delete_cancelled'         : 'ENDE. Löschvorgang abgebrochen.',
  'tokenActions_delete_nameNotFound'      : 'FEHLER! Der Name {name} wurde in der Logindatei nicht gefunden.',
  'tokenActions_delete_needName'          : 'FEHLER! Die delete-Option braucht den Namen des Accounts, dessen Zugangsschlüssel gelöscht werden soll.',
  'tokenActions_delete_revocationWarning' : 'Es wird strengstens davon abgeraten, einen Zugangsschlüssel ohne einen Widerruf dessen (--token revoke) zu löschen. Benutzen Sie diese Option nur bspw. zum Korrigieren von Tippfehlern. Dennoch fortfahren?',
  'tokenActions_delete_successful'        : 'Zugangsschlüssel erfolgreich aus der Logindatei gelöscht.',
  'tokenActions_missingKeyword'           : 'FEHLER! Die Option -t oder --token benötigt eines der folgenden Schlüsselworte: {keywords}.',
  'tokenActions_revoke_failed'            : 'Beim Widerruf des Zugangsschlüssels trat ein Fehler auf!',
  'tokenActions_revoke_nameNotFound'      : 'FEHLER! Der Name {name} wurde in der Logindatei nicht gefunden.',
  'tokenActions_revoke_needName'          : 'FEHLER! Die revoke-Option benötigt den Namen des Accounts, dessen Zugangsschlüssel gelöscht werden soll.',
  'tokenActions_revoke_successful'        : 'Zugangsschlüssel wurde erfolgreich widerrufen. Er wurde aus der Logindatei gelöscht.',
  'tokenActions_unknownOption'            : 'FEHLER! Unbekannte Zugangsschlüsseloption. Verfügbare Optionen: {options}.',
  # Help topics.
  'help_info_channel'                     : 'Zwingt Willowbot, sich mit dem Kanal {Kanalname} zu verbinden.',
  'help_info_config_get'                  : 'Gibt alle Schlüssel der Willowbotkonfigurationsdatei und deren Werte aus. Wird ein bestimmter Schlüssel [Schlüssel] als zusätzliches Argument übergeben, wird nur eben dieser Schlüssel und dessen Wert angezeigt.',
  'help_info_config_set'                  : 'Setzt den in der Willowbotkonfigurationsdatei existierenden Schlüssel {Schlüssel} auf den Wert {Wert}.',
  'help_info_configure'                   : 'Generiert eine Konfigurations- sowie eine Logindatei.',
  'help_info_debug_full'                  : 'Willowbot wird auf eine Reihe vordefinierter Nachrichtenmuster reagieren und dabei Kommandos des mittels --channel-Option festgelegten Kanals verwenden. Wird die --channel-Option weggelassen, werden die Kommandos des als »botname« in der Konfigurationsdatei festgelegten Kanals verwendet.',
  'help_info_debug_single'                : 'Willowbot wird die Nachricht {Nachricht} wie eine gewöhnliche Chatnachricht behandeln und darauf reagieren. Beachten Sie die einfachen Anführungszeichen um die Nachricht.',
  'help_info_help'                        : 'Zeigt diese Übersicht an.',
  'help_info_language'                    : 'Startet Willowbot mit der als {Sprachkürzel} übergebenen Sprache statt mit der Betriebssystemsprache (sofern diese unterstützt wird). Derzeit unterstützte Sprachen/Kürzel: {langList}.',
  'help_info_login'                       : 'Willowbot benutzt das Nutzerkonto {Kontoname} anstelle des als »botname« in der Konfigurationsdatei festgelegten.',
  'help_info_token'                       : 'Führt Zugansschlüsselaktionen aus. Benötigt eines der folgenden Schlüsselworte:',
  'help_info_token_add'                   : 'Fügt der Logindatei den Zugangsschlüssel {Zugangsschlüssel} für das Nutzerkonto {Name} hinzu.',
  'help_info_token_delete'                : 'Entfernt den Namen {Name} sowie den damit assoziierten Zugangsschlüssel aus der Logindatei.',
  'help_info_token_get'                   : 'Generiert einen Zugangsschlüssel über Twitch.',
  'help_info_token_list'                  : 'Listet alle in der Logindatei hinterlegten Zugangsschlüssel auf.',
  'help_info_token_revoke'                : 'Widerruft den mit dem Namen {Name} in der Logindatei hinterlegten Zugangsschlüssel. Dies entfernt entsprechenden Zugangsschlüssel zugleich aus der Logindatei.',
  # Some simple terms.
  'help_accountName'                      : 'Kontoname',
  'help_channelName'                      : 'Kanalname',
  'help_configKey'                        : 'Schlüssel',
  'help_configValue'                      : 'Wert',
  'help_keyword'                          : 'Schlüsselwort',
  'help_localeAbbreviation'               : 'Sprachkürzel',
  'help_message'                          : 'Nachricht',
  'help_name'                             : 'Name',
  'help_option'                           : 'Option',
  'help_options'                          : 'Optionen',
  'help_token'                            : 'Zugangsschlüssel',
  'help_usage'                            : 'Verwendung',
  'new_female'                            : 'neue',
  'symbol_failure'                        : '×',
  'symbol_success'                        : '✔',
  'yesNo_prompt'                          : '[j]a/[n]ein',
}
