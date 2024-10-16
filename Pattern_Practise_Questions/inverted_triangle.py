def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(1, n+1):
        lst.append('*'*(n+1-i))
    
    print(lst)
    return lst

generate_inverted_triangle(3)