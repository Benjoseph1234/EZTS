# n,m = map(int,input().split())
#approach 1
'''
n=int(input())
d={}
for i in range(n):
    l=list(map(str,input().split()))
    d[l[0]]=l[1]

t=int(input())
for i in range(t):
    name=input()
    if d.get(name)!=None:
        print(name+"="+d[name])
    else:
        print("Not found")
'''
#approach 2
n = int(input())
d = {}
for i in range(n):
    name,num = input().split()
    d[name] = num
while True:
    s = input()
    if s in d:
        print(f"{s} = {d[s]}")
    else:
        print("Not Found")
