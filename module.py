'''
modules-->user defined module-->create,accessing
built-in modules-->os,sys,random,math,pltform

a module is a python
'''
import my_module
print(dir(my_module)) #ude dir to get available methods and attributes
#acccessing from module
'''
print(my_module.greet("akshitha"))
#print(my_module.names)
#print(type(my_module.names))

my_module.names.update({'place':'hyd','age':7})
print(my_module.names)
print(type(my_module.display()))

#accessing methods/attributes using from keyword
from my_module import greet
print(greet("Agents"))
#print(names) #name error as we didnot import

from my_module import greet,names
print(greet('AAAI'))
print(names)
#print(display) #again it raises nameerror

#to access all methods/attributes we use*
#recommended only for userdefined/simple modules

from my_module import *
print(greet("Akshitha"))
names.update({'course':"AAAI"})
print(names)
#print(display())
y = display()
print(next(y))
print(__name__)
print(__doc__)
print(my_module.__name__)
print(my_module.__doc__)

#built-ins modules-->math,os,sys,random,json,collections,itertools
#math-->it has all mathematical constants,trignometric functions and basic math functions

import math
print(dir(math))
print(math.__doc__) #it gives description about the module
print(math.ceil(2.1)) #it returns the next higher value-->int
print(math.floor(2.9)) #it returns the lower value of given value-->int
print(math.e) #returns exponential value
print(math.exp(2))
print(math.factorial(6)) #returns the factorial of number
print(math.fmod(5,2)) #returns float value of modulus (5,2) 5%2-->1.0
print(math.log(2))
print(math.log10(2))
print(math.log2(2))
print(math.modf(5.3)) #seperates the real and integral part
print(math.pi)
print(math.pow(5,3))
print(math.trunc(5.5))

#os,sys,random,json...
#os-->it provides functions to interact with operating system

import os 
#print(dir(os))
#print(os.getcwd()) #returns current working directory 
#change current directory
#os.chdir('/home/workspace/my-project/python_classes')
print(os.getcwd())
#print(os.listdir())
# for i in os.listdir():
    print(i)
#print(os.mkdir('sample'))
print(os.removedirs('sample'))

import sys
print(sys.path) #gives complete root path
'''
#random module-->majorly useful to generate random data
import random,time
#print(dir(random))
print(random.random()) #it gives random number (float)
#OTP Gneration
for i in range(10):
    print(random.randint(1000,9999))
    time.sleep(5) #sleep-->take the time interval
