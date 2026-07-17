#Input Formatting -->input()
#String input
a=input()
print(a)
a=input('enter the username:')
print(a)
print(type(a))
#Integer input -->int()
age=int(input('enter the age:'))
print(age)
print(type(age))
#Float input
discount=float(input('enter the discounted value:'))
print(discount)
print(type(discount))
#costprice,selling price -->loss/profit
cp=int(input("enter the price:"))
sp=float(input("enter the price:"))
loss=cp-sp
print(loss)
#Multiple String inputs..
name,place=input("enter the detalis:").split()
print(name)
print(place)
name,place=input("enter the detalis:").split(',')
print(name)
print(place)
food,place=input("enter:").split()
print(food)
print(place)
#Multiple integer values
a,b=map(int,input("enter the values:").split(','))
print(a)
print(b)
#Multiple float values
a,b,c=map(float,input("enter the values:").split(','))
print(a)
print(b)
print(c)
#List of strings
data=input("enter the details:").split(',')
print(data)
marks=list(map(float,input("enter the marks:").split(',')))
print(marks)
#separator --> for separating the values
print(2026,7,9,sep='-')
print(2026,8,17,sep='/')
print(2004,28.5,sep=',')
#end argument in print() --> \n -->new line
name='akshitha'
place='hyderabad'
course='AAA'
print(name,place,course,end='\t')
#using commas
name='akshitha'
place='hyd'
print("name:",name,"place:",place,sep=',')
age=25;place='hyd'
print("age is %d and place is %s"%(age,place))
name,course='akshitha','Ai'
print("{} is enrolled in {} course".format(name,course))
#f-string Notation
name,course='akshitha','Ai'
print(f'{name} is enrolled in {course}')
print(f'{"akshitha"}')
      




































































