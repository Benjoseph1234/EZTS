#approach 1
'''
class check:
    def __init__(self,n):
        self.n = n
    def ispalindrome(self):
        if self.n == self.n[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = check("Hello")
ob2 = check("Sas")
ob1.ispalindrome()
ob2.ispalindrome()
'''
#approach 2
'''
j = input()
k = input()
class check:
    def __init__(self,n):
        self.n = n
    def ispalindrome(self):
        if self.n == self.n[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = check(j)
ob2 = check(k)
ob1.ispalindrome()
ob2.ispalindrome()
'''
#approach 3
class Palindrome:
    def __init__(self, string):
        self.string = string
    def is_palindrome(self):
        return self.string == self.string[::-1]
p = Palindrome("madam")
print(p.is_palindrome())

