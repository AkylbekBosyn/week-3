print("\nTask 13.1")
num=int(input("Input any number: "))
for num in range(num, 1000):
    sum1=0
    numcp=num
    if(num>=10 and num<100):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit
            sum1=sum1+d2
            num=int(num/10)

    if(num>=100 and num<1000):
        while(num>0):

            digit=int(num%10)
            d2=digit*digit*digit
            sum1=sum1+d2
            num=int(num/10)
    if(numcp==sum1):
        print("Answer is: ", sum1)
print("\nTask")
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input("Input x1.x2: " ).split())
y1, y2 = map(float,input("Input y1, y2: ").split())
z1, z2 = map(float,input("Input z1, z2: " ).split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*res)
n = 3
res = [tuple(map (float,input().split())) for i in range(n)]
rcos = [acos(*res[i]) for i in range(n)]
k = rcos.index(max(rcos))
print(res[k])
