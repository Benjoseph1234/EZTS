#functions 
# def function_name(arg1,arg2,arg3....)
# """Docstring"""
# statements(s)
# return[expressions]
# print/9eavl("20-10")

'''
def myFun(x):
    x[0] = 20
lst = [10,11,12,13,14,15,16]
myFun(lst)

print(lst)
'''

# def num(a,b):
#     return a*b
# num(2,6)

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

num = 4
print(num,factorial(num))

