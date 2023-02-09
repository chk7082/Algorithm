def test(array):
    '''
    function that return 1, if given array contains all from 1~9
                  return 0, otherwise
    '''

    # if it's in 2-dim'l 3 by 3 matrix, flatten it
    if len(array) == 3:
        array = array[0] + array[1] + array[2]

    # counts each word
    is_particular_num = [0] * 9
    for num in array:
        is_particular_num[num - 1] = 1

    # if there's 0 multiplicity, then it's invalid
    if 0 in is_particular_num:
        return 0
    else:
        return 1


def verify_sudoku(matrix):
    '''
    function that verify if the given matrix is valid sudoku or not

    :param
    matrix (list) : 2-dim'l matrix of size 9 by 9 (queried sudoku)

    :return:
    result (int) : 1, if valid sudoku
                   0, otherwise
    '''

    # for each row
    for i in range(9):
        if not test(matrix[i]):
            return 0

    # for each col
    for j in range(9):
        if not test([matrix[i][j] for i in range(9)]):
            return 0

    # for each 3 by 3 block
    # (i, j) : upper left index of each block
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [matrix[k][j:(j + 3)] for k in range(i, i + 3)]
            if not test(block):
                return 0
    return result


T = int(input())

for t in range(1, T + 1):
    result = 1
    matrix = []
    for _ in range(9):
        matrix.append(list(map(int, input().split())))
    print(f"#{t} {verify_sudoku(matrix)}")