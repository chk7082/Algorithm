def matrix_search(matrix, target):
    '''
    function that return  True, if target is in matrix
                         False, otherwise
    '''

    # compute the size of given matrix
    M = len(matrix)
    N = len(matrix[0])

    # start from the upper-right corner
    i, j = 0, N-1

    # while the index is valid
    while i < M and j >= 0:
        # if it's target, then done
        if matrix[i][j] == target:
            return True
        # if it's greater than the target, go left
        elif matrix[i][j] > target:
            j -= 1
        # if it's less than the target, go down
        else:
            i += 1

    # when target is not in the matrix
    return False


matrix = [[ 1,  4,  7, 11, 15],
          [ 2,  5,  8, 12, 19],
          [ 3,  6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]

target = 20

print(matrix_search(matrix, target))