# Update all indices for a given element in a global list provied

ans_list = [4, 5, 6]

def update_all_indices_in_list(arr, x, index=0):
    # global ans_list
    if len(arr) == index:
        return ans_list
    
    if arr[index] == x:
        ans_list.append(index)

    return  update_all_indices_in_list(arr, x, index+1)

print(update_all_indices_in_list([3,2,5,2,8,2,1], 2))  