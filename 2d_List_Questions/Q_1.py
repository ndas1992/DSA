def generate(numRows):
    """
    Function to generate the first numRows of Pascal's triangle.
    :param numRows: int -> Number of rows of Pascal's triangle to generate
    :return: List[List[int]] -> The first numRows of Pascal's triangle
    """
    # TODO: Implement this function
    final = []
    for i in range(numRows):
        temp = []
        print(i)
        for j in range(i+1):
            if i == 0:
                k = 1
            else:
                prev_list = final[i-1]
                print(f'prev__list: {prev_list}')
                if j==0 or j==i:
                    k = 1
                else:
                    k = prev_list[j-1]+prev_list[j]
            temp.append(k)  
        final.append(temp)       
        print(f'fianl: {final}')   
        print('-------'*10)    
    print(final)
    return final