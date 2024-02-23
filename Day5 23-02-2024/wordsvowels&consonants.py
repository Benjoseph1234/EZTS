#approach 1
'''
t = int(input())
v = "aeiou"
for i in range(t):
    s = list(input().split())
    vc=0
    cc=0
    wc=len(s)
    for j in s:
        for k in j:
            if k.isalpha():
                if k in v:
                    vc+=1
                else:
                    cc+=1
    print(wc,vc,cc)
'''
#approach 2
t=int(input())
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(t):
    s=input()
    l=list(s.split())
    v,c=0,0
    for i in s:
        if i in vowels:
            v+=1
        elif i.isalpha():
            c+=1
        else:
            continue
    print(f"{len(l)} {v} {c}")
