def fibonicci(n):
    """
    Function to calculate the nth Fibonacci number using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the Fibonacci number is to be calculated.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n==0:
        return 0
    if n==1:
        return 1
    
    last = fibonicci(n-1)
    second_last = fibonicci(n-2)
    ans = last + second_last
    print(f'n = {n}, ({last}, {second_last})----> {ans}')
    return ans

print(fibonicci(4))