---
layout: post
title: mitmproxy
description: A tool I wish I learned before burp suite.
tag: [hacking]
---
I've found that sometimes "being good" at computer security is just about knowing the right tool for the right job, so occasionally I'll make a post like this one to evangelize tools I've found very helpful that I think will help others ho are growing their offensive security toolset.

Recently, some [OSCP](https://www.offsec.com/courses/pen-200/) experience came in handy as I was trying to analyze and manipulate traffic that was going between a client and a webserver over https. There's two tools that can do this job well:

- [Burp Suite](https://portswigger.net/burp)
- [mitmproxy](https://mitmproxy.org/)

Burp Suite has a paid and free version and uses a GUI, whereas mitmproxy is free and open source. Naturally, mitmproxy is my preferred choice. I guess it takes slightly longer to learn, but I think it's faster to use once you learn it.

To use mitmproxy to man-in-the-middle an https connection, you must tell the client to you are man-in-the-middling to trust a certificate generated at mitmproxy - this is located at `~/.mitmproxy/`.[^1]

---
[^1]: <https://docs.mitmproxy.org/stable/concepts-certificates/#the-mitmproxy-certificate-authority>
