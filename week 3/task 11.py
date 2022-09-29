import random
print("\nTask")
def Twins(n):
    print([[i, i+2] for i in range(n, 2*n - 1)])
Twins(int(input())) 
print("\nTask")
A = int(input())
B = int(input())
C = [[random.randrange(10) for i in range(A)] for j in range(B)] 
for i, row in enumerate(C):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(C)
