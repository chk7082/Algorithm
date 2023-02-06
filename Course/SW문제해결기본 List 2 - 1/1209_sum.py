def sum_1209(matrix, size):
    '''
    function that return the maximum of union of
    (row sums & col sums & diag sums) of matrix

    :param
    matrix (list) : 2-dim'l array containing integers
    size (int) : integer that represent the dimension of matrix (size * size)

    :return
    max_val (num) : maximum of union of
    (row sums & col sums & diag sums) of matrix
    '''

    # initialize our max_val with large negative value
    max_val = -1e8

    # when we meet summation with > max_val
    # update it

    # consider row sum
    for i in range(size):
        row_sum = sum(matrix[i])
        if row_sum > max_val:
            max_val = row_sum

    # consider col sum
    for j in range(size):
        col_sum = sum([matrix[i][j] for i in range(size)])
        if col_sum > max_val:
            max_val = col_sum

    # consider diag sum
    diag_sum_1 = sum([matrix[i][i] for i in range(size)])
    if diag_sum_1 > max_val:
        max_val = diag_sum_1
    diag_sum_2 = sum([matrix[i][size - 1 - i] for i in range(size)])
    if diag_sum_2 > max_val:
        max_val = diag_sum_2

    return max_val


T = 10
size = 100

for t in range(1, T+1):
    _ = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    print(f"#{t} {sum_1209(matrix, size)}")