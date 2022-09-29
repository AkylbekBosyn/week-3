print("\nTask 15.1")
def Palindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
def count(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if Palindrome(i):
            print(i, end = " ")
count(0, 9999)
print("\nTask")
import math
def distance(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d
coordinates=['x','y','z','t']
arr=[]
print("Input coordinates: ")
for i in range(4):
    b=[]
    print("Coordinates: ",coordinates[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
flag = True
for i in range(3):
    for j in range(i+1, 4):
        dist = distance(arr[i],arr[j])
        if flag or min_dist > dist:
            m1=i
            m2=j
            min_dist = dist 
            flag = False
print(f'Minimum distance between points {coordinates[m1]} и {coordinates[m2]}')
print(f' The distance = {min_dist**0.5:.3f}')
