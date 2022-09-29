
print("\nTask")
def arrea(x,y,z,t):
    r_ar = x*y
    tr_ar = ((y-z)*x)/2
    area = tr_ar + r_ar
    return area
print("Y needs to be bigger, than Z. And T needs to be bigger than X.")
x = int(input("Input the 1st side X: "))
y = int(input("Input the 2nd side Y: "))
z = int(input("Input the 3rd side Z: "))
t = int(input("Input the 4th side T: "))
print(arrea(x,y,z,t))

print("\nTask")
def octal(n):
    print("The octal code: ", oct(n))
n = int(input("Input the number to convert: "))
octal(n)
