print("\nTask")
def divide(n):
    answer = []
    for i in range(1,n+1):
        s = str(i)
        temp = True
        for j in s:
            if int(j) == 0:
                temp = False
            elif i % int(j) != 0:
                temp = False
        if temp:
            answer.append(i)
    return answer
n = int(input("Input the number of elements: "))
print(divide(n))
print("\nTask")
m = int(input("Length: "))
list = []
for i in range(0,m):
    a = int(input("Enter the element: "))
    list.append(a)
def swap(list):
    print("Original array: ", list)
    list[0],list[m-1] = list[m-1],list[0]
    print("Result: ", list)
swap(list)
