def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # TODO: Implement this function
    new_arr = ARR[0:D]
    Remaining = ARR[D:]
    rotated = Remaining + new_arr
    print(rotated)
    return rotated
    
ARR = [1, 2, 3, 4, 5]
D = 2
rotate_left(ARR, D)
