def array_rotation(N, arr):
    '''
    function that return rotated version of rotated arr
    (90, 180, 270 degree rotated with clockwise direction)

    :param
    N (int) : size of arr
    arr (2-dim'l list) (N by N) : array containing digits in string!!

    :return
    rotated (2-dim'l list) (N by 3) : rotated array where each column
                                      represents one of (90, 180, 270)-degree
                                      rotated one
    '''

    # initialize rotated array
    rotated = [['']*3 for _ in range(N)]

    # 90 degree
    for i in range(N):
        rotated[i][0] = ''.join([arr[k][i] for k in range(N-1, -1, -1)])

    # 180 degree
    for i in range(N):
        rotated[i][1] = ''.join([arr[N-i-1][k] for k in range(N-1, -1, -1)])

    # 270 degree
    for i in range(N):
        rotated[i][2] = ''.join([arr[k][N-i-1] for k in range(N)])

    return rotated


T = int(input())
for t in range(1, T+1):
    N = int(input())

    # arr : 2-dim'l array containing digit character
    arr = [input().split() for _ in range(N)]

    # our result
    rotated = array_rotation(N, arr)

    print(f'#{t}')
    for i in range(N):
        print(*rotated[i], sep=' ')