#Tuples--->tuples are an immutable,ordered,heterogenous,indexed sequence type,we use () for decleration
data=1,24,5
print(data)
print(type(data))

#nested tuples
details=('codegnan',32,(2,4,5),'saketh',[12,45,'agents','rag'])
print(details)
print(len(details))
print(details[2])
print(details[4][2])
'''
details[0]=details[0].replace('n','f')
print(details)

details[4][2]=details[4][2].replace('a','A')
print(details)
'''
print(details[1:4])

print(details[::3])

details[4].remove('agents')
print(details)

#operations on Tuples
age=22,21,32,25
ids=231,342,213
print(age+ids)#merging
print(age*2)
print(22 in age)#membership

#len(),type(),min(),max()
age=(25,12,45,65)
print(min(age))
print(max(age))
print(tuple(sorted(age)))#typecasting

#index(),count()
details=('akshitha','vasanthi','manimala',34,23,5.8)
print(details)

print(details.index(34))
print(details.count(34))
'''
'''#Tuple--->list
details=list(details)
print(details)
print(type(details))

#list-->tuple
details='akki'
details=tuple(details)
print(details)
print(type(details))

#Set datatype--->sets,frozen sets
#sets-->a set is unique,mutable collection
a={}
b=set()# a set is an unorderd collection
print(type(a))
print(type(b))

ids={123,124,125,126,127,123,124}#duplicates will be removed
print(ids)
print(len(ids))
print(type(ids))

#as a set is mutable we can insert,remove elementss into set
data={23,4.5,'codegnan',(12,34,5)}
print(data)

ids={123,124,125,126,127,123,124}
print(ids)
#add()
ids.add(156)
print(ids)
ids.add('agents')
print(ids)
#update()
ids.update([2,78])
print(ids)
data=['vasu','akki','mani']
ids.update(data)
print(ids)

#remove elements from sets-->discard(),remove(),clear(),pop()
#discard()
ids.discard(123)
print(ids)
ids.discard(124)
print(ids)

#ids.remove(123)#returns keyError
#pop()
print(ids.pop())
print(ids.pop())
print(ids.pop())
#print(ids.pop())# it has become empty set
#clear()
print(ids.clear())#returns none
print(ids)#returns empty set

#union,intersection,diffrence,symmetric diff,subsets,supersets
ages={35,23,123,24,45}
print(ages)

d=ids.union(ages)
print(d)
e=ids.update(ages)
print(e)
print(ids)

f=ids.intersection(ages)
print(f)
print(ids)
g=ids.intersection_update(ages)
print(g)
print(ids)

h=ids.difference(ages)
print(h)#removes common elements & returns remg elements
#union-->'|'#intersection-->'&'#symmetric diff-->'^'#diff-->'-'
g=ages-ids
print(g)
u=ids|ages
print(u)
v=ids^ages
print(v)

#below fuctions returns boolean
a={1,2,3}
b={1,2,3,4,5}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))#it returns false

#Frozen set is an immutable set
data=frozenset(ids)
print(data)
print(type(data))
#we cannot remove/insert elements but mathematical operations are possible
temp_details=frozenset([34,35,34,32,31])
print(temp_details)
print(min(temp_details))
print(max(temp_details))
print(sorted(temp_details))





























