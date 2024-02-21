'''
w = int(input())
if w>2 and w%2==0:
    print("YES")
else:
    print("NO")
'''
n = int(input())
def divide_even(n):
    if n % 2 != 0 or n <= 2:
        return "Input must be an even number greater than 2"
    else:
        return n // 2 - 1, n // 2 + 1

# Test the function
print(divide_even(n)) 

