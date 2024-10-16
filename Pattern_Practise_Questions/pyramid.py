def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    lst=[]
    total = (2*n)-1 
    
    for i in range(1,n+1):
        if i != n:
            spaces = n-i
            pattern = (' '*(n-i)+'*'*((2*i)-1)+' '*(n-i))
        if i == n:
            pattern = '*'*((2*i)-1)
            
        lst.append(pattern)
            
    print(lst)
    return lst
    
generate_pyramid(3)