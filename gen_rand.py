import random as rn
import sys
import os

##filename finalno total_nos_to_gen
def gen_write(file_name, final_no, tot_nos_to_gen):
	l=[]
	s = ""
	for i in range(0, tot_nos_to_gen):
		l.append(int(rn.randint(0,final_no)))
		s+=str(l[i])+" "
	s=s[0:len(s)-1]
	s+="\n"
	os.system("touch input_files/"+file_name)
	file_name = "input_files/"+file_name
	f = open(file_name,"w")
	f.write(s)
	f.close()

#gen_write(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))

file_name_base="inp_"
for i in range(1,11):
	file_name = file_name_base+str(10)+"_"+str(i*10)+".txt"
	gen_write(file_name,10,i*10)

file_name="inp_100_1000.txt"
gen_write(file_name,100,1000)


file_name="inp_1000_10000.txt"
gen_write(file_name,1000,10000)

file_name="inp_10000_100000.txt"
gen_write(file_name,10000,100000)

file_name="inp_100000_1000000.txt"
gen_write(file_name,100000,1000000)


for i in range(1,11):
	file_name = file_name_base+str(10)+"_"+str(i*10)+".txt"
	gen_write(file_name,10,i*10)
