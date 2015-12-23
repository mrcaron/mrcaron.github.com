---
layout: post
title: "Cooperation Police"
---
Recently my company brought on some contractors for a few weeks to help tackle a big system configuration project. For obvious
reasons, I can't delve into that, but suffice it to say that we needed a lot of team coordiation. For reasons unknown to me,
our company blocks many useful tools for collaboration and team work. Slack, Trello, HipChat, etc are hopelessly outside
the bounds of our massive internet blocking. But, even in the face of the Cooperation Police, I can still facilitate
teamwork using old skool methods for fun and profit.

Sure they can block [Slack](http://www.slack.com) and [HipChat](http://www.hipchat.com), but they have neglected my little
friend, [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat). I discovered [Unreal IRC Daemon](https://www.unrealircd.org/),
which works really, really well on Windows; it's simply a config file edit and double click the daemon icon and you've got yourself
a bonafide IRC server to connect to. Clients like [HexChat](http://hexchat.github.io) are really simple to use and provide all
the little things you need, like flashing the window when an event occurs that you'd like to be notified of (this is **really**
handy because when working, I don't want to keep flipping back and forth to see if there's new messages). Sure, compared to
Slack and HipChat there's a lot missing (you mean I can't just drag-drop an image in the chat space to share it? dang!), but
it's basic interation and when copuled with a bot that can handle notifying you of checkins to your source control and other
special tasks (thanks for [Hubot](http://hubot.github.com), Github!), you're not that far behind the cool kids.

After using IRC for a week and really enjoying the interaction with the team (and getting really frustrated attempting to get 
hubot to work in Windows), I remembered that our SCM had a built in chat server with http client
