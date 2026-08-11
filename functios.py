 #pass by value
#pass by object reference

#pass by value reference-->Immutable objects(int,float,str,tuple,frozenset)
'''
def update(number):
    """pass by value reference works"""
    number = 15
    number = number * 5
    return number
print(update(5))
number = 23
print(update(number))
print(number)
print(update('3'))


def update(number):
    """Example Usage"""
    return number *3
    print(update(3))
    print(update(25))
    number = 45
    print(update(number))


#pass by object reference--> mutable objects(list,set,dict)
def update(items):
    """pass by value"""
    items.append("mobile")
    return items
cart = ['laptop','charger']
print(update(cart))
print(cart)

#Functions are termed as first class objects
#A function inside another function-->enclosing scope(non local)
#A function can be used as an argument to another function-->list(map(int,input()))
#A function can call itself(recursive functions)
#A function can return another function

#Built-in functions-->python by default has biult-ins which makes the logic easier
if __name__ == "__main__":
    #print(2+34)
    #print(dir())
    print(dir('__builtins__')) #list of all biult-ins (errors and functions)

#we will discuss some of widely used built-in functions
print(abs(-23))
all(),any()-->checks for the values
print(all(data))
data.clear
print(all(data))
d=[None,23,45]
print(all(d))
print(any(d))
print(bin(6)) #returns binary representation of object
print(chr(65)) #input any integer->returns specific char
print(bool(0)) #returns boolean(T/F)
print(complex()) #returns complex number
print(dict(name="akshitha",place="codegnan")) #returns a dictionary

print(divmod(5,3)) #returns the division modulus in a tuple...

details=['codegnan','akshitha','AAI']
for i in details:
    print(details.index(i),':',i)
#print(dict(enumerate(details)))
#print(dict(enumerate(details,1)))

a=eval(input("enter the dictionary:"))
print(a)
print(id(a))
b=(23,1,4,6)
print(tuple(sorted(b)))
print(min(b))
print(max(['C','code','data']))
print(pow(2,3))
print(tuple(reversed(b)))
print(round(4.56))
print(round(4.567,2))
details=['codegnan','AAAI']
ages=[7,1]
d=dict(zip(details,ages))
print(d)
#zip-->combines multiple collections into one iterable(list,dict)

#recursive fuctions,anonymous functions
#recursive function-->a function calling itself,where it makes the smaller problem is broken into multiple times
#depends on two cases-->base case(it indicates when to stop tha base condition)
#                   -->recursive case(it makes the problem to be repeated)
syntax:
def function():
    if base_condition:
        return()
    function() #we write our recursive
function()

def test():
    """without base case"""
    return test()
print(test())

#5! --> 5 * (5-1) * (5-2) * (5-3) * (5-4)-->120

#factorial approach using recursion

def factorial(n):
    """Recursive approach"""
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return ("enter only +ve values")
    else:
        return n * factorial(n-1)
n = int(input("enter a value:"))
print(factorial(n)

def natural(n):
    if n == 1:
        return 1
    else:
        return n+natural(n-1)
print(int(input("Enter a value:")))
print(natural(n))

#task : build a simple choice chooser
#1-->recursion logic for factorial
#2-->sum of numbers
#3-->BMI calculate
#4-->fibonacci series
#5-->ATM usecase

#anonymous functions-->nameless fuctions,we define them by using lamda keyword
#filter(),map()

#create a function to return the area of rectangle

def rectangle(l,b):
    """sample function to get area of rectangle"""
    return l*b
print(rectangle(5,4))
b=rectangle(4,5)
print(b)

#syntax:--->var_name=lambda parameters:expression
b = lambda l,b:l*b
print(type(b))
print(b(5,6))
#area of square
c=lambda side:side*side
side=int(input("enter the measurements:"))
print(c(side))

d=lambda firstname,lastname:firstname+lastname
firstname=str(input("enter the firstname:")).title()
lastname=str(input("enter the lastname:")).title()
print(d(firstname,lastname))

#to get even number from user input
n=int(input("enter a value:"))
result=lambda n: "Even" if n%2 == 0 else "odd"
print(result(n))

#length of sequences
name = input("enter the message:")
result = lambda name: len(name)
print(result(name))

#filter(),map()
#filter(function,iterable)-->returns the filtered values by satisfying the condition
#yielding the value from iterable

#list of integers
a=list(map(int,input("enter the values:").split(',')))
print(a)
b=list(filter(lambda x:x%2==0,a))
print(b)

names=['pavan','abhiram','nihanth','saikiran','roshan','vasanthi','manimala']
full_names=list(filter(lambda name:len(name)>6,names))
print(full_names)

#map()-->it will apply for every value from multiple iterables

names = ['codegnan','akshitha','agenticai']
result = list(map(lambda name:name.upper(),names))
print(result)

prices = [1000,2500,3500,4000]
final_price=list(map(lambda price:(price-price*0.1),prices))
print(final_price)
'''
#reduce-->this makes complete iterable to be a single value-->functools
from functools import reduce
numbers = [1,4,5,7,8]
result = reduce(lambda a,b:a+b,numbers)
print(result)
