def fly_extermination(N, M, fly_arr):
    '''
    function that return the possible maximum number of flies
    that we could kill with just a single swing swatter

    :param
    N (int) : size of fly arr (N by N)
    M (int) : size of fly swatter (M by M)
    fly_arr (list) (N by N) : 2-dim'l list containing
                              the number of flies in each position

    :return
    result (int) : the possible maximum number of flies
                   that we could kill with just a single swing swatter
    '''

    # use convolution with N by N image, with M by M filter with all 1s
    # stride : 1, no activation
    result_size = N - M + 1
    result_matrix = [[0] * result_size for _ in range(result_size)]

    # use element wise addition M * M times
    # for each result_size by result_size matrix with upper left index (i, j)
    for i in range(M):
        for j in range(M):
            result_matrix = element_wise_addition(result_matrix,
                                                  [row[j:j+result_size] for row in fly_arr[i:i+result_size]])

    return max([max(row) for row in result_matrix])

def element_wise_addition(arr1, arr2):
    '''
    helper function that return element-wise added array
    '''

    return [[arr1_element + arr2_element for arr1_element, arr2_element in zip(arr1_row, arr2_row)]
            for arr1_row, arr2_row in zip(arr1, arr2)]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    fly_arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {fly_extermination(N, M, fly_arr)}')