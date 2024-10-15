def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    lst = []
    for i in range(1, n+1):
        if (i == 1) or (i == n):
            lst.append('*'*n)
        else:
            lst.append('*'+' '*(n-2)+'*')
    print(lst)
    return lst
    
generate_hollow_square(3)
    