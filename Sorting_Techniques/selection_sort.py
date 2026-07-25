arr=[5,4,3,2,1]

def selectionSort(arr):
    
    for i in range(0,len(arr)-1):
       min_Index=i
       for j in range(i+1,len(arr)):
           if(arr[j]<arr[min_Index]):
               min_Index=j
       arr[i],arr[min_Index]=arr[min_Index],arr[i]
    return arr
            
print(selectionSort(arr))





# Time Complexity Anlaysis

# Inner for loop is traversing entire array for n times in first iteration    -    n
# Inner for loop is traversing entire array for n-1 times in second iteration  -   n-1
# |
# |
# |


# n+n-1+n-2+n-3 ......+ 2+1=  N(N+1)/2 = Nothing but N**2
#  Best Case= N**2
#  Avg Case= N**2
#  Worst Case= N**2

# Space Complexity : Selction sort uses Auxilary space , becuase it is "in -place" Algorithm

# Space: O(1)