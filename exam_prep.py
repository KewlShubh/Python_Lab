'''

def my_gen():
	n=1
	print("This is printed first")
	yield n

	n+=1
	print("this is printed second")
	yield n

a=my_gen()
for i in a:
	print(i)

'''

#Prime Function using generators
'''
def prime(m):
	i=2
	while m%i!=0:
		i+=1
	return i==m	

def gen():
	yield 2
	yield 3
	m = 5
	while True:
		if prime(m) :
			yield m
		m += 1
g = gen()
# get next n primes
n = 10
for i in range(n):
	print(next(g))
'''

'''
from functools import reduce
a=[1,333,4,5,6,7,8]

c=reduce(lambda x,y: x if x>=y else y,a)
print(c)	
'''

'''
import functools
names = [ 'nagabhushana', 'satya', 'kumar' ]
#names = [ 'amar', 'bharatha', 'chandra', 'deepa', 'eshwara']
# output : nsk
print(functools.reduce(lambda x, y : x+y[0], names,""))
'''

'''
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)] 
res=[[i[0] for i in test_list],[i[1] for i in test_list]]
print(res)
tes = list(zip(*test_list))
print(tes)
'''

'''
class MyException(Exception):
	def __init__(self, str):
		self.str = str
	def __str__(self):
		return self.str
# check whether n is between 1 and 100
n = 105
try:
	if not 1 <= n <= 100 :
		raise MyException("number not in range")
	print("number is fine : ", n)
except MyException as e:
		print(e)
print("thats all")

'''

'''
def gen(n):
	i=0
	while True:
		i+=n
		if i%10==0:
			yield i
g = gen(5)
for i in range(5):
	print(next(g)," ")
'''

'''
marks=[{'math':90,'chem':45},{'math':45,'chem':56}]
print(sorted(marks,key=lambda x:x['chem'],reverse=True))
'''

'''
a=['Hello World','Ricky Martin']
f=[c.split(" ")[0][0] + c.split(" ")[1][0] for c in a]
print(f)

from random import randint as r
print(r(0,5))
'''

a=[1,2,3]
print(a.index(50))
