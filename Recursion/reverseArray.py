def reverse(l,r,arr):
    if(l>=r):
        return arr
    temp=arr[l]
    arr[l]=arr[r]
    arr[r]=temp
    
    return reverse(l+1,r-1,arr)

arr=[1,2,3,4,5]
print(reverse(0,len(arr)-1,arr))