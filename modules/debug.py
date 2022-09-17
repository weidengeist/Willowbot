debugList = {
  'Action (/me)':
    '@badge-info=subscriber/56;badges=moderator/1,subscriber/3054;color=#FF0000;display-name=WillowbotDebugTester;emotes=1490352:46-54/555555584:56-57;first-msg=0;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=1;returning-chatter=0;room-id=123456789;subscriber=1;tmi-sent-ts=1658754900000;turbo=0;user-id=98765432;user-type=mod :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :ACTION I am a user who has emphasized his message.',

  'Announcement':
    '@badge-info=subscriber/56;badges=moderator/1,subscriber/36,artist-badge/1;color=#FF0000;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=willowbotdebugtester;mod=1;msg-id=announcement;msg-param-color=#FF0000;room-id=123456789;subscriber=1;system-msg=;tmi-sent-ts=1658754900000;user-id=98765432;user-type=mod :tmi.twitch.tv USERNOTICE #willowbotchannel :Attention everyone! This is an announcement.',

  'Ban':
    '@room-id=123456789;target-user-id=98765432;tmi-sent-ts=1658754900000 :tmi.twitch.tv CLEARCHAT #willowbotchannel :iamthebanneduser',

  
  'Deleted message':
    '@login=ilikespoilingsecrets;room-id=;target-msg-id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;tmi-sent-ts=1658754900000 :tmi.twitch.tv CLEARMSG #willowbotchannel :This is a message that has been deleted by someone with moderator privileges.',

  'Message (moderator)':
    '@badge-info=subscriber/56;badges=moderator/1,subscriber/2054;color=#FF0000;display-name=WillowbotDebugTester;emotes=;first-msg=0;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=1;returning-chatter=0;room-id=123456789;subscriber=1;tmi-sent-ts=1658754900000;turbo=0;user-id=98765432;user-type=mod :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :I am a moderator of this channel and posted this.',

  'Message (ordinary user)':
    '@badge-info=;badges=;client-nonce=9i8h7g6f5e4d3c2b1a;color=#FF0000;display-name=WillowbotDebugTester;emotes=555555560:83-84/555555584:114-115/1:31-32;first-msg=0;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=0;returning-chatter=0;room-id=123456789;subscriber=0;tmi-sent-ts=1658754900000;turbo=0;user-id=98765432;user-type= :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :This is a message from an non-sub user, not posting for the very first time.',

  'Message (ordinary user, first post ever)':
    '@badge-info=;badges=;client-nonce=9i8h7g6f5e4d3c2b1a;color=#FF0000;display-name=WillowbotDebugTester;emotes=555555560:83-84/555555584:114-115/1:31-32;first-msg=1;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=0;returning-chatter=0;room-id=123456789;subscriber=0;tmi-sent-ts=1658754900000;turbo=0;user-id=98765432;user-type= :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :This is a message from an non-sub user, posting for the very first time.',

  'Message (subscriber)':
    '@badge-info=subscriber/40;badges=subscriber/36,sub-gifter/50;client-nonce=9i8h7g6f5e4d3c2b1a;color=#FF0000;display-name=WillowbotDebugTester;emotes=300086928:10-18;first-msg=0;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=0;returning-chatter=0;room-id=123456789;subscriber=1;tmi-sent-ts=1658754900000;turbo=0;user-id=98765432;user-type= :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :This is a message from a subscriber.',

  'Message (VIP user)':
    '@badge-info=;badges=;client-nonce=9i8h7g6f5e4d3c2b1a;color=#FF0000;display-name=WillowbotDebugTester;emotes=555555560:83-84/555555584:114-115/1:31-32;first-msg=0;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;mod=0;returning-chatter=0;room-id=123456789;subscriber=0;tmi-sent-ts=1658754900000;turbo=0;user-id=98765432;user-type=;vip=1 :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv PRIVMSG #willowbotchannel :This is a message from an VIP user.',

  'Raid (999 raiders)':
    '@badge-info=subscriber/6;badges=subscriber/6,bits/100;color=#FF0000;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=willowbotdebugtester;mod=0;msg-id=raid;msg-param-displayName=WillowbotDebugTester;msg-param-login=willowbotdebugtester;msg-param-profileImageURL=https://static-cdn.jtvnw.net/jtv_user_pictures/this-url-leads-nowhere-profile_image-70x70.png;msg-param-viewerCount=999;room-id=123456789;subscriber=1;system-msg=999\sraiders\sfrom\sWillowbptDebugTester\shave\sjoined!;tmi-sent-ts=1658754900000;user-id=98765432;user-type= :tmi.twitch.tv USERNOTICE #willowbotchannel',

  'Subscription (Prime)':
    '@badge-info=subscriber/99;badges=subscriber/18;color=;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=willowbotdebugtester;mod=0;msg-id=resub;msg-param-cumulative-months=19;msg-param-months=0;msg-param-multimonth-duration=0;msg-param-multimonth-tenure=0;msg-param-should-share-streak=0;msg-param-sub-plan-name=A\ssubscription\sname\sfor\sWillowbot\sDebug\sTester;msg-param-sub-plan=Prime;msg-param-was-gifted=false;room-id=123456789;subscriber=1;system-msg=WillowbotDebugTester\ssubscribed\swith\sPrime.\sThey\'ve\ssubscribed\sfor\s99\smonths!;tmi-sent-ts=1658754900000;user-id=98765432;user-type= :tmi.twitch.tv USERNOTICE #willowbotchannel :I have subscribed with Prime and added this message.',

  'Subscription (resub, 99 months, tier 2)':
    '@badge-info=subscriber/99;badges=moderator/1,subscriber/2054;color=#FF0000;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=willowbotdebugtester;mod=1;msg-id=resub;msg-param-cumulative-months=99;msg-param-months=0;msg-param-multimonth-duration=0;msg-param-multimonth-tenure=0;msg-param-should-share-streak=0;msg-param-sub-plan-name=A\ssubscription\sname\sfor\sWillowbot\sDebug\sTester;msg-param-sub-plan=2000;msg-param-was-gifted=false;room-id=123456789;subscriber=1;system-msg=WillowbotDebugTester\ssubscribed\sat\sTier\s2.\sThey\'ve\ssubscribed\sfor\s99\smonths!;tmi-sent-ts=1658754900000;user-id=98765432;user-type=mod :tmi.twitch.tv USERNOTICE #willowbotchannel :The user who has just subscribed for 99 months has left this message.',

  'Subscription gift (anonymous)':
    '@badge-info=;badges=;color=;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=ananonymousgifter;mod=0;msg-id=subgift;msg-param-fun-string=FunStringFour;msg-param-gift-months=1;msg-param-months=1;msg-param-origin-id=this\sis\san\sorigin\sID;msg-param-recipient-display-name=WillowbotGiftRecipient;msg-param-recipient-id=12345678;msg-param-recipient-user-name=willowbotgiftrecipient;msg-param-sub-plan-name=A\ssubscription\sname\sfor\sWillowbot\sDebug\sTester;msg-param-sub-plan=1000;room-id=123456789;subscriber=0;system-msg=An\sanonymous\suser\sgifted\sa\sTier\s1\ssub\sto\sWillowbotDebugTester!\s;tmi-sent-ts=1658754900000;user-id=98765432;user-type= :tmi.twitch.tv USERNOTICE #willowbotchannel',

  'Subscription gift (multi, 10 gifts, 50 gifts total)':
    '@badge-info=subscriber/20;badges=subscriber/18,sub-gifter/10;color=#652669;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=willowbotdebugtester;mod=0;msg-id=submysterygift;msg-param-mass-gift-count=10;msg-param-origin-id=this\sis\san\sorigin\sID;msg-param-sender-count=50;msg-param-sub-plan=1000;room-id=123456789;subscriber=1;system-msg=WillowbotDebugTester\sis\sgifting\s10\sTier\s1\sSubs\sto\sWillowbotchannel\'s\scommunity!\sThey\'ve\sgifted\sa\stotal\sof\s50\sin\sthe\schannel!;tmi-sent-ts=1658754900000;user-id=98765432;user-type= :tmi.twitch.tv USERNOTICE #willowbotchannel',

  'Subscription gift (single, tier 1, 50 gifts total, month 35 for recipient)':
    '@badge-info=subscriber/25;badges=subscriber/2024,bits/25000;color=#FF0000;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=willowbotdebugtester;mod=0;msg-id=subgift;msg-param-gift-months=1;msg-param-months=35;msg-param-origin-id=this\sis\san\sorigin\sID;msg-param-recipient-display-name=WillowbotGiftRecipient;msg-param-recipient-id=74734078;msg-param-recipient-user-name=willowbotgiftrecipient;msg-param-sender-count=50;msg-param-sub-plan-name=A\ssubscription\sname\sfor\sWillowbot\sDebug\sTester;msg-param-sub-plan=1000;room-id=123456789;subscriber=1;system-msg=WillowbotDebugTester\sgifted\sa\sTier\s1\ssub\sto\sWillowbotGiftRecipient!\sThey\shave\sgiven\s50\sGift\sSubs\sin\sthe\schannel!;tmi-sent-ts=1658754900000;user-id=98765432;user-type= :tmi.twitch.tv USERNOTICE #willowbotchannel',

  'Subscription gift (single, follow-up message for multi-subgift)':
    '@badge-info=subscriber/20;badges=subscriber/18,sub-gifter/10;color=#652669;display-name=WillowbotDebugTester;emotes=;flags=;id=12345msgID54321-98765msgID56789-123-4u5v6w7x8y9z;login=willowbotdebugtester;mod=0;msg-id=subgift;msg-param-gift-months=1;msg-param-months=3;msg-param-origin-id=this\sis\san\sorigin\sID;msg-param-recipient-display-name=WillowbotGiftRecipient;msg-param-recipient-id=123456789;msg-param-recipient-user-name=willowbotgiftrecipient;msg-param-sender-count=0;msg-param-sub-plan-name=A\ssubscription\sname\sfor\sWillowbot\sDebug\sTester;msg-param-sub-plan=1000;room-id=123456789;subscriber=1;system-msg=willowbotdebugtester\sgifted\sa\sTier\s1\ssub\sto\sWillowbotGiftRecipient!;tmi-sent-ts=1658754900000;user-id=98765432;user-type= :tmi.twitch.tv USERNOTICE #willowbotchannel',

  'Whisper':
    '@badges=glitchcon2020/1;color=#FF0000;display-name=WillowbotDebugTester;emotes=;message-id=1;thread-id=12345678_987654321;turbo=0;user-id=98765432;user-type= :willowbotdebugtester!willowbotdebugtester@willowbotdebugtester.tmi.twitch.tv WHISPER willowbotwhisperrecipient :This is a whisper message from WillowbotDebugTester to WillowbotWhisperRecipient.',
}
