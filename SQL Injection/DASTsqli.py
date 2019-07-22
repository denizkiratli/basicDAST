import requests
import re

from colorama import init, Fore
init(autoreset=True)

print ('\n')

site = input('Enter the site: ')
site = site.rstrip(' ')

loginsite = input('Enter the login site: ')
loginsite = loginsite.rstrip(' ')

#listnum = input('Enter list number: ')
#listnum = listnum.rstrip(' ')

loginpay = {'username': 'admin', 'password': 'password', 'Login': 'Login'}

print ('\n')

vultime = 0

parameters=[]
with open('params.txt','r') as i:
	for line in i:
		parameters.append(line.rstrip('\n'))

payloads=[]
with open('payloads.txt', 'r') as i:
    for line in i:
        payloads.append(line.rstrip('\n'))

with requests.Session() as s:
	s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"})
	s.cookies.update({'security': 'low', 'security_level': '0'})
	rl = s.get(loginsite)
	token = re.search("user_token'\s*value='(.*?)'", rl.text).group(1)	
	loginpay['user_token'] = token
	l = s.post(loginsite, data=loginpay)
	
	for param in parameters:
		count = 1
		for i, payload in enumerate(payloads):
			if(count<=len(payloads)):
				r1 = s.get(site, params={param:payloads[i], 'Submit':'Submit'})
				if count<len(payloads):
					r2 = s.get(site, params={param:payloads[i+1], 'Submit':'Submit'})
				
				if len(r1.content) != len(r2.content) or re.search('SQL syntax', r1.text):
					vultime = vultime + 1
					print (Fore.LIGHTRED_EX+'INJECTION FOUND!')
					print ('URL: '+r1.url)
					if r1.status_code == 200:
						print ('Status Code: '+Fore.LIGHTGREEN_EX+str(r1.status_code))
					else:
						print ('CHECK STATUS!')
						print ('Status Code: '+Fore.LIGHTYELLOW_EX+str(r1.status_code))
					input ('Press Enter to continue')
					print ('\n')
				
				else:
					print ('URL: '+r1.url)
					if r1.status_code == 200:
						print ('Status Code: '+Fore.LIGHTGREEN_EX+str(r1.status_code))
					else:
						print ('CHECK STATUS!')
						print ('Status Code: '+Fore.LIGHTYELLOW_EX+str(r1.status_code))
						input ('Press Enter to continue')
					print ('\n')

				count = count+1

print ('Vulnerabilities run '+str(vultime)+' times')