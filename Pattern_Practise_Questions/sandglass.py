def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    lst = []
    for i in range(1, 2*n):
        star = (2*(n-i)+1)*'*'
        space = (i-1)*' '
        
        if i>n:
            star = star = (2*(i-n)+1)*'*'
            space = ((2*n)-i-1)*' '
        
        pattern = space + star + space
        if (i==1) or (i==2*n):
            pattern = ((2*n)-1)*'*'
        lst.append(pattern)
        
    print(lst)
    return lst
    
generate_sandglass(3)