

def countDigit():
    n=int(input('Enter a Number'))
    count=0
    while(n>0):
        n=int(n/10)
        count=count+1
    return count
print(countDigit())