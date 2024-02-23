#approach 1
'''
digit=("0123456789")
s=input()
c=0
for i in s:
    if i in digit:
        c+=1
    else:
        break

if c==len(s):
    print("Yes")
else:
    print("No")
'''
#approach 2
'''
a = input()
d = "0123456789"
for i in a:
    if i not in d:
        print("No")
        break
else:
    print("Yes")
'''
#approach 3
'''
s = input()
if s.isdigit():
    print("Yes")
else:
    print("No")
'''

#approach 4
'''
s=input()
digits="1234567890"
for i in s:
    if i not in s:
        print("No")
        break
else:
    print("Yes")
'''

