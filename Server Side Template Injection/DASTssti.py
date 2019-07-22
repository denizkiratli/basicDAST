import requests
from colorama import init, Fore
init(autoreset=True)

print ('\n')

site = input('Enter the site: ')
site = site.rstrip(' ')

print ('\n')

vultime = 0

parameters=[]
with open('params.txt','r') as i:
    for line in i:
        parameters.append(line.rstrip('\n'))

for parameter in parameters:
    r = requests.get(site, params={parameter:'{{3586*1}}'})
    if '3586' in r.text:
        vultime = vultime + 1
        print (Fore.LIGHTRED_EX+'INJECTION FOUND!')
        print ('URL: '+r.url)
        if r.status_code == 200:
            print ('Status Code: '+Fore.LIGHTGREEN_EX+str(r.status_code))
        else:
            print ('CHECK STATUS!')
            print ('Status Code: '+Fore.LIGHTYELLOW_EX+str(r.status_code))
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