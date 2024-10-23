def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # TODO: Implement this function
    if lst[::-1] == lst:
        print(True)
        return True
    else:
        print(False)
        return False

lst = [7, 8, 9, 8]        
is_palindrome(lst)