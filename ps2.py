###### this is the second .py file ###########

####### write your code here ##########

import random
user_count=0  
user_unit=0     

#number of users
for user_count in range(1,100):
	(X,Y)=(random.random()*2- 1, random.random()*2-1)
	user_count+=1
#no of user in unit circle	
	if((X**2+Y**2)<=1):
		user_unit+=1


percentage_user=(float(user_unit)/100)*100
print "Percentage of users around MSC within unit circle is %d" %percentage_user
