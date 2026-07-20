# brute force approach
# def divisorCount():
#     n = int(input("Enter a Number: "))

#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i)

# divisorCount()



# Optimized Approach

import math

def divisorCount():
    n = int(input("Enter a Number: "))
    arr = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n // i:
                arr.append(n // i)
    arr.sort()
    return arr
print(divisorCount())