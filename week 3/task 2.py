import math
print("Task")
side = int(input("Input the side of a hexagon: "))
def hex_ar(side):
    return ((3*math.sqrt(3)*(side**2))/2);
print("The area: ", str(hex_ar(side)))
print("Task")
n = 1
def area(a,b):
    area = a*b
    return area
while n<=3:
    a = int(input("Input the 1st side: "))
    b = int(input("Input the 2nd side: "))
    n+=1
    print(area(a,b))
