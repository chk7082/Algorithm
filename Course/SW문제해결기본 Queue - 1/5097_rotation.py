def rotation(N, M, arr):
    '''
    function that return the first element of arr after rotating it M-times

    :param
    N (int) : length of arr
    M (int) : the number of rotation that we want to proceed
    arr (list) : original list containing positive numbers

    :return
    result (int) : the first element of arr after rotating it M-times
    '''

    # we don't actually need to rotate it, just move index(front)
    return arr[M % N]



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'#{t} {rotation(N, M, arr)}')

