
'''
def primeno(n):
    se = set(range(2,n+1))
    prime=[]
    while se:
        a=min(se)
        prime.append(a)
        se = se - set(range(a,n+1,a))
    return (prime)
n=int(input('Enter the end limit:'))
s=primeno(n)
print(s)
'''

'''
print('2.a>')
def rev(s1): #Function definition
 if len(s1)==0: #Default condition
  return s1
 else:
  return rev(s1[1:]) + s1[0] #Recursion statement
s=input("Enter the string to be reversed: ")
print(rev(s))

print('2.b>')
def tower(n,s,d,aux): #Function definition
 if n==1: #Move only one disk at once
  print('Move disk',n,'from',s,'to',d)
  return
 tower(n-1,s,aux,d)
 print('Move disk',n,'from',s,'to',d)
 tower(n-1,aux,d,s)
n=int(input('Enter the number of disks \n'))
tower(n,'Source','Destination','Auxillary')

print('2.c>')
def exp(a,b): #Function definition
 if b==0: #Number power zero is 1
  return 1
 elif a==1: #Number power one is number itself
  return 1
 else:
  return a*exp(a,b-1) #Recursion statement
x=int(input("Enter number to raise to power :\n"))
y=int(input("Enter the power to be raised to :\n"))
print('Ans',exp(x,y))
'''

'''
def Sum(n): #Function to find sum of numbers upto n 
 sum=0
 for i in range(n+1):
  sum+=i
 print('Sum of numbers upto',n,'is',sum)
def Double(n): #Function to find double
 print('Double of',n,'is',2*n)
def Triple(n): #Function to find triple
 print('Triple of',n,'is',3*n)
def Calc(n,f): #Function that acts as a callable
 f(n)
n=int(input('Enter the number: \n'))
Calc(n,Sum) #Callabe-1
Calc(n,Double) #Callabe-2
Calc(n,Triple) #Callable-3
'''

'''
print('4a>')
def outer(n):
    def inner():            #Condtion-1 for implementing closure
        num=5
        for i in range(n):
            print(num)
            num+=5          #Number added iteratively by 5
        return inner        #Condtion-2 for implementing closure
n=int(input('Enter the number: '))
fn=outer(n)  
fn()


print('4b>') 
def outer(n,r): 
 def inner(): #Condtion-1 for implementing closure
  print('Root: ',n**(1/r))
 return inner #Condtion-2 for implementing closure
n=int(input('Enter the base :\n')) #Input base
r=int(input('Enter the nth root :\n')) #Input nth root
fn=outer(n,r)
fn()
'''

'''
def fib(n): #Function to find nth fibonacci number
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def call(fn): #Callback
    def display(n): #Closure
        return fn(n)
    return display
f=call(fib)
n=int(input('Enter the term: \n'))
print('nth fibonacci number: ',f(n))
'''

import socket
import sys
import time
x=socket.socket()
h_name= input(str(" Enter the hostname of the server"))
port = 8080
x.connect((h_name,port))
print("Connected to chat server")


