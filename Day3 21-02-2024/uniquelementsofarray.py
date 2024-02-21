#approach 1
'''
n = int(input())
a = list(map(int,input().split()))[:n]
unique = []
for i in range(n):
    if a.count(a[i])==1:
        if a[i] in unique:
            continue
        else:
            unique.append(a[i])  
        break

for i in unique:
    print(i,end = " ")
'''

#approach 2
n= int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    if a.count(i)==1:
        print(i,end = " ")


