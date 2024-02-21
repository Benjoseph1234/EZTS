'''n = int(input())
for i in range(1,n+1):
    a = tuple(map(int,input().split()))
    if a%2==0:
        print(0)
    elif a == 1:
        print(1)
    else:
        print(0)
     
'''
#approach1
'''
t = int(input())
for i in range(t):
    n = int(input())
    t1 = 0
    t2 = 0
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                t1+=1
            else:
                t2+=1
    if t1==t2:
        print(1)
    else:
        print(0)

'''

#approach2

t = int(input())
for i in range(t):
    n = int(input())
    factors = []
    for j in range(1,n+1):
        if n%j==0:
            factors.append(j)
    #print(factors)
    ed = []
    od = []
    for j in factors:
        if j%2==0:
            ed.append(j)
        else:
            od.append(j)
    if len(ed)==len(od):
        print(1)
    else:
        print(0)



    
      