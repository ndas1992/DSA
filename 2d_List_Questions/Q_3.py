def can_be_rotated(matrix, target):
    """
    Function to rotate the matrix 90 degrees clockwise.
    :param matrix: List[List[int]] -> 2D list representing the matrix
    :return: None -> Modifies the matrix in-place
    """
    # TODO: Implement this function
    rt = 1
    while rt<=3:
        for i, arr in enumerate(matrix):
            m = len(arr)-1-i
            for j, obj in enumerate(arr):
                n = len(arr)-1-j
                if j>=i and j<m:
                    temp = matrix[n][i]
                    matrix[n][i] = matrix[m][n]
                    matrix[m][n] = matrix[j][m]
                    matrix[j][m] = matrix[i][j]
                    matrix[i][j] = temp
        if matrix == target:
            print(matrix)
            break
        rt = rt+1

# matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
# target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
matrix = [[0, 1], [1, 1]]
target = [[1, 0], [0, 1]]
can_be_rotated(matrix, target)