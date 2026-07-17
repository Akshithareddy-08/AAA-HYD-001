data=['codegnan',35,4.56,['python','java','AAI','DA',],100,45]
print(len(data))
print(data[3])
a=data[3][:2]
print(a)
b=data[3][2:]
print(b)
c=(data[3][1][1:4])
print(c)
d=(data[3][::2])
print(d)
e=(data[1::2])
print(e)

data[1]=45
print(data)
data[2]=['agents','prompt','RAG']
print(data)
data[3][1]='RAG'
print(data)

data=['codegnan',35,4.56,['python','java','AAI','DA',],100,45]
data[1:3]=['java''DSA']
print(data)
data[1:3]=['RAG','MCP','Agents','LORA','GPT']
print(data)
data[3][1::2]=['RAG','MCP']
print(data)

#append(),extend(),insert()
details=['akshitha',21,'codegnan']
print(len(details))
print(details)
details.append(35)
print(details)
details.append('agentic AI')
print(details)
details.append(data)
print(details)
details.extend((34,45))
print(details)
details.extend(['codegnan'])
print(details)
details.extend((['code'],36,45))
print(details)
details.insert(1,'python')
print(details)
print(len(details))
details.insert(-1,['code'])
print(details)
details.insert(6,['temp','agents','class'])
print(details)
details.extend(['agents','MCP'])
print(details)
details.pop()
print(details)
details.pop(2)
print(details)
details.remove('agents')
print(details)
details.clear()
print(details)
del details[2:4]
print(details)

details.extend(['agents','RAG'])
print(details)
print(details.index('agents'))
print(details.index('agents',4))
print(details.count('agents'))
print(details.count('code'))
details.pop(1)
print(details)
details.sort()
print(details)
    





























            













              

































