def rotate(matrix):
    """
    Function to rotate the matrix 90 degrees clockwise.
    :param matrix: List[List[int]] -> 2D list representing the matrix
    :return: None -> Modifies the matrix in-place
    """
    # TODO: Implement this function
    print(matrix)
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
                print(f'({i}, {j})----> ({j}, {m})----> ({m}, {n})----> ({n}, {i})---->  ({i}, {j})')
                print(f'matrix after {j} iteration: {matrix}')
        print(f'matrix after {i} iteration: {matrix}')
        print('-------------'*4)

matrix = [[5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]]
rotate(matrix)