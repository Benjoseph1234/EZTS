t = int(input())
r=""
for i in range(t):
    a,b = input().split()
    for i in b:
        if i not in a:
            r+=i
    print(r)
