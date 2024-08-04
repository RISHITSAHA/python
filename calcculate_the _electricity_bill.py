# write a program to calculate the electricity bill
# first 100 unit RS 6 per unit
# second 100 unit RS 7 per unit
# next 100 unit RS 8 per unit

a=int(input("enter the amount of units consumed"))

if a<=100:
    b=6*a
    print("electricity bill is RS",b)
elif a<=200:
    c=(6*100)+(7*(a-100))
    print("the electricity bill is RS",c)
else:
    d=(6*100)+(7*100)+(8*(a-100))
    print("electricity bill is RS",d)

