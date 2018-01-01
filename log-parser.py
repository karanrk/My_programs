import sys
import re
from collections import Counter

def parser(log):
	with open(log) as f:
		l=f.read()
		#print l
		#phone number regex
	
		#my_reg=re.compile(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})\s*$')
		
		#my_reg=re.compile(r'[\+\(]?(\d{1,2})?\)?[\(-.\s]?\d{3}[\)-. \s]?\d{3}[-.\s]?\d{4}') 
		
		#ip address regex
	
		my_reg=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
		iplist=re.findall(my_reg,l)
		ipcount=Counter(iplist)
		for i,j in ipcount.items():
			print ("The IP address -->"+str(i)+" Count-->"+str(j))
			

if __name__=='__main__':
	parser(sys.argv[1])
		
