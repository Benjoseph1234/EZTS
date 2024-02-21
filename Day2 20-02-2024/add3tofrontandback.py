# n = int(input())
# n = ((n*10)+3)
# print(n)
# n1 = ((n*10)+3)


#Append Three
'''
def three(n):
    temp=n
    l=0
    while temp>0:
        l+=1
        temp=temp//10
    power=1
    while l>0:
        power=power*10
        l-=1
    n=(3*power)+n
    n=n*10+3
    return n    
'''
    
n = int(input())
def temp(n):
    r=n
    c=0
    while r>0:
        c+=1
        r=r//10
    n = (3*pow(10,c))+n
    n = n*10+3
    return n 
print(temp(n))
