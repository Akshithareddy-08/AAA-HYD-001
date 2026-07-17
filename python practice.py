data = [ 'Akshitha','Angel',24,(95, 88, 91), {'Python', 'Java', 'Agentic AI', 'GenAI'},{'ML', 'DL', 'MCP'}, 96, 98]
print(data)
print(type(data))
print(len(data))
print(data[3])          # Getting tuple
print(data[4])          # Getting first set
a = data[1:3]
print(a)
b = data[::2]
print(b)
c = data[0][:4]
print(c)
data[1] = 'Codegnan'
print(data)
data[2] = ['RAG', 'Prompt Engineering']
print(data)
print(len(data))
data.pop()
print(data)
data[2].remove('RAG')
print(data)
print(data[2].index('Prompt Engineering'))
print(data.count('Akshitha'))
# Tuple Operations
print(data[3][::2])
print(min(data[3]))
print(max(data[3]))
print(tuple(sorted(data[3])))
print(data[3].index(88))
print(91 in data[3])
print(75 in data[3])
print(data[3].count(88))
print(type(data[3]))
# Set Operations
print(data[4])
print(data[5])
data[5].add('Python')
print(data[5])
data[4].update(('Cloud', 'SQL'))
print(data[4])
print(data)
g = data[4] | data[5]
print(g)
B = data[4].intersection(data[5])
print(B)
C = data[4].copy()
C.intersection_update(data[5])
print(C)
D = data[5].difference(data[4])
print(D)
E = data[4].copy()
E.difference_update(data[5])
print(E)
F = data[4].symmetric_difference(data[5])
print(F)
G = data[4].copy()
G.symmetric_difference_update(data[5])
print(G)
print(data[5].issubset(data[4]))
print(data[4].issuperset(data[5]))
print(data[4].isdisjoint(data[5]))
print(data[4].pop())
data[5].discard('ML')
print(data[5])
data[4].discard('GenAI')
print(data[4])
O = frozenset(data[4])# Frozenset
print(O)
print(type(O))
C = list(data[2])# Type Casting
print(C)
d = data.copy()# Copy
print(d)
d[2][0] = 'Machine Learning'
print(d)
print(data)
data.reverse()# Reverse
print(data)
data.append('Software Engineer')# Append
print(data)# Extend
data.extend(('AWS', 'Docker'))
print(data)
