def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    lst = []
    for i in range(1, n+1):
        spaces = i-1
        star = (2*(n-i)) + 1
        if i==1:
            lst.append('*'*((2*n) - 1))
        else:
            lst.append(' '*spaces + '*'*star + ' '*spaces)
            
    print(lst)
    return lst

generate_inverted_pyramid(3)        