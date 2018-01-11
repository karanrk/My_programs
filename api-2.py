import requests,json
import sys

def make_api_call(url,time):
	try:
		payload={'id':'121'}
		r=requests.get(url,timeout=time,params=payload)
		r.raise_for_status()
		#print 'url-->',r.url()
		print r.json()
		print r.status_code

	except requests.exceptions.HTTPError as ht:
		print "Http Error",ht
		sys.exit(1)

	except requests.exceptions.TooManyRedirects as tm:
		print "Too many redirects",tm
		sys.exit(1)

	except requests.exceptions.ConnectionError as ce:
		print "Connection error",ce
		sys.exit(1)

	except requests.exceptions.Timeout as t:
		print "Timeout",t
		sys.exit(1)

	except requests.exceptions.RequestException as re:
		print "request excetions",re
		sys.exit(1)

	
if __name__ == '__main__':
	make_api_call(sys.argv[1],3)	
	
	


