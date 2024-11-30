---
layout: post
title: Echo As A File Uploader
description: How to write to embedded devices using echo up.
tag: [hacking]
---

Sometimes you want to write files/programs to an embedded device that does not have any file transfer utilities. If the embedded device has an 'echo' command that supports the '-n' and '-e' options, then we can effectively write files to disk in small chunks. Furthermore, we can use a tmux script to automate typing these echo commands. 

Check out my implementation of this [here](https://github.com/tristan-white/echo_sender/tree/main)