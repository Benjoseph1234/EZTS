'''
def sugarcane(n):
    income=50*n
    remain=int(income-income*0.7)
    print(remain)

def main(t):
    if t==0:
        return
    else:
        n=int(input("Enter no.of glasses: "))
        sugarcane(n)
    main(t-1)
    

t=int(input("Enter the test cases: "))
main(t)
'''


def profit(nu):
    p = nu*50*(0.3)
    return int(p)
def test(t):
    if t==0:
        return
    else:
        n = int(input())
        print(profit(n))
    test(t-1)
t = int(input())
test(t)



        