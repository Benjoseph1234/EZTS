a = int(input())
for i in range(a):
    n,x = map(int,input().split())
    if(n>x):
        k = n-x
        if k%4==0:
            print(k//4)
        else:
            print((k//4)+1)
    else:
        print(0)
