def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    # TODO: Implement this function
    n = len(arr)-1
    for i in range(n):
        if arr[0]>arr[-1]:
            if arr[i+1]<arr[i]:
                return False
        else:
            if arr[i]>arr[i+1]:
                return False
    return True
                
        
