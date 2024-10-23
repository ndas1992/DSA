def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    
    new = lst[::-1]
    print(new)
    return new
lst = [1, 2, 3, 4, 5]
reverse_list(lst)