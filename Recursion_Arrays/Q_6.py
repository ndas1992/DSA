# Update all indices for a given element in a list provied

def update_all_indices_in_list(arr, x, ans_list, index=0):
    if len(arr) == index:
        return ans_list
    
    if arr[index] == x:
        ans_list.append(index)

    return  update_all_indices_in_list(arr, x, ans_list, index+1)

print(update_all_indices_in_list([3,2,5,2,8,2,1], 2, [8, 9]))  