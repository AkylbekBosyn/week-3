import math
#import
print("Task")
a = int(input("The length of 1:"))
b = int(input("The length of 2:"))
def hypot(s1):
    h = math.sqrt((s1**2)*2)
    return h
print(hypot(a))
print(hypot(b))
if hypot(a)>hypot(b):
    print("Hypotenuse1 is bigger!")
if hypot(a)<hypot(b):
    print("Hypotenuse2 is bigger!")
else: print("They are equal!")
print("\nTask")
def alphab_order(str):
    return ''.join(sorted(str))
str = 'Python is the best programming language'
print(alphab_order(str))
