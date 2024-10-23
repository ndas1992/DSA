def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # TODO: Implement this function
    number = int(''.join(map(str, digits)))
    number = str(number + 1 )
    print(number)
    lst = list(number)
    lst = list(map(int, lst))
    print(lst)
    return lst
    
    
digits = [1, 2, 3]
plus_one(digits)
    
