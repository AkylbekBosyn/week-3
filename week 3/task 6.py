print("\nTask")
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    return gcd
def lcm(a, b):
    lcm = (a*b)/gcd(a,b)
    print(lcm)
a = int(input("Input the 1st number: "))
b = int(input("Input the 2nd number: "))
print(gcd(a,b))
lcm(a,b)
print("\nTask")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
d = float(input("Fourth side: "))
dia = float(input("Diagonal: "))
def quadl(a,b,c,d,dia):
    def heron_f(a,b,c):
        p=0.5*(a+b+c)
        return (p*(p-a)*(p-b)*(p-c))**0.5
    return heron_f(a,b,dia) + heron_f(c,d,dia)
print("The area of a quadliteral is: ", quadl(a,b,c,d,dia))
