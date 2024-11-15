def Linear_search_recursion(arr, x, index=0):
    if len(arr) == index:
        return False
    
    if arr[index] == x:
        return True
    
    # if Linear_search_recursion(arr, x, index+1) == True:
    #     return True
    # else:
    #     if arr[index] == x:
    #         return True
    #     else:
    
    return Linear_search_recursion(arr, x, index+1)

print(Linear_search_recursion([i for i in range(3, 1000)], 2))