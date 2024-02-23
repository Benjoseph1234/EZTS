#approach 1
'''
vowels=['a','e','i','o','u','A','E','I','O','U']
s=input()
c=0
for i in s:
    if i in vowels:
        c+=1
    else:
        break

if c==len(s):
    print("Yes")
else:
    print("No")
'''
#approach 2
a = input()
v = "aeiouAEIOU"
for i in a:
    if i not in v:
        print("No")
        break
else:
    print("Yes")

