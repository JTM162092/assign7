###### this is the first .py file ###########
####### write your code here ##########
###Reading inputs and spiliting fields
inp=raw_input()
inp2=inp.split( );
l=len(inp)

#blank string
default_d={}


#crating dictionary
for i in inp2:
	p=inp2.count(i)
	default_d.update({i: p})


#sorting the string accroding to values
out= sorted(default_d.iteritems(), key=lambda x:-x[1])[:3]
for field in out :
	print "{0}: {1}".format(*field)



##permutation program

from itertools import permutations
for i in inp2:
	z=len(i)
	if(z<=1):
		print i
	else:
		iteration = [''.join(pic) for pic in permutations(i)]
		print iteration[1]
