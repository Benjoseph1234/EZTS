'''
a = int(input())
for i in range(a):
    n,x = map(int,input().split())
    if ((n*x)%4 == 0):
        print((n*x)//4)
    else:
        print((n*x)//4+1)
'''

t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    ts = n*x
    tp=0
    while ts>4:
        tp=tp+1
        ts=ts-4
    if tp==0:
        print(tp)
    else:
        print(tp+1)

