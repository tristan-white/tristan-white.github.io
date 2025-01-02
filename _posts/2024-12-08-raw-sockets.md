---
layout: post
title: Raw Sockets
description: Tips for using raw sockets in C.
image: https://images.unsplash.com/photo-1581619971320-0e278e5971a0?q=80&w=2207&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
tag: [coding]
---

I began learning about raw sockets in C recently. Here's a simple raw socket proram in C with comments explaning what's going on.

```c
/** This code shows how to create raw socket in C that listens for any
 * incoming packet of any protocol. Comments added anywhere someone 
 * familiar with C socket programming (but not raw sockets) may have
 * questions.
 * 
 * Assumes you're already familiar with
 * socket programming. For info/intro on socket programming, check out:
 * https://beej.us/guide/bgnet/
 * 
 * Reccomended reading for raw socket programming:
 * - man 7 ip
 * - man packet
 * 
 * The _DEFAULT_SOURCE macro help vscode's intellisense work properly;
 * very handy when working with large struct in network programming.
 * See https://stackoverflow.com/questions/74823127/vscode-c-c-intellisense-issue-with-netinet-ip-h
 */
#ifndef _DEFAULT_SOURCE
#define _DEFAULT_SOURCE
#endif // _DEFAULT_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/ether.h>
#include <sys/socket.h>
#include <net/ethernet.h>
#include <netpacket/packet.h>

void print_packet_info(const unsigned char *packet, int packet_len) {
    // struct ether_header defined in <netinet/ethernet.h>
    struct ether_header *eth_header = (struct ether_header *)packet;
    // struct ip defined in <netinet/ip.h>

    struct ip *ip_header; // newer version of up struct is the iphdr struct

    // Print MAC addresses
    printf("Source MAC: %s\n", ether_ntoa((struct ether_addr *)eth_header->ether_shost));
    printf("Destination MAC: %s\n", ether_ntoa((struct ether_addr *)eth_header->ether_dhost));

    // Check if the packet is an IP packet
    if (ntohs(eth_header->ether_type) == ETHERTYPE_IP) {
        ip_header = (struct ip *)(packet + sizeof(struct ether_header));
        printf("Source IP: %s\n", inet_ntoa(ip_header->ip_src));
        printf("Destination IP: %s\n", inet_ntoa(ip_header->ip_dst));
    }

    printf("\n");
}

int main() {
    int sock;
    struct sockaddr saddr;
    int saddr_len = sizeof(saddr);
    unsigned char buffer[65536]; // Buffer to hold the packet

    /** Create a raw socket. 
     * `man packet` has helpful info about these socket() params
     * 
     * AF_PACKET:   Specifices socket will be raw.
     * SOCK_RAW:    Packets are not changed before receipt (eg stripped of
     *              link layer header).
     * ETH_P_ALL:   Specifies that all protocols should be received on this
     *              socket (not just UDP, TCP, etc)
     */
    sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (sock < 0) {
        perror("Socket creation failed");
        return 1;
    }

    // Listen for incoming packets
    while (1) {
        int packet_len = recvfrom(sock, buffer, 65536, 0, &saddr, (socklen_t *)&saddr_len);
        if (packet_len < 0) {
            perror("Packet receive failed");
            close(sock);
            return 1;
        }
        print_packet_info(buffer, packet_len);
    }

    // Cleanup
    close(sock);
    return 0;
}
```

### Resources

If you're new to C socket programming, I would highly reccomend [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/).

To learn more about raw socket programing, read these man pages:
- [man 7 ip](https://www.man7.org/linux/man-pages/man7/ip.7.html)
- [man packet](https://www.man7.org/linux/man-pages/man7/packet.7.html)