print("\nTask")
def sumOfd(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum
n = int(input("Input the number: "))
sub = sumOfd(n)
ans = 0
while n > 0:
    ans += 1
    n -= sub
print(ans)
print("\nTask")
def prod_mean(arr):
    a = 1
    mean = sum(arr)/len(arr)
    for i in range(0,len(arr)):
        a*=arr[i]
    print("The product of elements: ", a)
    print("The arithmetic mean: ", mean, "\n")
arr1 = [4, 65, -78, 74, 4, 3, 2, 9]
arr2 = [5, 77, 69, 14, 25, -81]
arr3 = [99, 88, 44, 66, 33, 22, 55, 77]
prod_mean(arr1)
prod_mean(arr2)
prod_mean(arr3)
