
#plan your weekend
Budget=int(input("enter the budget:"))
if Budget>10000:
    print("plan:Trip")
elif Budget>5000:
    print("plan:Resort stay")
elif Budget>3000:
    print("plan:Movie and Dinner")
elif Budget>1000:
    print("plan:Cafe and Shopping")
elif Budget>500:
    print("plan:Street food and Park visit")
elif Budget<0:
    print("enter valid amount")
else:
    print("plan:Stay Home")


    


