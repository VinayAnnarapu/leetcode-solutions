# given the number , you need to find how many the number is repeated in array or return count 
# of given number in array



def findCount(num,arr):
    count=0
    for i in range(len(arr)-1):
        if num==arr[i]:
           count= count+1
            
    return count



arr=[5,5,5,6]
print(findCount(5,arr))