def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    # TODO: Implement this function
    maxx = lst[0]
    for i in lst:
        print(f'i: {i},   max:{maxx}')
        if i>=maxx:
            maxx = i
    return maxx
    
lst = [3, 5, 2, 9, 6]
find_max_element(lst)