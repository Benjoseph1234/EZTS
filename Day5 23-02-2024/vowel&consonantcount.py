#approach 1
'''
s = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
s = s.lower()
vc = 0
cc = 0
for i in s:
    if i in v:
        vc+=1
    elif i in c:
        cc+=1
print(vc,cc)
'''
#approach 2
vowels=['a','e','i','o','u','A','E','I','O','U']
s=input()
v,c=0,0
for i in s:
    if i in vowels:
        v+=1
    elif i.isalpha():
        c+=1
    else:
        continue
print(f"{v} {c}")



