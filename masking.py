import re
#from collections import Counter
import sys

def find_num(log):
	with open(log) as f:
		l=f.read()
		my_reg=r'[\+]?\d{1,2}[\s\(]*\d{3}[\)-.\s]*\d{3}[\s.-]*\d{4}' 
		phone_list=re.findall(my_reg,l)
		return phone_list

def mask(plist):
	m_reg="(.*)(\d{4})$" #create groups that can be divided for masking
	for i in plist:
		maskp,publicp=re.match(m_reg,i).groups()
		#print 'public'+publicp

		print re.sub('\d','*',maskp)+publicp
	
	
		





if __name__ == '__main__':
	pl=find_num(sys.argv[1])
	mask(pl)



