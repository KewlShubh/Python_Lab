'''
def my_gen():
 n = 1
 print('This is printed first')
 # Generator function contains yield statements
 yield n
 n += 1
 print('This is printed second')
 yield n
 n += 1
 print('This is printed at last')
 yield n
a = my_gen()

for i in a:
	print(i)


'''


'''
a=[[],[],[],[]]

for i in range(4):
	for j in range(4):
		if i==j:
			a[i].append(5)
		else:
			a[i].append(0)	

for i in a:
	print(i)

'''

'''
class MyContainer:
	def __init__(self,mylist):
		self.mylist=mylist

	def __iter__(self):
		self.i=0
		return self


	def __next__(self):
		self.i+=1
		if self.i<len(self.mylist):
			i=self.i
			return self.mylist[i]
		else:
			raise StopIteration()

A=["hello","welcome","to","the","world","of","Computers"]
C=MyContainer(A)
for w in C:
	print(w)		
'''
'''
import random

lst=['EC','MATH','STATICS','CS','CHEM']
print(random.choice(lst))


Sample space : 

CHEM: 1 1 1 1
MATH: 1
EC: 1 1
STATICS: 1
CS: 1 1 1 1 1 1 1
'''



from random import choice
a={'Shubh':0,'Sanju':0}

for i in range(76):
	c=choice(list(a.keys()))
	a[c]+=1
print(a)