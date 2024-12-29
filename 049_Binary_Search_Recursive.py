def binary_search(lst, val, low, high):
  if (low > high):
    return None
  else:
    mid = (low + high) // 2
    if (val > lst[mid]):
      return binary_search(lst, val, mid+1, high)
    elif (val < lst[mid]):
      return binary_search(lst, val, low, mid-1)
    else:
      return mid 

# The binary search algorithm works on sorted lists like this one
sorted = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# We pass the list, the element to find '6', and the initial low and high 
# indexes as 0 and len(sorted)-1, i.e. the entire list. The high index is the 
# last index in the list, we need to subtract 1 from the length of the list 
# to get this index as lists in Python are zero-indexed.
i = binary_search(sorted, 6, 0, len(sorted) - 1)

# We should get index '5' as the index of element 6
print("Index of 6:", i)