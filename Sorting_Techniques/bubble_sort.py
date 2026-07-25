arr=[5,7,8,6,4,8]

def bubble_sort(arr):
    
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    
print(bubble_sort(arr))


# Time Complexity Analysis

#  Best Case= N**2
#  Avg Case= N**2
#  Worst Case= N**2

# Space Complexoty Analysis

# O(1)




# You can make Bubble Sort run in $O(N)$ Best Case time if the array is already sorted by using a swapped flag to stop early:

# def bubble_sort_optimized(arr):
#   n = len(arr)
#   for i in range(n - 1):
#     swapped = False
#     for j in range(0, n - 1 - i):
#       if arr[j] > arr[j + 1]:
#         arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         swapped = True
#     # If no swaps occurred during this pass, the array is already sorted!
#     if not swapped:
#       break
#   return arr