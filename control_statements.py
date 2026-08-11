'''
assert--->assert keyword is mainly used for debugging cases in development,it checks for the given


x= int(input("enter a positive number:"))
assert x>0
assert x>0,"value should be only +ve"
print(f'updated value is {x}')
assert x in [12,23,45],"checking data"
print(f'search found')

for i in range(3):
    for j in range(2):
        print(i,j)
        
#number patterns,row based number patterns,column based number patterns,triangle
for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()
      '''  

for i in range(65,68):
    for j in range(1,4):
        print(chr(i),end=(' '))
    print()
    




