import requests,json
import sys


def make_api_call(url,time):

	try:
		r=requests.get(url,timeout=time)
		r.raise_for_status()
		print "Body--->"+r.json()['body']
		print "User Id-->"+str(r.json()['userId'])
		print "Title -->"+str(r.json()['title'])
		if r.status_code != 200:
		#raise ApiError('GET /timeline {}'.format(r.status_code))
			print r.status_code

	except requests.exceptions.Timeout as t:
		print "Timeout Error" +str(t)
		sys.exit(1)

	except requests.exceptions.HTTPError as ht:
		print "HTTP Error" +str(ht)
		sys.exit(1)
	except requests.exceptions.TooManyRedirects as tm:
		print "Too Many redirects"+ str(tm)
		sys.exit(1)
	except requests.exceptions.ConnectionError as ce:

		print "ConnectionError" + str(ce)
		sys.exit(1) 

	except requests.exceptions.RequestException as re:
		print "Request exception" + str(re)
		sys.exit(1)

	

	

if __name__ == '__main__':

	make_api_call(str(sys.argv[1]),3)
