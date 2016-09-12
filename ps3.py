###### this is the third .py file ###########



#database
state={"AP":'000',"DELHI":'001',"MAHARASTRA":'010'}
city={"ROORKEE":'111',"KANPUR":'110',"NEWDELHI":'101'}
district={"NIT":'000',"IIT ROORKEE":'001',"IIT DEHLI":'010'}


print "1.add 2.modify 3.delete"
choice=input("enter the operation you want to perform")
#add block
if choice==1:
	st=raw_input("enter the state ")
	cd=raw_input("enter the code ")
	state.update({st:cd})
	st1=raw_input("enter the city ")
	cd1=raw_input("enter the code ")
	city.update({st1:cd1})
	st2=raw_input("enter the district")
	cd2=raw_input("enter the code")
	district.update({st2:cd2})
	

#modify block
if choice==2:
	st=raw_input("enter the state to modify\n")
	cd=raw_input("enter the new code\n")
	if st in state.keys():
		state.update({st:cd})
	else :
		print 'invalid state'
	st1=raw_input("enter the district to modify\n")
	cd1=raw_input("enter the new code\n")
	if st1 in district.keys():
		district.update({st1:cd1})
	else :
		print 'invalid district'
	st2=raw_input("enter the city to modify\n")
	cd2=raw_input("enter the new code\n")
	if st2 in city.keys():
		city.update({st2:cd2})
	else :
		print 'invalid city'


#Delete block
if choice==3:	
	st=raw_input("enter state  to delete\n")
	if st in state.keys():	
		del state[b]
	else :
		print "invalid key"
	ci=raw_input("enter the city delete\n")
	if ci in city.keys():	
		del city[b]
	else :
		print "invalid key" 
	dt=raw_input("enter the district delete\n")
	if dt in district.keys():	
		del district[b]
	else :
		print "Invalid key"

#query block
else :
	l1=raw_input("customer name\n")
	l2=raw_input("customer district\n")
	l3=raw_input("customer city\n")
	l4=raw_input("customer state\n")
	if l4 in state.keys():
		print "CC_NO = ",state.get(l4,"None")
	if l2 in district.keys():
		print district.get(l2, "None")
	if l3 in city.keys():
		print city.get(l3, "None")
	
	
print state	
	
