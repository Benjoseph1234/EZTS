'''
#ours
a = int(input())
res = 0
if a>0:
    while a!=0:
        digit = a%10
        res = res*10+digit
        a=a//10
    print(res)
else:
    a = a*(-1)
    while a!=0:
        digit = a%10
        res = res*10+digit
        a=a//10
    print(res*(-1))
'''

'''
n = int(input())
if n>0:
    res = 0
    while n>0:
        r = n%10
        res = (res*10)+r
        n=n//10
    print(res)
elif n==0:
    print(n)
else:
    res = 0
    n=n*-1
    while n>0:
        r = n%10
        res = (res*10)+r
        n=n//10
    print(res*(-1))
'''

