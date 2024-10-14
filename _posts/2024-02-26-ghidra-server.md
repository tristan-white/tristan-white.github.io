---
layout: post
title: 'Ghidra Shared Projects: SRE Collaboration'
description: A quick start guide to get your Ghidra server up and running.
image: https://static1.makeuseofimages.com/wordpress/wp-content/uploads/2022/03/Installing-Ghidra-in-Linux.jpg
tag: [hacking]
---
To start a shared project in Ghidra you'll need a Ghidra server. How do you make or start one?

There's three things you need to do:

1. Get a copy of Ghidra.[^1]
2. Run the server install script.
3. Add authorized users to the server.[^2]

The first two steps have been automated by this script (see the comments for a description of what is happening):

<script src='https://gist.github.com/tristan-white/436d9dbdebab477f65bda06b228591d5.js'></script>

## Final Step: Add Users
After running the script, everything will be installed and ready to run. Before creating a shared project, you'll need to add a user to the server:

`sudo <SVRROOT>/server/svrAdmin -add <USERNAME>` [^3]

Now you can create a shared project! Here's a gif showing how:

<div style="width:100%;height:0;padding-bottom:75%;position:relative;"><iframe src="https://giphy.com/embed/qyCbhDOnIuwXuKu0WL" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>

NOTE: the first time you log in with a new user, the default password is "changeme". You will immediately be prompted to change this password after using it.

---
[^1]: A separate installation of Ghidra isn't necessary, but I think it's a good idea. Many people (myself included) switch to new versions of Ghidra by simply replacing their old Ghidra installation directory with a copy of the newer Ghidra version. By creating a separate directory for your Ghidra server, you'll prevent yourself from accidentally deleting your instance of the Ghidra server and its configuration.
[^2]: There are other authentication methods including PKI, a pre-shared SSH key, or no authentication at all. See the official documentation for Ghidra server in `<GHIDRA_INSTALL_DIR>/server/svrREADME.html` or a [copy I found online](https://static.grumpycoder.net/pixel/server/svrREADME.html)
[^3]: `SVRROOT` is set to `/opt/ghidrasvr` if you didn't change the install script. 

