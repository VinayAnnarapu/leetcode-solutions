def printNumber(current,n):
    if(current>n):
        return
    print(current)
    printNumber(current+1,n)
    
printNumber(1,10)