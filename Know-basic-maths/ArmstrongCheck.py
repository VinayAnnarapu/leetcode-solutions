def armstrongCheck():
    n=int(input('Enter Number to Check Armstrong'))
    pow=0
    sum=0
    org=n
    num=n
    while(n>0):
        n=int(n/10)
        pow=pow+1
    while(num>0):
        ld=num%10
        sum=sum+(ld**pow)
        num=int(num/10)
    print(pow)
    return org==sum

# armstrongCheck()

print(armstrongCheck())