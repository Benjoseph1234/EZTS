#approach 1
'''
t = int(input())
for i in range(t):
    a,b = input().split()
    b = int(b)
    r = ""
    for i in a:
        k = ord(i)+b
        if k>122:
            k = 96 + (k-122)
            r+=chr(k)
        else:
            r+=chr(k)
    print(r)
'''
#approach 2
for i in range(int(input())):
    s,n=map(str,input().split())
    res=""
    n=int(n)
    for j in s:
        if (ord(j)+n)>122:
            res+=chr(96+(ord(j)+n)-122)
        else:
            res=res+chr(ord(j)+n)
    print(res)
