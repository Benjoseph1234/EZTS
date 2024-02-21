#approach1
'''
n=int(input())
factors=[]
if n==1:
    print("Neither prime nor composite")
else:
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    if len(factors)>2:
        print("Not Prime")
    else:
        print("Prime")
'''

#approach2
'''
n =int(input())
for i in range(2,n+1):
    if i%2==0:
        print("prime")
    else:
        print("Nor prime")
'''


