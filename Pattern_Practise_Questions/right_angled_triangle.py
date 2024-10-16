def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(1, n+1):
        space = (n-i)*' '
        star = i*'*'
        pattern = space+star
        lst.append(pattern)
    print(lst)
    return lst

generate_right_angled_triangle(3)
        