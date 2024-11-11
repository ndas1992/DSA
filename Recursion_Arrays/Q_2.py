def first_index_of_element(arr, x):
    # Base Case
    if len(arr) == 0:
        return -1
    
    if arr[0]==x:
        return 0
    
    if first_index_of_element(arr[1:], x) == -1:
        return first_index_of_element(arr[1:], x)
    else:
        return first_index_of_element(arr[1:], x) + 1

print(first_index_of_element([3, 2, 5, 2, 8, 2, 1], 2))
print(first_index_of_element([3, 2, 5, 2, 8, 2, 1], 10))
print(first_index_of_element([3, 2, 5, 2, 8, 2, 1], 1))




def last_index_of_element(arr, x):
    # Base Case
    if len(arr) == 0:
        return -1

    smallresult = last_index_of_element(arr[1:], x)

    if smallresult != -1:
        return smallresult + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1

print(last_index_of_element([3, 2, 5, 2, 8, 2, 1], 2))
print(last_index_of_element([3, 2, 5, 2, 8, 2, 1], 10))
print(last_index_of_element([3, 2, 5, 2, 8, 2, 1], 1))