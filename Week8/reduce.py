#format: reduce(function,iterable[,start_value])
#Note: reduce returns a single value
# reduce function needs to be imported from functools library


'''
a=[1,2,3,4,5]
from functools import reduce

x=reduce(int.__add__,a,0)
print(x)
#print(dir(int))
print(int.__add__(3,4))
'''

#Q: input is a list of strings, ouput should be one string
'''
a=['I','Am','A','Good','Boy']
from functools import reduce
q=reduce(lambda a,b:(a+' '+b),a)
print(q)

'''
# Question using Data Set
'''
l=[1,2,3]
m=['shubh','vini','sree']
n=[23,34,56]
a=zip(l,m,n)		#Using zip function
print(list(a))
'''

#Question: Find maximum from a list
'''
l=[1,2,3,4,5]
from functools import reduce
y = reduce(lambda x,y:x if x>y else y,l)
print(y)
'''

#Question: Find factorial
from functools import reduce
y=reduce(lambda x,y:x*y,range(1,int(input())+1))
print(y)
