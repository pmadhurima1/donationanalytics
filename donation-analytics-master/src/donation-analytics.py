#! python
import sys
import string
import math  
import os.path

from validate import checkID,checkName,checkDate,checkZip,checkAmount,checkNull
ALLOWED = frozenset(string.ascii_letters + string.digits)
dictusers = {};

my_path = os.path.abspath(os.path.dirname(__file__))
outputpath = os.path.join(my_path, "./../output/repeat_donors.txt")
file = open(outputpath,"w")
ppath =os.path.join(my_path, "./../input/percentile.txt")
pfile = open(ppath,"r")
per=int(pfile.read()); 
itpath=os.path.join(my_path, "./../input/itcont.txt")
with open(itpath) as f:
    for line in f:
		words = line.split("|")  
		
		flag=True;
		if(checkNull(words[15])==False):
			if(checkID(words[0]) and checkName(words[7]) and checkDate(words[13]) and checkZip(words[10]) and checkAmount(words[14])):	
				flag =True;
			else :
				flag =False;
		# checkID(words[0])    #id
		# checkName(words[7])  #name
		# checkDate(words[13]) #date
		# checkZip(words[10])  #zip 
		# checkAmount(words[14])#money
		# checkNull(words[15]) #individual payer null 
		#print (words)	
		#print ( flag) 
		line1="";
		if flag==True:
			id=words[0];
			zip=words[10];	
			year=words[13];
			did=id[0:5]+zip[0:5]
			#print(did);
			
			val=dictusers.get(did,[-2]);             # default value set -2

			#print ("++\n"+str(val))
			if(val[0]<0):                            #increase val[0] ..waiting for first occurence to pass
				val[0]=val[0]+1;		
			else:   					 
				if(val[0]==0):			 # second occurance, reset val list	                    
					val=[];
				val.append(int(words[14]))
				val.sort();
				pindex=int(math.ceil(len(val)*30/100))
				line1=id+"|"+zip[0:5]+"|"+year[4:9]+"|"+str(val[pindex])+"|"+str(sum(val))+"|"+str(len(val))
				file.write(line1+"\n") 
			dictusers[did]=val;	
#print(dictusers)
file.close() 
pfile.close()
f.close()
