#approach1
'''
n=int(input())
both_happy=0
alice=list(map(int,input().split()))
bob=list(map(int,input().split()))
for i in range(n):
    if bob[i]<=(2*alice[i]) and alice[i]<=(2*bob[i]):
        both_happy+=1
print(both_happy)
'''
#approach2
'''
def compare(t):
    if t==0:
        return
    else:
        n=int(input())
        both_happy=0
        alice=list(map(int,input().split()))
        bob=list(map(int,input().split()))
        for i in range(n):
            if bob[i]<=(2*alice[i]) and alice[i]<=(2*bob[i]):
                both_happy+=1
        print(both_happy)
    
    compare(t-1)

t=int(input())
compare(t)
'''
#approach3
t = int(input())
for i in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    b = list(map(int,input().split()))
    happy = 0
    for i in range(n):
        if a[i] <= 2*b[i] and b[i]<=2*a[i]:
            happy+=1
    print(happy)

