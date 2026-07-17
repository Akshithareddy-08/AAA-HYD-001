#dictionary--->collection of key value pairs,mutable,ordered
details= {}
print(details)
print(type(details))

details={'Name':'Akshitha','Place':'Hyd','Age':21}
print(details)
print(len(details))
#Accessing keys
print(details['Name'])
print(details['Age'])
#print(details['age'])#raises keyError

#key must be unique in a dictionary

data={'Age':25,'name':'code','Age':26}
print(data)#returns recent update value of age as output
#in dictionary we index by using keys


#create dictionaries using datatypes

students_data={'ids':[23,21,45,52],
               'names':['praneeth','abhiram','vasanthi','akshitha'],
               'place':('hyd','vjwda'),
               'gender':{'male','female'}}
print(len(students_data))
print(students_data.keys())#returns keys from dictionary
print(students_data['names'])

print(students_data.values())

students_data['course']=['PFS','JFS','AAA','DA']

print(students_data)
print(type(students_data))

print(type(students_data['ids']))
#now if we want to insert 3 more unique ids
#students_data['ids']=56,67,87#this is not recommended in this case

students_data['ids'].extend([56,67,87])
print(students_data)
students_data['names'].insert(1,'Ashok')
print(students_data['names'])

#we want to insert new place
students_data['place']=list(students_data['place'])
print(students_data['place'])
students_data['place'].append('Vizag')
print(students_data['place'])
print(students_data)

print(students_data['course'])
print(students_data['course'][1::2])

students_data['names'].sort()
print(students_data['names'])


#keys(),values(),items()
print(students_data.items())#returns key,value pairs as tuple

#get will return value if key is existing,else default--->None
print(students_data.get('branch'))
print(students_data.get('branch','CSE'))#returns CSE instead of None
print(students_data)
#print(students_data['branch'])#returns keyError

#setdefault()--->update the dic if key is not existing with default none
print(students_data.setdefault('ids'))
#students_data.setdefault('branch')
students_data.setdefault('branch',['CSE','CSD','ECE','IT'])
print(students_data)

#update(),pop(),popitem(),clear()
students_data.update({'fees':[456,234],'marks':[45,78,85]})
print(students_data)
print(students_data.pop('marks'))
print(students_data)
print(students_data.popitem())#comes from last
print(students_data)

#clear()&copy() work it out

#fromkeys() will create a new dic by accepting each object in the given iterable as key whereas value is set to None
ids=[23,45,67]
#
d=dict.fromkeys(ids)
print(d)
d[23]='random'
print(d)

#nested dictionaries:

data={
    's1':{'id':23,
          'name':'ram',
          'place':'hyd'},
    's2':{'id':25,
          'name':'sony',
          'place':'bng'}}
print(data.keys())
print(data['s1']['name'])






                            



























