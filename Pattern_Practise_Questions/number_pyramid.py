def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        num_str = ''
        for j in range(i):
            num_str = (num_str + str(j+1) + ' ')
        pattern = (n-i)*' ' + num_str.strip() + (n-i)*' '
        lst.append(pattern)
        
    print(lst)
    return lst
generate_number_pyramid(3)