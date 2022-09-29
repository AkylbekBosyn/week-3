
import math
#first
print("Task 1.1")
n = int(input("Choose the number to calcuate the area:\n""1.Triangle\n2.Rectangle\n3.Circle\n"))
def area(n):
    if n==1:
        h = int(input("Enter triangle's height length: "))
        b = int(input("Enter triangle's breadth length: "))
        t_area = 0.5 * b * h
        print("The area of triangle is: ", t_area)
    if n==2:
        h = int(input("Enter rectangle's first side: "))
        b = int(input("Second side: "))
        r_area = h * b
        print("Rectangle's area is: ", r_area)
    if n==3:
        r = int(input("Enter circle's radius: "))
        c_area = math.pi * r**2
        print("Circle's area is: ", c_area)
area(n)
print("\nTask 1.2")
arr1 = [1, 5, -98, 5, 77, -7, 34]
arr2 = [1, 2, 34, 456, 7, 3, 4, -9, -10]
arr3 = [3, -7, 4, -6, 12, 17]
def sum_and_mean(arr):
    print(sum(arr))
    mean = sum(arr)/len(arr)
    print(mean)
sum_and_mean(arr1)
sum_and_mean(arr2)
sum_and_mean(arr3)
