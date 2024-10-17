def celsius_to_fahrenheit(C):
    """
    Function to convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    C (float): The temperature in Celsius.
    
    Returns:
    float: The temperature in Fahrenheit.
    """
    # Your code here
    f_temp = ((9/5)*C) + 32
    print(f_temp)
    return f_temp
    
celsius_to_fahrenheit(25)