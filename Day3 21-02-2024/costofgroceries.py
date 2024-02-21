#approach1
'''
def Cost(t):
    if t==0:
        return 
    else:
        n,x=map(int,input().split())
        fresh=list(map(int,input().split()))
        cost=list(map(int,input().split()))
        total_cost=0
        for i in range(n):
            if fresh[i]>=x:
                total_cost+=cost[i]
        print(total_cost)
    Cost(t-1)
    
t=int(input())
Cost(t)
'''
#approach 2
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split))
    b = list(map(int,input().split))
    c = 0
    for j in range(n):
        if a[j]>=x:
            c+=b[j]
    print(c)


