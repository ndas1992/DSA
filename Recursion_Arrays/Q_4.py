def print_all_indices_list(arr, x, ind=0):
    if len(arr) == ind:
        return -1
    
    if arr[ind] == x:
        print(ind)
    
    print_all_indices_list(arr, x, ind+1)
    

    
print_all_indices_list([3,2,5,2,8,2,1], 2)