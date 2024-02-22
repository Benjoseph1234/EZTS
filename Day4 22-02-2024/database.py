#approach 1
'''
t = int(input())
for i in range(t) :
    n,r = map(int,input().split())
    d = {}
    for j in range(r):
        st,co = map(int,input().split())
        if co in d:
            d[co].append(st)
        else:
            d[co] = [st]
for k in d:
    if len(d[k]>n) and len(set(d[j]==len(d[j]))):
        print(f"scenario #{i+1} : Impossible")
        break
else:
    print('possible')
'''

#approach 2
t=int(input())
for a in range(t):
    impossible=0
    n,r=map(int,input().split())
    d={}
    for b in range(r):
        i,c=map(int,input().split())
        if c in d:
            if i in d[c]:
                impossible=1
            else:
                d[c].append(i)
        else:
            d[c]=[i]
            
    if impossible:
        print(f"Scenario #{a+1}: impossible")
    else:
        print(f"Scenario #{a+1}: possible")
