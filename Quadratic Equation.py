import cmath
a=int(input('Enter The value Of A : '))
b=int(input('Enter The Value of B : '))
c=int(input('Enter The Value of C : '))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print(sol1)
print(sol2)