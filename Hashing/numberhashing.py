def numberHash(num,arr):
    maxVal=max(arr)
    # crating new hash Array to store frequencies
    newArr=[0]*(maxVal+1)
    
    # Storing frequencies in hash array
    for val in arr:
        newArr[val]+=1
    print(newArr)
    
    # Fetching the frequecy of given number from hash array
    
    return newArr[num]
    
        
arr=[1,2,2,4,5,6]

print(numberHash(2,arr))