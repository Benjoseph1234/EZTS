#approach 1
'''
s=input()
res=""
l=0
while l<len(s):
    c=1
    for i in range(l+1,len(s)):
        if s[l]==s[i]:
            c+=1
        else:
            break
    res+=s[l]
    res+=str(c)
    l+=c

print(res)
'''
#approach 2
s = input()
n = len(s)
r = ""
c = 1
for i in range(1,n):
    if s[i] == s[i-1]:
        c+=1
    else:
        r=r+s[i-1]+str(c)
        c=1
r=r+s[n-1]+str(c)
print(r)

