def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    # TODO: Implement this function
    summ = 0
    for i in lst:
        summ = summ + i 
    print(summ)
    return summ
    
lst = [-1, -2, -3, -4] 
sum_of_elements(lst)
