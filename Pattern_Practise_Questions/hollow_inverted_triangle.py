def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(1, n+1):
        if (i==1) or (i==n):
            pattern = ((n+1)-i)*'*'
            
        else:
            space = (n-i-1)*' '
            pattern = '*'+space+'*'
            
        lst.append(pattern)
    print(lst)
    return lst
    
generate_hollow_inverted_right_angled_triangle(4)