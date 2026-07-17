#control statements-->these are the statements which control the flow of execution of the program
#conditional statements (if,else,elif)--->nested if statemets
#repetition statements (loops)--->for,while,nested loops (patterns)
#jumping statements---> break,continue,pass,assert

#if statement:
'''
if <condition>:
    statement(s)....
    ......
    ...


#validate the price
money=100
money=int(input("enter the billing value:"))#dynamic input
if money <=100:
    print(f'now you are eligible to get your items')
    print("check again")

students=['ram','akash','abhi','mani']
name=input("enter the student name:").lower()
if name in students:
    marks=50
    grade='A'
    print(f'{name} has secured {marks} marks and {grade} grade')


#if-else statements
#syntax:

if condition:
    statement(s)
    .....
    ...
else:
    statement(s)..
    ...

#vote eligibility

age=int(input("Enter the age:"))
if age>=18:
    print(f'you are eligible to vote,so use it properly')
    print("your age is {} years,eligible".format(age))
else:
    print("you are not eligible to vote")
    print(f'you need to wait for {18-age} years to get vote right')
'''
#elif statements
age=int(input("Enter the age:"))
if age>=18:
    print(f'you are eligible to vote,so use it properly')
    print("your age is {} years,eligible".format(age))
elif age==0 or age<0:
    print(f'enter only +ve values')
else:
    print("you are not eligible to vote")
    print(f'you need to wait for {18-age} years to get vote right')

          




















    
    
