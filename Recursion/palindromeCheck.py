def palindromeCheck(l,r,str):
    if(l>=r):
        return True
    if(str[l]!=str[r]):
        return False
    return palindromeCheck(l+1,r-1,str)
str='MADAM'
print(palindromeCheck(0,len(str)-1,str))