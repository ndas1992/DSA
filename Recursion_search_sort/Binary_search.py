def helper(arr, x, s, e):
    if s>e:
        return False
    
    m = (s+e)//2
    
    if arr[m]==x:
        return True
    if arr[m]<x:
        s = m+1
        return helper(arr, x, s, e)
    else:
        e = m-1
        return helper(arr, x, s, e)
    
def Binary_search(arr, x):
    s = 0
    e = len(arr)-1
    return helper(arr, x, s, e)
    
print(Binary_search([i for i in range(3, 1000)], 3))

