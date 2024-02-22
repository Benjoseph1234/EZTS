'''
n = input()
s = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
for n in range(set(s)):
    if (s|n) == s:
        print("pangram")
    else:
        print("not pangram")
'''
#approach1
'''
s = input()
def pan(s):
    s.lower()
    a = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    for i in a:
        if i not in s:
            return "not pangram"
        else:
            return "pangram"
print(pan(s))
'''
#approach2
'''
s = input()
s1 = set(s)
if len(s1) == 27:
    print("pangram")
else:
    print("not pangram")
'''
#approach3
'''
alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s = input()
d = {}
for i in s:
    if i in alpha:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
x = d.keys()
if x==26:
    print("pangram")
else:
    print("not pangram")
'''
#approach4
'''
s=input()
a=set(s)
c=0
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitals=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(26):
    if (alphabets[i] in a) or (capitals[i] in a):
        c+=1
if c==26:
    print("Panagram")
else:
    print("Not Panagram")
'''                
#approach5
'''
s=input()
d={}
numbers=['0','1','2','3','4','5','6','7','8','9']
for i in s:
    if i!=" " and i not in numbers:
        if i in  d:
            continue
        else:
            d[i]=1

if len(d)==26:
    print("Panagram")
else:
    print("Not Panagram")
'''
#approach6
