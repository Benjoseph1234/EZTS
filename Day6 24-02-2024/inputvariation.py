class total:
    def __init__(self,n,s):
        self.n,s = n,s
    def isprime(self):
        count = 0
        for i in range(1,self.n+1):
               if self.n%i==0:
                   count+=1
        if count == 2:
            return "Yes"
        else:
            return "No"
    def ispalindrome(self):
        if self.s == self.s[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = total(12,"Hello")
ob1.isprime()
ob2 = total(14,"SaS")
ob1.ispalindrome()
ob3 = total(17,"RadaR")
ob3.isprime()
ob3.ispalindrome()

