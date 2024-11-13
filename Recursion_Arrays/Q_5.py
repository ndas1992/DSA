def all_indices_list(arr, x):

    def helper(ind):
        if len(arr) == ind:
            return []
        
        if arr[ind] == x:
            return [ind] + helper(ind+1)
        else:
            return helper(ind+1)
    
    return helper(0)
    

print(all_indices_list([3,2,5,2,8,2,1], 2))  

