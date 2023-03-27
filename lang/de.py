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
  'config_loginSuccessful'                : 'Erfolgreich den Schlüssel für {botname} geladen.',
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
  'regexError_listPrefix'                 : 'In den folgenden regulären Ausdrücken befinden sich Fehler:',
  'regexError_listItem'                   : '— {expression}\n    Fehler: {error}',
  'roles_missingClientID'                 : 'WARNUNG! Konnte Moderator- und Streamer-ID wegen einer fehlenden Client-ID in Ihrer Konfiguration nicht beziehen, weshalb das Verarbeiten von Chatkommandos (mit Schrägstrich beginnend) nicht möglich ist! Bitte erneuern Sie Ihren Zugangsschlüssel, indem Sie Willowbot zunächst mit der Option »--token revoke«, um Ihren aktuellen Schlüssel zu widerrufen, und anschließend zum Generieren eines neuen Schlüssels mit »--token get« starten. Willowbot fährt jetzt im eingeschränkten Modus fort.',
  'roles_retrievingFailed'                : 'WARNUNG! Konnte Moderator- und Streamer-ID nicht beziehen, weshalb das Verarbeiten von Chatkommandos (mit Schrägstrich beginnend) nicht möglich ist! Fehlermeldung:\n     ',
  'roles_retrievingSuccessful'            : 'Erfolgreich\n       Moderator-({botname}-)ID: {moderatorID} und\n       Streamer-({channel}-)ID: {broadcasterID}.\n   empfangen.',
  'tokenPage_title'                       : 'Twitchzugangsschlüssel empfangen',
  'tokenPage_h2'                          : 'Ihr Zugangsschlüssel wurde erstellt.',
  'tokenPage_clickInfo'                   : 'Sie können auf den nun folgenden Zugangsschlüssel klicken, um ihn in die Zwischenablage zu kopieren.',
  'tokenPage_copyStatus'                  : 'Schlüssel in die Zwischenablage kopiert.',
  'tokenPage_commandInfo1'                : 'Fügen Sie diesen Schlüssel wie folgt in Ihre Kommandozeile ein:',
  'tokenPage_commandInfo2'                : 'und drücken Sie Enter, um diesen Schlüssel<br>Ihrer Willowbotlogindatei hinzuzufügen.',
  'configFiles_osMismatch'                : 'Das erkannte Betriebssystem, {os}, scheint nicht unterstützt zu werden. Beende.',
  'configFiles_configFileAlreadyExists'   : 'Eine Konfigurationsdatei existiert im Verzeichnis\n    {dir}\nbereits. Überschreiben?',
  'yesNo_prompt'                          : '[j]a/[n]ein',
  'configFiles_newConfigFile'             : 'Eine {optionalNew}Konfigurationsdatei wurde angelegt.',
  'new_female'                            : 'neue',
  'configFiles_configFileUntouched'       : 'Konfigurationsdatei bleibt unverändert.',
  'configFiles_loginsFileAlreadyExists'   : 'Eine Logindatei existiert im Verzeichnis\n    {dir}\nbereits. Überschreiben?',
  'configFiles_newLoginsFile'             : 'Eine {optionalNew}Logindatei wurde angelegt.',
  'configFiles_loginsFileUntouched'       : 'Logindatei bleibt unverändert.',
  'tokenActions_unknownOption'            : 'FEHLER! Unbekannte Schlüsseloption. Verfügbare Optionen: {options}.',
  'tokenActions_add_needName'             : 'FEHLER! Die add-Option benötigt einen Accountnamen sowie den hinzuzufügenden Schlüssel:\n      {pythonExec} {willowbotMain} --token add [Accountname] [Schlüssel]',
  'tokenActions_add_needToken'            : 'FEHLER! Die add-Option benötigt einen Schlüssel für den angegebenen Accountnamen:\n      {pythonExec} {willowbotMain} --token add {name} [Schlüssel]',
  'tokenActions_add_loginAlreadyExists'   : 'Ein Schlüssel für {name} existiert in Ihrer Logindatei bereits. Überschreiben?',
  'tokenActions_add_successful'           : 'Erfolgreich\n    {name}: {token}\nder Logindatei hinzugefügt.',
  'tokenActions_add_cancelled'            : 'ENDE. Der Logindatei wurde nichts hinzugefügt.',
  'tokenActions_delete_needName'          : 'FEHLER! Die delete-Option braucht den Namen des Accounts, dessen Schlüssel gelöscht werden soll.',
  'tokenActions_delete_revocationWarning' : 'Es wird strengstens davon abgeraten, einen Schlüssel ohne einen Widerruf dessen (--token revoke) zu löschen. Benutzen Sie diese Option nur bspw. zum Korrigieren von Tippfehlern. Dennoch fortfahren?',
  'tokenActions_delete_successful'        : 'Schlüssel erfolgreich aus der Logindatei gelöscht.',
  'tokenActions_delete_cancelled'         : 'ENDE. Löschvorgang abgebrochen.',
  'tokenActions_delete_nameNotFound'      : 'FEHLER! Der Name {name} wurde in der Logindatei nicht gefunden.',
  'tokenActions_revoke_needName'          : 'FEHLER! Die revoke-Option benötigt den Namen des Accounts, dessen Schlüssel gelöscht werden soll.',
  'tokenActions_revoke_successful'        : 'Schlüssel wurde erfolgreich widerrufen. Er wurde aus der Logindatei gelöscht.',
  'tokenActions_revoke_failed'            : 'Beim Rückruf des Schlüssels trat ein Fehler auf!',
  'tokenActions_revoke_nameNotFound'      : 'FEHLER! Der Name {name} wurde in der Logindatei nicht gefunden.',
  'tokenActions_missingKeyword'           : 'FEHLER! Die Option -t oder --token benötigt eines der folgenden Schlüsselworte: {keywords}.',
  'debug_single_noMessageError'           : 'FEHLER! Der Option -ds/--debug-single muss eine Nachricht übergeben werden.',
  'debug_full_testingInfo'                : 'Teste IRC-Nachricht des Typs {type}.',
  'help_usage'                            : 'Verwendung',
  'help_option'                           : 'Option',
  'help_options'                          : 'Optionen',
  'help_channelName'                      : 'Kanalname',
  'help_info_channel'                     : 'Zwingt Willowbot, sich mit dem Kanal {Kanalname} zu verbinden.',
  'help_info_configure'                   : 'Generiert eine Konfigurations- sowie eine Logindatei.',
  'help_info_debug_full'                  : 'Willowbot wird auf eine Reihe vordefinierter Nachrichtenmuster reagieren und dabei Kommandos des mittels --channel-Option ausgewählten Kanals verwenden.',
  'help_info_debug_single'                : 'Willowbot wird die Nachricht {Nachricht} wie eine gewöhnliche Chatnachricht behandeln und darauf reagieren. Beachten Sie die einfachen Anführungszeichen um die Nachricht.',
  'help_info_help'                        : 'Zeigt diese Übersicht an.',
  'help_info_login'                       : 'Willowbot benutzt das Nutzerkonto {Kontoname} anstelle des als »botname« in der Konfigurationsdatei festgelegten.',
  'help_info_language'                    : 'Startet Willowbot mit einer anderen als der Betriebssystemsprache. Derzeit unterstützte Sprachen/Kürzel: {langList}.',
  'help_info_token'                       : 'Führt Zugansschlüsselaktionen aus. Benötigt eines der folgenden Schlüsselworte:',
  'help_info_token_add'                   : 'Fügt der Logindatei den Schlüssel {Schlüssel} für das Nutzerkonto {Name} hinzu.',
  'help_info_token_delete'                : 'Entfernt den Namen {Name} sowie den damit assoziierten Schlüssel aus der Logindatei.',
  'help_info_token_get'                   : 'Generiert einen Zugangsschlüssel über Twitch.',
  'help_info_token_list'                  : 'Listet alle in der Logindatei hinterlegten Schlüssel auf.',
  'help_info_token_revoke'                : 'Widerruft den mit dem Namen {Name} in der Logindatei hinterlegten Schlüssel. Dies entfernt entsprechenden Schlüssel zugleich aus der Logindatei.',
  'help_message'                          : 'Nachricht',
  'help_accountName'                      : 'Kontoname',
  'help_localeAbbreviation'               : 'Sprachkürzel',
  'help_keyword'                          : 'Schlüsselwort',
  'help_name'                             : 'Name',
  'help_token'                            : 'Schlüssel',
}
