#p1
''' p1
a = int(input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)'''

#p2
''' 
a = int(input())
b = int(input())
c = int(input())
if a>b and b>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)'''

#p3
'''
a = int(input())
b = int(input())
if a>b:
    print(b)
else:
    print(a)
'''

#p4
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    a=0
elif b>c:
    b=0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
