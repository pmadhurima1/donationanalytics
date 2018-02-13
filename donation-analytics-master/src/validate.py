from datetime import datetime
def checkID(mystring):
	flag =True;
	if (len(mystring)<9):
		flag =False;
	if (flag==True):
		flag=mystring.isalnum();
	return flag;
	
def checkName(mystring):
	flag =True;
	mystring.replace(',',' ')
	if (len(mystring)==0):
		flag =False;
	#if (flag==True):
	#	flag=mystring.isalnum() or mystring.isspace() ;
	return flag;
	
	
def checkDate(date_text):
	flag=True;
	try:
		datetime.strptime(date_text, '%m%d%Y')
	except ValueError:
		flag=False;
	return flag;	
	
def checkZip(mystring):
	flag =True;
	if (len(mystring)<5):
		flag =False;
	if (flag==True):
		flag=mystring.isdigit();
	return flag;
	
def checkAmount(mystring):
	flag =True;
	if (flag==True):
		flag=mystring.isdigit();
	return flag;
	
	
def checkNull(mystring):
	return bool(mystring.strip());	