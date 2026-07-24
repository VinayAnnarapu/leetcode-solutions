
# Parameterized recursion

def findFactorial(n, fact=1):
    if n == 0:
        return fact
    return findFactorial(n - 1, fact * n)

print(findFactorial(5))  




# Functional Recursion

# def findFactorial(n):
#     if n==0:
#         return 1
#     return n*findFactorial(n-1)
# print(findFactorial(5))