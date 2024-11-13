def print_all_indices(arr, x, index=0):
    if len(arr)==index:
        return
    
    if arr[index] == x:
        print(index)

    print_all_indices(arr, x, index+1)
    



print_all_indices([3,2,5,2,8,2,1], 2)