def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.
    
    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.
    
    Returns:
    float: The calculated value of y.
    """
    # Your code here
    y = float(slope*x)+intercept
    print(y)
    return y
    
calculate_y(1.5, -2, 2)