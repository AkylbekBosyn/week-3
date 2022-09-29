print("\nTask")
def permutation(lst):
    if len(lst) == 0: return []
    if len(lst) == 1: return [lst]
    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l
llist = []
count = 0
print("You need to input 3 numbers. (Range: [100,N], 210<N<231.) ")
for c in range(3):
    n = int(input("Input an integer: "))
    llist.append(n)
for c in permutation(llist):
    print(*c, sep="")
    count+=1
print("Number of numbers: ", count)
print("\nTask ")
def seq_reverse(string):
    words = string.split(' ')
    rev_s = ' '.join(reversed(words))
    return rev_s
n = input("Input some text: ")
print(seq_reverse(n))
