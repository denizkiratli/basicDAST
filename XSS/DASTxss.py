import requests

from colorama import init, Fore
init(autoreset=True)

print ('\n')

site = input('Enter the site: ')
site = site.rstrip(' ')

listnum = input('Enter list number: ')
listnum = listnum.rstrip(' ')

ans = input('With parameter or not (y or n): ')

print ('\n')

vultime = 0

if ans == 'y':
	parameters=[]
	with open('params.txt','r') as i:
		for line in i:
			parameters.append(line.rstrip('\n'))

payloads=[]
with open('xsspayload' + listnum + '.txt', 'r') as i:
    for line in i:
        payloads.append(line.rstrip('\n'))

if ans == 'n':
	for payload in payloads:
		siteparam = site + payload
		r = requests.get(siteparam)
		if payload in r.text:
			vultime = vultime + 1
			print (Fore.LIGHTRED_EX+'PAYLOAD FOUND!')
			print ('URL: '+r.url)
			if r.status_code == 200:
				print ('Status Code: '+Fore.LIGHTGREEN_EX+str(r.status_code))
			else:
				print ('CHECK STATUS!')
				print ('Status Code: '+Fore.LIGHTYELLOW_EX+str(r.status_code))
			restxt = r.text.rsplit('\n')
			for line in restxt:
				if payload in line:
					print ('In line '+Fore.LIGHTCYAN_EX+str(restxt.index(line)+1)+Fore.RESET+' - '+line+'\n')
			input ('Press Enter to continue')
			print ('\n')
		else:
			print ('URL: '+r.url)
			if r.status_code == 200:
				print ('Status Code: '+Fore.LIGHTGREEN_EX+str(r.status_code))
			else:
				print ('CHECK STATUS!')
				print ('Status Code: '+Fore.LIGHTYELLOW_EX+str(r.status_code))
				input ('Press Enter to continue')
			print ('\n')
			
else:
	for param in parameters:
		for payload in payloads:
			r = requests.get(site, params= {param:payload})
			if payload in r.text:
				vultime = vultime + 1
				print (Fore.LIGHTRED_EX+'PAYLOAD FOUND!')
				print ('URL: '+r.url)
				if r.status_code == 200:
					print ('Status Code: '+Fore.LIGHTGREEN_EX+str(r.status_code))
				else:
					print ('CHECK STATUS!')
					print ('Status Code: '+Fore.LIGHTYELLOW_EX+str(r.status_code))
				restxt = r.text.rsplit('\n')
				for line in restxt:
					if payload in line:
						print ('In line '+Fore.LIGHTCYAN_EX+str(restxt.index(line)+1)+Fore.RESET+' - '+line+'\n')
				input ('Press Enter to continue')
				print ('\n')
			else:
				print ('URL: '+r.url)
				if r.status_code == 200:
					print ('Status Code: '+Fore.LIGHTGREEN_EX+str(r.status_code))
				else:
					print ('CHECK STATUS!')
					print ('Status Code: '+Fore.LIGHTYELLOW_EX+str(r.status_code))
					input ('Press Enter to continue')
				print ('\n')
				
print ('Vulnerabilities run '+str(vultime)+' times')