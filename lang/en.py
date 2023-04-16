langDict = {
  'commands_loadingFailed'                : 'WARNING! No commands available for channel {channel}.',
  'commands_loadingSuccessful'            : 'Successfully loaded commands for channel {channel}.',
  'config_channelOauthFound'              : 'Loaded the login oauth for channel {channel}.',
  'config_channelOauthMissing'            : 'WARNING! No login oauth found for {channel}. Some commands might be disabled due to missing privileges.',
  'config_loadingFailed_incomplete'       : 'ERROR! The configuration file at\n       {dir}\n   is incomplete. Please check.',
  'config_loadingFailed_missing'          : 'There is no config file in your Willowbot configuration directory:\n       {dir}\n   Will exit now. Have you configured Willowbot yet (--configure)?',
  'config_loadingSuccessful'              : 'Successfully loaded the IRC configuration file.',
  'config_loginFailed_noOauth'            : 'ERROR! There is no login oauth for {botname}. Please check your configuration and login files.',
  'config_loginFailed_noOauth_tryDefault' : 'WARNING! There is no login oauth for {botname}. Checking botname default …',
  'config_loginSuccessful'                : 'Successfully loaded the login oauth for {botname}.',
  'config_get_noFile'                     : 'There is no config file in\n    {dir}\n\nto retrieve data from. Have you configured Willowbot yet (--configure)?',
  'config_get_noSuchKey'                  : 'The key {key} does not exist in the config file, thus it can not be read.',
  'config_set_noFile'                     : 'There is no config file in\n    {dir}\n\nthe date of which can be modified. Have you configured Willowbot yet (--configure)?',
  'config_set_noKeyProvided'              : 'Please provide a key the value of which you want to set.',
  'config_set_noNewValue'                 : 'Please provide a new value for the key {key}.',
  'config_set_noSuchKey'                  : 'The key {key} does not exist in the config file, thus it can not be modified.',
  'config_set_valueUpdated'               : 'The key {key} has been updated!\n    old value: {oldValue}\n    new value: {newValue}',
  'configFiles_configFileAlreadyExists'   : 'A configuration file in\n    {dir}\nalready exists. Overwrite?',
  'configFiles_configFileUntouched'       : 'Configuration file remains untouched.',
  'configFiles_loginsFileAlreadyExists'   : 'A logins file in {dir} already exists. Overwrite?',
  'configFiles_loginsFileUntouched'       : 'Logins file remains untouched.',
  'configFiles_newConfigFile'             : 'Created a {optionalNew}configuration file.',
  'configFiles_newLoginsFile'             : 'Created a {optionalNew}logins file.',
  'configFiles_osMismatch'                : 'The detected OS, {os}, seems to be unsupported. Exit.',
  'debug_full_testingInfo'                : 'Testing IRC message of type {type}.',
  'debug_single_noMessageError'           : 'ERROR! You have to provide a message for the -ds/--debug-single option.',
  'irc_botnameSent'                       : 'Bot account name {botname} sent successfully.',
  'irc_channelEntered'                    : 'Successfully entered channel\n       {channel}.',
  'irc_connectionError'                   : 'Connection error.',
  'irc_connectionError_reconnection'      : 'Connection error. Trying to reconnect.\n\n——————————————————————————————————\n\n',
  'irc_connectionEstablished'             : 'Connected successfully. Waiting for messages on the server.',
  'irc_passSent'                          : 'Pass sent successfully.',
  'irc_reconnectionTrial'                 : 'Reconnection trial {currentTrial} of {maxTrials} in {seconds} seconds …   ',
  'logins_loadingFailed'                  : 'There is no logins file in your Willowbot configuration directory:\n       {dir}\n   Will exit now. Have you configured Willowbot yet (--configure)?',
  'logins_loadingSuccessful'              : 'Successfully loaded the logins file.',
  'optModules_importTrial'                : 'Trying to import module {module}.',
  'optModules_loadingFailed'              : 'Could not load {module}. Not found.',
  'optModules_loadingSuccessful'          : '{module} loaded successfully.',
  'regexError_exitMessage'                : '\nWillowbot can only be run with correct patterns. Exit.',
  'regexError_listItem'                   : '— {expression}\n    Error: {error}',
  'regexError_listPrefix'                 : 'There are errors in your following regular expressions:',
  'roles_missingClientID'                 : 'WARNING! Could not retrieve moderator and broadcaster IDs because of a missing client ID in your configuration, so processing chat commands (beginning with a slash) is not available! Please renew your access token by starting Willowbot with the option »--token revoke« to revoke your current one and start it again with the option »--token get« to generate a new one. Willowbot will continue now in its limited state.',
  'roles_retrievingFailed'                : 'WARNING! Could not retrieve moderator and broadcaster IDs, so processing chat commands (beginning with a slash) is not available! Error response:\n     ',
  'roles_retrievingSuccessful'            : 'Successfully retrieved\n       moderator ({botname}) ID: {moderatorID} and \n       broadcaster ({channel}) ID: {broadcasterID}.',
  # Token stuff.
  'tokenPage_clickInfo'                   : 'You may click the token below to copy it to your clipboard.',
  'tokenPage_copyStatus'                  : 'Token copied to the clipboard.',
  'tokenPage_commandInfo1'                : 'Paste this token into your terminal like this:',
  'tokenPage_commandInfo2'                : 'and press Enter to add this token<br>to your Willowbot logins file.',
  'tokenPage_h2'                          : 'Your token has been created.',
  'tokenPage_title'                       : 'Twitch OAuth token received',
  'tokenActions_add_cancelled'            : 'EXIT. Nothing added to the logins file.',
  'tokenActions_add_loginAlreadyExists'   : 'A login for {name} already exists in your logins file. Overwrite?',
  'tokenActions_add_needName'             : 'ERROR! The add option needs an account name and the token you want to add:\n      {pythonExec} {willowbotMain} --token add [account name] [token]',
  'tokenActions_add_needToken'            : 'ERROR! The add option needs a token for the account name you provided:\n      {pythonExec} {willowbotMain} --token add {name} [token]',
  'tokenActions_add_successful'           : 'Successfully added\n    {name}: {token}\nto your logins file.',
  'tokenActions_delete_cancelled'         : 'EXIT. Deletion cancelled.',
  'tokenActions_delete_nameNotFound'      : 'ERROR! Could’t find {name} in the logins file.',
  'tokenActions_delete_needName'          : 'ERROR! The delete option needs the name of the account the token of which you want to delete.',
  'tokenActions_delete_revocationWarning' : 'It is strictly discouraged to delete tokens without revoking (--token revoke) them. Only use this option for e.g. correcting typos. Continue anyway?',
  'tokenActions_delete_successful'        : 'Successfully deleted your access token from your logins file.',
  'tokenActions_missingKeyword'           : 'ERROR! The option -t or --token needs one of the following keywords: {keywords}.',
  'tokenActions_revoke_failed'            : 'An error occurred while trying to revoke your token!',
  'tokenActions_revoke_nameNotFound'      : 'ERROR! Could’t find {name} in the logins file.',
  'tokenActions_revoke_needName'          : 'ERROR! The revoke option needs the name of the account the token of which you want to revoke.',
  'tokenActions_revoke_successful'        : 'Successfully revoked your access token. It has been removed from your logins file.',
  'tokenActions_unknownOption'            : 'ERROR! Unknown token option. Available options: {options}.',
  # Help topics.
  'help_info_channel'                     : 'Make Willowbot connect to the channel {channel name}.',
  'help_info_config_get'                  : 'Show all keys of the Willowbot config file and their values. If you provide a distinct key [key] as an additional argument, onyl that key and its value will be shown.',
  'help_info_config_set'                  : 'Set the value of an existing key {key} of Willowbot’s config file to {value}.',
  'help_info_configure'                   : 'Generate a config and a logins file.',
  'help_info_debug_full'                  : 'Willowbot will react to a series of predefined message patterns, using the commands set of the channel specified via the --channel option. If the --channel option is omitted, the commands of the channel set as »botname« in the config file will be used.',
  'help_info_debug_single'                : 'Willowbot will treat {message} like an ordinary chat message and react to it. Note the single quotation marks around the message.',
  'help_info_help'                        : 'Show this overview.',
  'help_info_language'                    : 'Start Willowbot with the language that has the code {locale abbreviation} instead of with OS default language (provided it is supported). Currently supported language abbreviations: {langList}.',
  'help_info_login'                       : 'Make Willowbot use the account {account name} instead of the one stated as botname in the config file.',
  'help_info_token'                       : 'Perform a token operation. One of the following keywords is needed:',
  'help_info_token_add'                   : 'Add the token {token} for the account {name} to the logins file.',
  'help_info_token_delete'                : 'Remove {name} and the token associated with it from the logins file.',
  'help_info_token_get'                   : 'Generate a token via Twitch.',
  'help_info_token_list'                  : 'List all tokens residing in the logins file.',
  'help_info_token_revoke'                : 'Revoke the token listed in the logins file and associated with the passed {name}. This operation will also delete the token from the logins file.',
  # Some simple terms.
  'help_accountName'                      : 'account name',
  'help_channelName'                      : 'channel name',
  'help_configKey'                        : 'key',
  'help_configValue'                      : 'value',
  'help_keyword'                          : 'keyword',
  'help_localeAbbreviation'               : 'locale abbreviation',
  'help_message'                          : 'message',
  'help_name'                             : 'name',
  'help_option'                           : 'option',
  'help_options'                          : 'options',
  'help_token'                            : 'token',
  'help_usage'                            : 'Usage',
  'new_female'                            : 'new',
  'symbol_failure'                        : '×',
  'symbol_success'                        : '✔',
  'yesNo_prompt'                          : '[y]es/[n]o',
}
