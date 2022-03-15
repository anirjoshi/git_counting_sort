from functools import reduce
import sys
import time

def csort(arry):
	time_st =time.time()
	arry_min=reduce(lambda x,y: min(x,y), arry)
	arry_max=reduce(lambda x,y: max(x,y), arry)
	counting_arr=[0]*(arry_max-arry_min+1)

	for i in arry:
		counting_arr[i-arry_min]+=1
	
	sorted_arry = []
	for i in range(0,len(counting_arr)):
		sorted_arry+=[i+arry_min]*counting_arr[i]

	#print(sorted_arry)
	time_end=time.time()
	return sorted_arry, time_end-time_st


def bsort(arry2):
	time_st =time.time()
	arry = arry2
	for i in range(0,len(arry)):
		for j in range(0, len(arry)-1):
			if(arry[j]>arry[j+1]):
				arry[j], arry[j+1] = arry[j+1], arry[j]

	time_end=time.time()
	return arry, time_end-time_st

def msort_caller(arry):
	time_st =time.time()
	sarry=msort(arry)
	time_end=time.time()
	return sarry, time_end-time_st

def msort(arry):
	sarry=arry
	if len(arry)==1:
		return arry
	else:
		mid = (0+len(arry))/2
		mid = int(max(mid,1))
		
		s1 = msort(arry[0:mid])
		s2 = msort(arry[mid:len(arry)])
		i=0
		j=0
		m_arry=[]
		while(i!=len(s1) and j!=len(s2)):
			if s1[i]>s2[j]:
				m_arry.append(s2[j])
				j+=1
			else:
				m_arry.append(s1[i])
				i+=1
		if i!=len(s1):
			m_arry+=s1[i:len(s1)]
		
		if j!=len(s2):
			m_arry+=s2[j:len(s2)]
			
		return m_arry
				
#print(sys.argv)
given_file=open(sys.argv[1],'r')
line = given_file.readlines()
l = line[0].strip("\n").split(" ")
l = list(map(lambda x: int(x), l))
#print(l) 
#l = [4,3,2,1,-1,-3]
print(csort(l.copy())[1],bsort(l.copy())[1],msort_caller(l.copy())[1],sys.argv[2],sep=", ")
#print()
#print()
