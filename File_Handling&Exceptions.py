
#Files modes-->'r','w','a'

#Default file mode-->open("file_name.txt",'r') #default we have 'r'
file = open('example.txt')
#print(file)
print(file.read()) #returns entire text from tha file
#print(file.read(5))
#print(file.readlines())
#print(len(a))
#print(file.readline())

#check whether the file exists or not
import os 

if os.path.exists('example.txt'):
    f = open('example.txt').read()
    print(f)
    print(f'File is already present')
else:
    print("File not found")

#checking the file and its size 
file_path = "example.txt"
if os.path.exists(file_path):
    print(f'File size is {os.path.getsize(file_path)}bytes')
    print(f'File Absolute path is {os.path.abspath(file_path)}')
else:
    print('File not found')

#'w'mode-->it will automatically creates a file and if same file name is present it
#overrides the content in previous file
a = open('agents.txt','w')
print(a)
a.write("AAA-HYD-001 students are good.")
a.write("\n Yes it is true.")
a.writelines("Agentic AI is the big thing happening.\t The world is progressing")
a.close()

a = open('example.txt','w')
a.write("Today is wednesday")
a.close()

#if the file is already present 'w' mode will override the content
#we can use with statement
with open('example.txt','w') as file:
    #print(file.read()) raises error
    print(file)
    file.writelines("Agentic AI is the big thing happening.\t The world is progressing")
    print(file.read())

with open('example.txt','a') as f:
    print(f)
    f.write("\nPython RAG Agents...")

with open('rag.txt','a') as r:
    print(r)
    r.writelines("Agents,MCP,RAG,GEN AI...")

with open('rag.txt','r+') as d:
    print(d.read())
    d.write('\n Claude,Chatgpt,Copilot...')

import os 
d = os.listdir()
for file in d:
    if file.endswith('.txt'):
        print(file)

#exception handling-->program (try,except,finally)
'''syntax as below
try:
    base statement(s) which may raise error...
    .....
except exception (error name) as e:
    .....
finally:
    statement(s)...

#typeError,valueerror,index error,arithmetic error,zerodivision error,Attribute errors
a,b = map(int,input("enter the values").split(','))
try:
    result = a/b
    print(f'Result is {result}')
except ZeroDivisionError:
    print('Denominator cannot be zero')
except ValueError:
    print('values to be of integer format only')
finally:
    print("Anyways this will be printed...")
'''
#exceptions together
try:
    a,b = map(int,input("enter the values").split(','))
    result = a/b
    print(f'Result is {result}')
except (ZeroDivisionError,ValueError) as e:
    print(f"The error occured {e}")
finally:
    print("Anyways this will be printed...")

   