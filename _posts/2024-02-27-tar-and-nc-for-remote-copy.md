---
layout: post
title: Tar and Netcat
description: How to use tar and nc to dump a file system from embedded devices.
---

![](https://imgs.xkcd.com/comics/tar.png)

Having a copy of binaries from the target system is important in vulnerability research.

When investigating embedded systems, some factors can make this process more difficult:

- the target system lacks typical programs used for copying files to remotes systems (eg. `scp`)
- the target system is not physically accessible
- the target system has very little storage

I have noticed that netcat, or `nc`, is one utility that’s fairly common on embedded systems. Or at least more common than `scp`, which would be the easiest tool for remote copying directories. In the past, I’ve used `nc` for copying a single file at a time by setting up a listener on the target:

`# cat file.txt | nc -lp 1234` 

and then connecting to it from my host:

`$ nc <TARGET_IP_ADDR> 1234 > file.txt`

But it wasn’t till recently that I realized I could use `nc` in conjunction with `tar` (which is also fairly common to find on embedded systems) to easily copy an entire file system from target to host. You can do this with two commands.

First run `$ tar -cvz / | nc -lp 1234` on the target.

- `-c` tells tar to create an archive
- `-v` print file names as it archives them
- `-z` tells tar to compress the archive before sending it to netcat
- `/` specifies you want tar to create an archive from the root directory
- `-lp 1234` means “listen on port 1234”

Next run `$ nc <TARGET_IP_ADDR> 1234 | pv > rootfs.tar.gz` on your host system.

- `pv` this binary functionally behaves exactly like `cat` but will display progress of the transfer

Since tar creates the archive on the fly, it doesn’t matter if out target doesn’t have much storage to spare - as soon as tar packages and zips a small portion of the root directory, it sends it to netcat.

### Troubleshooting

If the archive being created by your `tar` command is growing much larger than expected, it’s probably because `tar` is attempting to archive things you don’t actually want archived.

For example: `/proc/kcore` is a virtual file that takes up very little physical space on disk but is massive if you try to read it. If `tar` attempts to archive it, you’ll likely run out of space on your system before `tar` is done reading `/proc/kcore` . Note that you won’t run into this issue if `tar` is not run by a privileged user.

You can exclude files and directories from the archive by using the `--exclude` option. 

Example: `tar -cvz --exclude proc / | nc -lp 1234` 

If you’re still running into issues with `tar` archiving undesired files, try reducing the archived directories to those located in your `PATH` variable.
