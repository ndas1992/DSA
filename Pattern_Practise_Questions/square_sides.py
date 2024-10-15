def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    lst = []
    for i in range(1, n+1):
        lst.append(n*'*')
    print(lst)
    return lst
    
generate_square(3)