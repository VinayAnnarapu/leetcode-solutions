import math

def primeCheck():
    n = int(input("Enter Number: "))
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(primeCheck())