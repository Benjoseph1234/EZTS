'''
n = int(input())
x = 1
for i in range(1,n+1):
    x = x*i
print(x)

'''
'''
n = int(input())
x = 1
while n>0:
    x = x*n
    n = n-1
print(x)

'''

def fact(n):
    if n>1:
        return n*fact(n-1)
    else:
        return 1
print(fact(n))


