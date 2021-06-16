physics=int(input("enter the marks of physics"))
chem=int(input("enter the marks of chemistry"))
bio=int(input("enter the marks of biology"))
sum=physics+chem+bio;
avg=sum/3;
print("your avgerage mark is",avg)
if(avg>=80):
    print("your grade is Distinction")
elif(avg>=60 and avg<=80):
    print("your grade is first divison")
elif(avg>=45 and avg<=60):
    print("you grade is second dvison")
elif(avg>=40 and avg<=45):
    print("your grade is pass")
elif(avg<=40):
    print("your garde is promotion")
else:
    print("yo garde is fail")
