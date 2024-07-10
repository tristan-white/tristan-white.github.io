---
layout: post
title: firmware exfiltration
category: computer
---
I started learning about hardware hacking about a year ago. One topic I've found interesting is firmware extraction. I bought a router from Goodwill to practice ripping firmware off it, but found that there weren't a lot of videos online about how extracting firmware from start to finish. Additionally, I couldn't find any information about exfiltrating data over ethernet (which is about 1000x faster than over UART), so I made a video showing how to do it. Here it is, along with a outline for the entire process. Hope it helps!

<iframe width="560" height="315" src="https://www.youtube.com/embed/fxTVpxTXwBg?si=ROyE5Ow0d0kQAK47" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

## Outline

1. Is the firmware available online? Sometimes you can simply download the firmware from the manufacturer’s website. Google the name of the router to check.
    1. Additionally, it’s helpful to know that if the router has an FCC ID printed on the label, you can look up the ID on [fccid.io](http://fccid.io) to find lot of info about the router. Sometimes you can even find pictures of the internal chips on the PCB (Printed Circuit Board).
2. Take apart the router
    1. Screws may be hidden under labels or rubber feet on the router.
3. Determine if the PCB has a UART header; using UART to extract firmware will be easier than other potential options (JTAG, SPI flash, NAND flash, etc). 
    1. Tips for finding a UART header:
        1. Sometimes you’ll just find the word “UART” printed next to some pins. Easy.
        2. Other times you may find some pins labeled “TX” and “RX”. These may also be accompanied by pins labeled “GND” or “3.3V”. These are strong indications that you may have found UART pins.
        3. Don’t see any labels on the PCB? Examine the chips on the board and look up their serial numbers (printed on the chips) to find their datasheets online. There will probably be one central microcontroller on the board. Look at the pinout of that chip in its datasheet. Does the microcontroller support UART (ie, does the pinout in the datasheet show a RX and TX pin)?
            1. If not, tough luck. There might not be any UART interface on this board.
    2. If there are UART pins, try visually examining the board to see where the pins go. You may be able to follow them to some pins. If there aren’t pins but there is a header, you may want to solder pins onto the header in order to make attaching the USB to Serial Adapter to the PCB an easier process. 
    3. It could be that the pin out doesn’t lead anywhere (ie those pins are not used by any other component on the board). In this case, you may still be able to use micro grabbers to attach directly to a pin on the PCB.
    4. Use jumper cables to attach the pins to a USB to Serial Adapter.
    5. Determine the baud rate of the UART interface.
        1. You could guess the baud rate using [common baud rates](https://lucidar.me/en/serialib/most-used-baud-rates-table/) or use the baudrate.py tool.
    6. Use a command line tool such as [screen](https://linux.die.net/man/1/screen) on linux or [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/) on Windows to open a terminal to read/write to the UART shell on the router.
        1. If you use PuTTY, you’ll need to know which COM port your adapter is using. You can check in Device Manager.
        2. On linux, you’ll need to know which device your system is using to interface with your adapter. It’s probably `/dev/ttyUSB0` . Try using `ls /dev/ttyUSB*` before plugging your adapter into your host computer, then run the command again after plugging it in to see which device was added.
    7. Find the location of the root filesystem.
        1. `cat /proc/mtd` should output information that reveals the location of rootfs
    8. Look around the filesystem exposed by the UART shell. Are there any binaries that you may be able to use to exfiltrate the firmware over ethernet?
        1. [tftp](https://linux.die.net/man/1/tftp)? [nc](https://linux.die.net/man/1/nc)? If so, go ahead and and use those. Exfiltrating a file over ethernet will be wayyy faster than doing it over UART.
    9. Is there a hexdump utility on the embedded system?
        1. If yes, use hexdump to dump the rootfs over UART. Make sure you CLI tool used for interfacing with the UART shell (in my case `screen` ) is logging output to a file. `screen` can do this with `-L` . Once complete, open the log file with the hexdump and delete any part of the log that wasn’t part of the hexdump (eg the line where you executed the hexdump command). Use `xxd -r` to convert the hex dump on your host computer back into the original binary.
        2. If not, you may be able to write a simple bash script to do a hexdump.
    10. File system too large? Don’t want to wait hours for the file system to get hex dumped over UART? See the technique at the end of my video to write a custom binary that dumps the file system over ethernet.
4. What if your embedded system doesn’t have UART? You still have a number of a options.
    1. Find the flash chip on which the firmware is stored, then use an EPROM programmer to read the data off it. This [video](https://www.youtube.com/watch?v=tVJ78gOnRl8&pp=ygUmbWF0dCBicm93bmNoaXAgb2ZmIGZpcm13YXJlIGV4dHJhY3Rpb24%3D) shows the whole process. If you’re interested in buying a programmer but aren’t sure which to buy, I’d recommend watching [this video](https://www.youtube.com/watch?v=42VCmOVWAyc) which I found to be informative.
    2. Firmware on a NOR flash chip? Read it using SPI. Check out [this in depth video](https://www.youtube.com/watch?v=nruUuDalNR0&pp=ygUNc3BpIG5vciBmbGFzaA%3D%3D) from the Flashback Team.

