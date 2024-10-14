---
layout: post
title: packet captures with a native windows binary
---
Windows doesn't have tcpdump, so if you want to create a .pcap file from a packet capture, the easiest method is to download Wireshark or some other third party software. But it's still possible to create a pcap using native files installed on Windows - there's just a few more steps.

[Netsh.exe](https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-contexts) is a file in `\Windows\System32\` that can enable you to capture network packets with `netsh trace start capture=yes [filters]`. After you've captured the traffic, end the capture with `netsh trace stop`. Use the filters to filter out any traffic you don't want in the capture. To see information about available filters, use `netsh trace show capturefilterhelp`. To specify the output file, use `tracefile=DEST`.

At this point, you'll see the output file is an [.etl](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/trace-log) file. In order to convert it to a .pcapng file (which you'll need to do before you pop it open in Wireshark), you'll need to download [etl2pcapng](https://github.com/microsoft/etl2pcapng/); unfortunately, you can only run in on 64 bit Windows.
