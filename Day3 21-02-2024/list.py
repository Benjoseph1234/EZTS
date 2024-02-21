'''
a = [10, 20, 30, 40]
print(a)
'''

'''
a = list(map(int,input().split()))
print(a)
'''


#duplicate elements in a array


'''
lst = []
n = list(map(input("Enter number of elements : ").split()))[:n]
for i in range(0, n):
    ele =int(input())
    lst.append(ele)
    print(lst)
'''
#approach 1
'''
n = int(input())
a = list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break
'''
#approach 2
'''
n = int(input())
a = list(map(int,input().split()))[:n]
a.sort()
for i in range(0,n-1):
    if a[i]==a[i+1]:
        print(a[i])
        break
'''
#approach 3

n = int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    c = a.count(i)
    if c>1:
        print(i)
        break
