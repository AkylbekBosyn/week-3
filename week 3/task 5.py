#Task_5
print("\nTask")
from fractions import Fraction
a,b = 4,3
c,d = 8,9
ir_f = Fraction(Fraction(a,b) - Fraction(c,d))
print("The irreducible fraction: ", ir_f)
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ir_f.numerator, ir_f.denominator)
print("\nTask")
def div(a):
    for i in range(1, a+1):
        if a%i==0:
            print(i, end=" ")
        else: continue
n = int(input("Input the number: "))
div(n)
