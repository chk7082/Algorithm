def deadlock(transposed):
    '''
    function that compute the number of deadlock made by magnetics

    :param
    N (int) : size of original space (before deleting 0)
    transposed (list) : list containing strings where each string
                        indicate each column (with 0 deleted)

    :return
    result (int) : the number of deadlock made by magnetics
    '''

    # it is sufficient to count the number of '12' in each column
    return sum(map(lambda string: string.count('12'), transposed))


# 1 : to south
# 2 : to north

T = 10
for t in range(1, T+1):
    N = int(input())
    magnetic = [input().split() for _ in range(N)]
    transposed = list(map(lambda string: (''.join(string)).replace('0', ''), zip(*magnetic)))

    print(f'#{t} {deadlock(transposed)}')