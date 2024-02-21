#approach1
'''
n=int(input())
for i in range(1,n+1):
    factors=[]
    if i%2==0:
        for j in range(1,i):
            if i%j==0:
                factors.append(j)
        if sum(factors)==i:
            print(i)
'''
#approach2
n = int(input())
s=0
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
    s=0

