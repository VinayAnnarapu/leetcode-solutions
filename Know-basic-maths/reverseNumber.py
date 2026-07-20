def reverseNumber():
    n=int(input("Enter a Number"))
    rev=0
    while(n>0):
        ld=n%10
        rev=rev*10+ld
        n=int(n/10)
    return rev


print(reverseNumber())