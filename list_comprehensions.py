'''
list comprehensions-->in python its a precise/easiest way to create lists

syntax: [expression for itemn in iterable]
iterable-->list,tuple,set,dict or range

#we need to apppend elements into list
list = []
for i in range(10):
    list.append(i)
    print(list)

#the same above using list comprehension
list = [i for i in range(10)]
print(list)

#get the squares of numbers
data = [i**2 for i in range(10)]
print(data)

e = [i%2 ==1 for i in range(10)]
print(e)

#coverting strings to uppercase/lowercase
details=['akshitha','codegnan','data','rag']
new=[i.upper() for i in details]
print(new)
print(*new)

a,*name,c=21,'akshitha','vasanthi','manimala',30
print(a)
print(name)
print(*name)
print(c)

a = [15,20,25,35]
#update the list with each value by 5
a=[i+5 for i in a]
print(a)

#get the first letter of each object in collection
data=['codegnan','agents','rag']
letter=[i[0] for i in data]
print(letter)

#list comprehension with if usage
# [expression for item in iterable/range if condition]

#even numbers from the collection
collection = list(map(int,input("enter the values:").split(',')))
print(collection)
result = [i for i in collection if i%2==0]
print(result)
for i in result:
    print(i,end=' ')
#byusing filter()-->lambda
result1 = list(filter(lambda x:x%2==0,collection))
print(result1)

#fetch desired values with condition satisfied
final = [i for i in collection if i>10]
print(final)

#list comprehension with if-else condition
#syntax:
#[true_value if condition else false_value for item in iterable]
data=[12,3,4,6,7,9]
print(data)
result=["New" if i%2==0 else "old" for i in data]
print(result)

#nested comprehensions
#nested-->one inide another (one loop inside another loop)
#[expression for item in iterable1 for j in iterable2]

a=[(i,j) for i in range(5) for j in range(3)]
print(a)

b = [(i,j) for i in [1,3,5] for j in [4,5,6]]
print(b)

#multiplication table pattern
c = [i*j for i in range(1,11) for j in range(1,11)]
print(c)
print(*c)

colors = ['red','blue','green']
sizes = ['S','M','L']
dress = [(i,j) for i in colors for j in sizes]
print(dress)

#nested comprehension with if condition
#[expression for item1 in iterable1 for item2 in iterable2 if condition]

#possible pairs
a = [(i,j) for i in range(5) for j in range(3) if i!=j]
print(a)

c = [i*j for i in range(1,11) for j in range(1,11) if i!=j]
print(c)
print(*c)
'''

#nested comprehensions with if-else
#[true_value if condition else false_value for item1 in iterable for item2 in iterable]

a=[1,3,5,6,7]
b=[2,4,6,8,9]
c=(x+5 if x<y else x for x in a for y in b)
print(c)
#in the above case if we replace [] braces with () we dont get tuple -->generator
#no tuple comprehension---> generator
#Generator---> generator is a special function which produces one value at a time...
#we use yield keyword
#normal function
'''
def fname():
    """doc string"""
    return value(s)
fname()

def fname():
    """doc string"""
    yield value1
    yield value2
    yield value3
fname()

def fun():
    """normal function"""
    return [1,2,4,5,6]
print(fun())
a=fun()
for i in a:
    print(i)

def fun():
    """generator function"""
    yield 1
    yield 2
    yield 3
b=fun()
print(next(b))
print(next(b))
print(next(b))
print(next(b)) #stop iteration

def display():
    """subjects covered"""
    yield "Python"
    yield "GENAI"
    yield "RAG"
    yield "Agents"
print(display())
print(type(display()))
d = display()
print(next(d))
'''
                                                                                                                                                                                                                                                                                                