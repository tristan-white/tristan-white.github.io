---
layout: post
title: 'Multicast DNS (mDNS)'
description: What it is and how to use it.
image: https://images.unsplash.com/photo-1520869562399-e772f042f422?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
tag: [network]
---

![](/assets/images/stream-icon.jpeg){: .right .w-50}
Have you ever watched a youtube video on your phone and seen button that allows you to stream to a TV on your local network? Your phone is able to "sense" that nearby TV because most smart TV broadcast an mDNS service discovery packet to the whole LAN periodically.

Multicast DNS[^1] (mDNS) and its companion technology DNS-Based Service Discovery[^2] (DNS-SD) were created to provide IP networking with ease-of-use and autoconfiguration.

AppleTalk was the first technology to popularize a similar networking solution that allowed devices to publish and discover services and host names to a LAN. In other words, mDNS functions like DNS[^3] but on a smaller scale and does not need a DNS server.

## How does it work?

When the manufacturer of a computer, IOT device, phone, or other device makes a new product, they may want to allow it to be easily discoverable by other devices on a local network. DNS-SD was created to solve this problem by creating a standard where devices can declare services or information about themselves to other devices on a LAN. Additonally, devices (such as a phone searching for a smart TV) can broadcast a "service discovery" packet. Any device with a service it would like to advertise can responde with another broadcasted packet. Devices on the LAN can cache these broadcasted packets for use later. 

## How do I view DNS?

On Debian systems, [avahi](https://avahi.org/) comes pre-installed as an `apt` package.

Here's how to use it:

```bash
# see help
avahi-browse -h

# dump database of common service types
avahi-browse -b

# see all the devices and services being broadcasted on your LAN
avahi-browse -a
```

Alternatively, you could use wireshark or `tcpdump` to view mDNS packets on your network; just listen on port 5353:

## How do I implement DNS progrmatically?

There are already some libraries for using/interacting with mDNS:
- C library: [https://github.com/mjansson/mdns](https://github.com/mjansson/mdns)
- Python library: [https://github.com/python-zeroconf/python-zeroconf](https://github.com/python-zeroconf/python-zeroconf)


---
[^1]: mDNS is defined in [RFC 6762](https://www.rfc-editor.org/rfc/rfc6762)
[^2]: DNS-SD is defined in [RFC 6763](https://www.rfc-editor.org/rfc/rfc6763)
[^3]: See [this document](https://courses.cs.duke.edu/fall16/compsci356/DNS/DNS-primer.pdf) for a good quick overview of DNS packets.