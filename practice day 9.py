#nested dictionaries:
data= {
    'p1':{'name':'Akshitha',
          'Age':21,
          'Disease':'fever',
          'Doctor':'Praveen'},
    'p2':{'name':'Shiva',
          'Age':30,
          'Disease':'diabetes',
          'Doctor':'Haritha'},
    'p3':{'name':'Sujatha',
          'Age':40,
          'Disease':'PCOD',
          'Doctor':'Sunitha'},
    'p4':{'name':'Manasa',
          'Age':36,
          'Disease':'Cancer',
          'Doctor':'David'}}

#display all records
print(data.keys())
#give disease of p2
print(data['p2']['Disease'])
print(data.setdefault('p4'))
#add a new patient
#print(data.setdefault('p5'))
data.setdefault('p5',{'name':'krishna','Age':35,'Disease':'Covid','Doctor':'Ram'})
print(data)
#update doctor in p3
data['p3']['Doctor']='Anitha'
print(data)
#delete p1
del data['p1']
print(data)
#total patients
print(len(data))





































                      




    
    
    




























