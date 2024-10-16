def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    lst = []
    k = 1
    for i in range(1, n+1):
        pattern = ''
        for j in range(i):
            pattern = pattern + str(k) + ' '
            k = k+1
        lst.append(pattern.strip())
    
    print(lst)
    return lst

generate_floyds_triangle(3)
