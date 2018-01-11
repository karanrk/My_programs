import requests,json
import sys

def make_api_call(url,time):
	try:
		payload={'title':'Karan Testing','body':'This is a simple test','userId':101,'id':121}
		headers={'content-type':'application/json'}
		r=requests.post(url,data=json.dumps(payload),headers=headers)
		print "success with code",r.status_code
	
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



#client id-c358b65d5c674c3f8a9aa105e64fe57a
#client secret- d4022116bb794429b67cb92aea41403f





#access_token=5428220330.c358b65.91f56b3fe65b4d42805d3d577a5aca7c
	


