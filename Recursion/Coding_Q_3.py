def sum_of_natural_numbers(n):
    """
    Function to calculate the sum of the first n natural numbers using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the sum is to be calculated.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    # Your code here
    if n==0:
        return 0
    ans = sum_of_natural_numbers(n-1) + n
    return ans
    
n=5
print(sum_of_natural_numbers(n))