import socket
import sys
import time
import requests, builtwith
import os
import ipapi
import json
from colorama import Fore
search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']


def __start__():
    print(""" [!] Please Enter The Target Website Address\n""")
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"inquisitio"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Bypass-CloudFlare"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    print("""\n\n [!] 1. Bypass Cloud Fare\n""") 
    cloudfare(site)
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 2. CMS Detect\n""")
    cms(site)
    print(Fore.CYAN+"  \n\n**********************\n\n")
    print(""" [!] 3. Trace route\n""")
    tr(site)
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 4. Reverse IP \n""")
    reverseIP(site)
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 5. Port Scan\n""")
    portscan(site) 
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 6. IP Location Finder\n""") 
    #iplocation()  
    #print(Fore.CYAN+"  \n\n**********************\n\n") 
    #print(""" [!] 7. Show HTTP Header\n""")
    httpheader(site) 
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 8. Find Shared DNS\n""")
    findshareddns(site)
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 9. Whois\n""")
    whois(site)    
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 10. DNS Lookup\n""")
    dnslookup(site)    
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    print(""" [!] 11. Robot Scanner\n""")
    robot(site)    
    print(Fore.CYAN+"  \n\n**********************\n\n") 
    try:
         input(Fore.RED+" [!] "+Fore.GREEN+"\nBack To Menu (Press Enter...) ")
    except:
         print("")
         sys.exit()  
         print("\nExit :)")

def cloudfare(site):
	print(""" [!] Welcome To The Cloudflare Bypasser Part\n""")
	subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
	if site == "":
        	try:
            		print(Fore.RED+" [!] "+Fore.BLUE+"Please Enter Address :) \n")
            		time.sleep(5)
            		sys.exit()
        	except:
            		return
	for sub in subdom:
        		try:
            			hosts = str(sub) + "." + str(site)
            			bypass = socket.gethostbyname(str(hosts))
            			#print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            			print (" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
        		except Exception:
            			pass

def cms(site):
    if not 'https://' in site or not 'http://' in site:
        site = 'http://'+site
    info = builtwith.parse(site)
    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
        print(Fore.BLUE+"\n"+name+': '+value)
    
def tr(site):
	result = requests.get('https://api.hackertarget.com/mtr/?q=' + site).text
	print(Fore.YELLOW+result)
def reverseIP(site):
	mysite = {"remoteAddress":site}
	link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)
	source = json.loads(link.content)
	print(source)
	for data in source["domainArray"]:
		print(" "+data[0]+"\n")
def portscan(site):
	result = requests.get('https://api.hackertarget.com/nmap/?q=' + site).text
	print(Fore.YELLOW+result)
def iplocation():
	print(Fore.RED+"\n [!] Enter IP Address")
	site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Location"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
	source = ipapi.location(ip=site, key=None, field=None)
	try:
		print(Fore.GREEN+" [!]"+Fore.RED+" See your info")
		print (Fore.GREEN+" [!]"+Fore.BLUE+" ip = "+ source["ip"])
		print (Fore.GREEN+" [!]"+Fore.YELLOW+" city = " + source["city"])
		print (Fore.GREEN+" [!]"+Fore.RED+" region = "+ source["region"])
		print (Fore.GREEN+" [!]"+Fore.MAGENTA+" id country = "+source["country"])
		print (Fore.GREEN+" [!]"+Fore.WHITE+" country = "+ source["country_name"])
		print (Fore.GREEN+" [!]"+Fore.CYAN+" Calling Code = "+source["country_calling_code"])
		print (Fore.GREEN+" [!]"+Fore.GREEN+" Languages = "+source["languages"])
		print (Fore.GREEN+" [!]"+Fore.BLUE+" org = "+ source["org"])
	except:
		print(Fore.RED+"Sorry Please Enter an IP Address")
def httpheader(site):
	result = requests.get('https://api.hackertarget.com/httpheaders/?q=' + site).text
	print(Fore.YELLOW+result)
def findshareddns(site):
	result = requests.get('https://api.hackertarget.com/findshareddns/?q=' + site).text
	print(Fore.BLUE+result)
def whois(site):
	result = requests.get('http://api.hackertarget.com/whois/?q=' + site).text
	print(Fore.YELLOW+result)
def dnslookup(site):
	result = requests.get('http://api.hackertarget.com/dnslookup/?q=' + site).text
	print(Fore.BLUE+result)
def robot(site):
	url = site
	if 'http' in url:
		pass
	elif 'http' != url:
		url = ('http://'+url)            
	for i in search:
		time.sleep(0.1)
		ur = (url+"/"+i)
		"http://pythons.ir/robots.txt"
		reqs = requests.get(ur)
		if reqs.status_code == 200 or reqs.status_code == 405:
			print(Fore.YELLOW+" [+] "+ ur)
		else:
			print(Fore.CYAN+" [-] "+ur)

