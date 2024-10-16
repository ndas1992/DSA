def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    lst = []
    for i in range(1, (2*n)):
        if i>n:
            i = (2*n) - i
        star = (2*i)-1
        space = (n-i)
        pattern = ' '*space + '*'*star + ' '*space
        lst.append(pattern)
    print(lst)
    return lst
    
generate_diamond(3)
        
            
            