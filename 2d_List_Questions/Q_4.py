def spiral_order(matrix):
    """
    Function to return the elements of the matrix in spiral order.
    :param matrix: List[List[int]] -> The input matrix
    :return: List[int] -> The elements in spiral order
    """
    # TODO: Implement this function
    n = len(matrix[0])
    m = len(matrix)
    left, right = 0, n
    top, bottom = 0, m
    #print(f'top: {top}, bottom: {bottom}, left: {left}, right: {right}')
    op_array = []

    while left<right and top<bottom:
        print(f'top: {top}, bottom: {bottom}, left: {left}, right: {right}')
        for i in range(left, right):
            op_array.append(matrix[top][i])
        top = top+1
        print(op_array)
        print(f'top: {top}, bottom: {bottom}, left: {left}, right: {right}')

        for i in range(top, bottom):
            op_array.append(matrix[i][right-1])
        right = right-1
        print(op_array)
        print(f'top: {top}, bottom: {bottom}, left: {left}, right: {right}')

        if not(left<right and top<bottom):
            break

        for i in range(left, right):
            op_array.append(matrix[bottom-1][right-1-i])
        bottom = bottom-1
        print(op_array)
        print(f'top: {top}, bottom: {bottom}, left: {left}, right: {right}')

        for i in range(top, bottom):
            op_array.append(matrix[bottom-i][left])
        left = left+1
        print(op_array) 
        print(f'top: {top}, bottom: {bottom}, left: {left}, right: {right}')
        print('------------'*4)
    print(op_array)

    
matrix = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
spiral_order(matrix)