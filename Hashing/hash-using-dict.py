
# Number Hasing using dict 
# dictionary useful when we want array with size more than 10**7


def numberHash(num,arr):
    Dict={}
    for val in arr:
        if val in Dict:
            Dict[val]+=1
        else:
            Dict[val]=1
    return Dict.get(num)


arr=[1,3,4,5,6,7,7,7]
print(numberHash(7,arr))


# Char hasing using dictionary

def characterHash(char, string):
    hashMap = {}
    
    for ch in string:
        if ch in hashMap:
            hashMap[ch] += 1
        else:
            hashMap[ch] = 1

    return hashMap.get(char)


string = "VinayVinay"

print(characterHash('V', string))  
print(characterHash('i', string))  
