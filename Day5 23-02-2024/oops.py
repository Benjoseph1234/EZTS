#p1
'''
class cse:
    def hello(self):
        print("hello cse")
class aiml:
    def hello(self):
        print("hello aiml")
ob1=cse()
ob1.hello()
'''
#p2
'''
class classa:
    def factorial(self,n):
        r=1
        for i in range(1,n+1):
            r*=i
        print(r)
a = int(input())
ob=classa()
ob.factorial(a)
'''
#p3
'''
class a:
    def __init__(self):
        print("Hello")
    def hello(self):
        print("Hello a")
ob=a()
'''
#p4
'''
class classa:
    def __init__(self,n):
        self.n = n
    def factorial(self):
        r=1
        for i in range(1,self.n+1):
            r*=i
        print(r)
ob = classa(5)
ob.factorial()
'''
#p4
class classa:
    def __init__(self,n):
        self.n=n
    def factorial(self):
        print(self.fact(self.n))
    def fact(self,n):
        if n==1:
            return 1
        else:
            return n*(self.fact(n-1))
ob=classa(5)
ob.factorial()
