#approach1
'''
n=int(input())
d={}

for i in range(n):
    word=input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1

large=max(d.values())


same=[i for i in d if d[i]==large]

print(f"{max(same)} {large}")
'''

#approach 2
n = int(input())
d ={}
for i in range(n):
    s = input()
    if s in d:
        d[s] = d[s]+1
    else:
        d[s] = 1
x = max(d.values())
z = []
for i in d:
    if d[i] == x:
        z.append(i)
print(max(z),x)
