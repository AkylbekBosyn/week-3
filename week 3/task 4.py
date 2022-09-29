#four
print("Task")
from fractions import Fraction
a,b = 4,3
c,d = 8,9
ir_fr = Fraction(Fraction(a,b), Fraction(c,d))
print("The irreducible fraction: ", ir_fr)
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ir_fr.numerator, ir_fr.denominator)
print("Task")
x = 1;
y = 1;
p1,p2 = 0,4
f1,f2 = 3,2
n1,n2 = 1,2
radius = 3
def point_in(px, py, radius, x, y):
    if ((x-px)**2+(y-py)**2)<=radius**2:
        print("Point is inside if the circle!")
    else:
        print("Point is outside of the circle!")
point_in(p1,p2,radius,x,y)
point_in(f1,f2,radius,x,y)
point_in(n1,n2,radius,x,y)
