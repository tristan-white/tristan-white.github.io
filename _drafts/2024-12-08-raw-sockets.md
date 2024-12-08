---
layout: post
title: Raw Sockets
description: Tips for using raw sockets in C.
image: https://images.unsplash.com/photo-1581619971320-0e278e5971a0?q=80&w=2207&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
tag: [coding]
---

I began learning about raw sockets in C recently. Here's a simple raw socket proram in C with comments explaning what's going on.

<script src="https://gist.github.com/tristan-white/f0712db5aa449dd4c655c1f6163f74bd.js"></script>

### Resources

If you're new to C socket programming, I would highly reccomend [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/).

To learn more about raw socket programing, read these man pages:
- [man 7 ip](https://www.man7.org/linux/man-pages/man7/ip.7.html)
- [man packet](https://www.man7.org/linux/man-pages/man7/packet.7.html)