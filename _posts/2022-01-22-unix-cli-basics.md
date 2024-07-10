---
layout: post
title: unix command line basics
category: computer
---
This is the document I wish I had when I started using Unix command line interfaces (CLI). There are already many beginner's guides to using a unix CLI online, but I feel most of them skip some important commands. This article assumes you already know some of the most essential commands, and how to pass arguments to commands - if not, read [this article](https://www.linuxjournal.com/content/linux-command-line-interface-introduction-guide) first. If your using a Windows machine and are new to using CLIs, note that the CLIs that come with Windows operating systems are Command Prompt and Powershell which are not Unix CLIs, but you can [install a Unix CLI on your Windows computer](https://learn.microsoft.com/en-us/windows/wsl/install) if you desire.

#### man
Some beginner's guides don't teach this command, but I think it's most important because it shows **man**uals (ie instructions) for how to use other commands. For example, to learn how to use the command `ls` or to see what arguments you can pass to that command, enter `man ls` into your CLI. After displaying the instructions, press `q` to quit or `h` to show the help page which, among other things, will tell you how to navigate the manuals using your keyboard. Alternatively if you prefer a webpage, google "man <command>" and a link to a webpage with the command's manual will almsot certainly be the first result.

#### pwd
Stands for Present Working Directory, ie current directory. This just prints the current directory you're working from currently.

Prints the **p**resent **w**orking **d**irectory (ie the directory you're currently inside) to the screen.

#### less
You may know the command [cat](https://www.man7.org/linux/man-pages/man1/cat.1.html), but what if you want to navigate/read through a file and not just have all it's text dumped to your screen? Use the command `less`. You can use the same keys to navigate files opened using `less` as the commands that you use to navigate `man` pages.

#### nano
Sometimes you may need to edit a file with text in it. One of the easiest ways to do this from the command line is to use the `nano` text file editor. Simply type `nano <path to your file>` to open up a text editor in your CLI environment. Again, if you need help learning how to use the `nano` editor, you can use `man nano` (and google is always an option). There are numerous other CLI text editors, with `vim` probably being the most used, but since it requires a learning curve, I'd reccomend `nano` to beginners.

#### mkdir
Create a directory (eg a folder). Just type `mkdir <directory name>`.

#### sudo
If you're new to using CLIs, it's good to be aware of this command because it may not be obvious when you need it. If you ever try to give a command that you don't have permissions for, you CLI may compalin that you don't have permission to do it. For example:
```bash
$ apt-get update
Reading package lists... Done
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
E: Unable to lock directory /var/lib/apt/lists/
W: Problem unlinking the file /var/cache/apt/pkgcache.bin - RemoveCaches (13: Permission denied)
W: Problem unlinking the file /var/cache/apt/srcpkgcache.bin - RemoveCaches (13: Permission denied)
```
Here I'm trying to update my package manager, but I see that the CLI says I don't have permission. I can fix this by simply appending `sudo` to the begginning of my command and doing `sudo apt-get update`. My computer will then prompt me for my password before executing the command. Note that when you enter your password into the CLI, it will show no ticks or dots to register that it's receiving your keyboard input - this can throw off beginners.

This is also a good time to mention various expansions that are available in unix CLIs:
- `!!`: Expands to the last command you executed. For example, if you entered `apt-get update` as in the previous example, but now you want to prepend `sudo` to the command, you could enter `sudo !!` which the CLI will interpret as `sudo apt-get update`.
- `*`: This is the "wildcard" operator. See some helpful examples of using it [here](https://www.tecmint.com/use-wildcards-to-match-filenames-in-linux/).

Any other commands you wish you knew when you started out using CLIs? Let me know using the form at the bottom of this page.



