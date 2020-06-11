thislist=[]
N=int(input("enter number of students:"))#entering number of students
for i in range(0,N):
    elements=int(input("enter weights in lbs:"))#enter weights of students
    thislist.append(elements)#appends weights into lists

print(elements)
kg=[lbs / 2.204 for lbs in thislist]
print(kg)#prints weights in kgs


