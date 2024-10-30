def matrix_reshape(mat, r, c):
    """
    Function to reshape a matrix.
    :param mat: List[List[int]] -> The original matrix
    :param r: int -> Number of rows in reshaped matrix
    :param c: int -> Number of columns in reshaped matrix
    :return: List[List[int]] -> The reshaped matrix or original matrix if not possible
    """
    # TODO: Implement this function
    m = len(mat)
    n = len(mat[0])
    new_mat = []
    temp = []
    if m*n == r*c:
        for ar in mat:
            for obj in ar:
                temp.append(obj)
        print(temp)

        index = 0
        for i in range(r):
            lst = []
            for j in range(c):
                lst.append(temp[index])
                index = index+1
            new_mat.append(lst) 
        return new_mat
    else:
        return mat


mat = [[1, 2], [3, 4]]
r = 1
c = 4
matrix_reshape(mat, r, c)