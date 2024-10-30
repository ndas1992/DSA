def search_matrix(matrix, target):
    """
    Function to search for a target in the matrix.
    :param matrix: List[List[int]] -> The input matrix
    :param target: int -> The target value to search for
    :return: bool -> True if target is found, False otherwise
    """
    # TODO: Implement this function
    m = len(matrix)-1
    n = len(matrix[0])-1

    start = 0
    end = m
    while start<=end:
        mid = (start+end)//2

        if matrix[mid][0] < target:
            start = start+1
        elif matrix[mid][0] > target:
            end = end-1
        elif matrix[mid][0] == target:
            print(f'target: {target}')
            return True

    arr = matrix[end]
    start = 0
    end = n
    while start<=end:
        mid = (start+end)//2

        if arr[mid] < target:
            start = start+1
        elif arr[mid] > target:
            end = end-1
        elif arr[mid] == target:
            print(f'target: {target}')
            return True
    print('False')
    return False


    
        
matrix = [[1, 3, 5, 7], 
        [10, 11, 16, 20],
        [23, 30, 34, 60]]
target = 5
search_matrix(matrix, target)