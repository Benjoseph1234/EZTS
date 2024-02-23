#approach 1
'''
s = input()
x = len()
es = ""
os = ""
for i in range(n):
    if i%2==0:
        es+=s[i]
    else:
        os+=s[i]
print(os+es)
'''
#approach 2
'''
s = input()
n = len(s)
os = s[1::2]
es = s[::2]
print(es+os)
'''
#approach 3
s=input()
if len(s)%2==0:
    for i in range(1,len(s)+1,2):
        print(s[i],end="")
    for i in range(0,len(s),2):
        print(s[i],end="")
else:
    for i in range(1,len(s),2):
        print(s[i],end="")
    for i in range(0,len(s)+1,2):
        print(s[i],end="")
