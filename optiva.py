#!/usr/bin/env python
#
# Author  : Hackermachan
# Optiva-framework - Web application scanner
# insta   : sajuuz_5
# Channel ; https://youtu.be/Eo7-aXDp8C4
# Dont forget to subscribe 


#modules
import os
import sys
import time
import hashlib
import datetime
sys.path.append('core/')
from gost import *
from coder import *
from update import *
from banner import *
from command import *
sys.path.append('modules/')
from hashc import *
from hashk import * 
from hashm import * 
from hashs import *
from hashz import *
from xssy import *
from info import *
from sqldork import *
from adm import *
from who import *
from por import *
from rce import *
from sqll import *
from iplocator import *
from reverse import *
from header import *


try:
	from termcolor import colored, cprint

except ImportError as ie:
	print(str(ie))

def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass

class OptivaMain(object):
	   
	   def Hackermachan(self):
		__version__ = '1.0.4'
		__author__ = "Hackermachan"
		__Github__ = "https://github.com/Hackermachan2"
		__instagram__ = "sajuuz_5"
		__Channel__ = "https://youtu.be/Eo7-aXDp8C4"
		__youtube__ = 'dont forget to subscribe
		__date__ = datetime.datetime.now()
		__tools__ = "15"

                try:
		    github = raw_input("\n\033[92m[\033[91m0ptiva\033[92m]\033[93m$>")

		    if github == 'exit':
		    	print '\033[1;91mThanks for Usage \033[96mOptivaframework !'
		    	sys.exit(0)

		    if github == 'clear':
			    os.system('clear')
			    Banner()
			    GostBanner()
			    return Optiva.Hackermachan()

		    if github == 'version':
		    	os.system('clear')
		    	Banner()
		    	GostBanner()
		        print("\033[41mVersion: " + colored(__version__, 'white'))
		        return Optiva.Hackermachan()


		    if github == 'banner':
		         Banner()
		         GostBanner()
		         return Optiva.Hackermachan()

		    if github == 'xss':
				 xssvu()
				 return Optiva.Hackermachan()

		    if github == 'whois':
		    	 whois()
		    	 return Optiva.Hackermachan()

		    if github == 'iplocator':
		         iploc()
		         return Optiva.Hackermachan()

		    if github == 'dork':
		         sdork()
		         return Optiva.Hackermachan()

		    if github == 'rce':
		    	 rceScan()
		    	 return Optiva.Hackermachan()

		    if github == 'sql':
		         sqlvuln()
		         return Optiva.Hackermachan()

		    if github == 'info':
		         infor()
		         return Optiva.Hackermachan() 

		    if github == 'admin':
		         adminv()
		         return Optiva.Hackermachan()

		    if github == 'md5':
		    	 md5hash()
		    	 return Optiva.Hackermachan()

		    if github == 'sha1':
				 sha1hash()
				 return Optiva.Hackermachan()

		    if github == 'show modules':
			    modules()
			    return Optiva.Hackermachan()

		    if github == 'update':
		         Optivaf()
		         return Optiva.Hackermachan()


		    if github == 'SHA256':
				 SHA256hash()
				 return Optiva.Hackermachan()

		    if github == 'SHA384':
				 SHA384hash()
				 return Optiva.Hackermachan()

		    if github == 'SHA512':
				 SHA512hash()
				 return Optiva.Hackermachan()

		    if github == 'author':
			    Gostauto()
			    return Optiva.Hackermachan()

		    if github == 'help':
		    	cmd()
		    	return Optiva.Hackermachan()

		    elif github == 'port':
			    port()
			    return Optiva.Hackermachan()

		    elif github == 'reverse':
			    revip()
			    return Optiva.Hackermachan()

		    elif github == 'header':
			    head()
			    return Optiva.Hackermachan()

                except KeyboardInterrupt:
                        cprint("\n[!] You Press Ctrl + C! To Quit.", 'red')
                        sys.exit(1)

                except:
                        pass

def banner():
    Banner()
    GostBanner()


if __name__ == "__main__":
	Banner()
	GostBanner()
	Optiva = OptivaMain()
	Optiva.Hackermachan()
