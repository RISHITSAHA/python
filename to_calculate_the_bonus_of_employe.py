#write a program to calculte the bonus of an emplye based n their age
#if age>50 bonus is 20%
#   age>30-50 bonus 30%
#   else 50%

a=int (input("enter the age of the employe :"))
b=int(input("enter the salary of the employe :"))

if a>50:
    c=(b*20)/100
    f=b+c
    print("the salary is:",c)
    print("the total salary is :",f)
elif a>30:
    d=(b*30)/100
    h=b+d
    print("the salary is:",d)
    print("the total salary is :",h)
else:
    e=(b*50)/100
    i=b+e
    print("the salary is:",e)
    print("the total salary is :",i)