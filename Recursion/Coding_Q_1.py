def factorial(num):
    """
    Function to calculate the factorial of a non-negative integer n using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of n.
    """
    if num==1 or num==0: #Base Case where no more iteration are needed
        return 1
    fact = num*factorial(num-1)
    num = num-1
    return fact

print(factorial(5))