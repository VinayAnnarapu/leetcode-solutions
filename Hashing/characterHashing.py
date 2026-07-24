def characterHash(char,str):
    # Creating an eptry hash array
    str= str.lower()
    strArr=[0]*(26)
    # Storing the frequencies in hash array
    for ch in str:
        ch=ord(ch)-ord('a')
        strArr[ch]+=1
    print(strArr)
    
    # Fetching the frequency of the given character
    return strArr[ord(char)-ord('a')]
    
print(characterHash('i','VinayVinay'))