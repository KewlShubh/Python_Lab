#List Comprehension:

# Convert one list from another list using the iterables
# new_list=[expression for member in iterable if conditional]

#Question: Make a list of squares of numbers using list comprehension
'''
x=[c**2 for c in range(5)]
print(x)
'''

#Question: Print list of strings having length greater than 5
'''
li=['Shubh','Vini','Sreeee','Shubhankar','Bengaluru']
x=[c for c in li if len(c)>5]
print(x)
'''

#Question : Print list of strings having length greater than 5 with the length size
'''
li=['Shubh','Vini','Sreeee','Shubhankar','Bengaluru']
x=[(c,len(c)) for c in li if len(c)>5]
print(x)
'''

#Question: Make a list of squares of even natural numbers 
'''
x=[c**2 for c in range(10) if c%2==0]
print(x)
'''

#Question: Make a list of squares of numbers divisible by 2 and 3
'''
x=[c**2 for c in range(10) if c%2==0 and c%3==0]
print(x)
'''


li=['Shubh','Vini','Sreeee','Shubhankar','Bengaluru']
l=[1,2,3,4,5]
x={liq:lw for liq in li for lw in l if len(liq)>5}
print(x)

x={i:j for (i,j) in zip(li,l)}
print(x)
