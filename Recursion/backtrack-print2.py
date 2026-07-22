def printNumber(n):
    if(n<1):
        return
    print(n)
    printNumber(n-1)
    
printNumber(10)