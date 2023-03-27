def ancient_ruins(N, M, arr):
    '''
    function that computes the longest ancient structure in ancient ruins (arr)

    :param
    N, M (int) : integer representing the size of arr
    arr (list) : N by M matrix (2-dim'l list) of '1'/'0'
                 '1', if the region is part of some structure
                 '0', otherwise

    :return
    result (int) : the longest ancient structure in ancient ruins (arr)
    '''

    # convert each row or column into string & split it with '0'
    # then calculate length of each element

    # initialize our result
    result = 0

    # for each row
    for row in arr:
        string = ''.join(row)
        max_substructure = max(map(lambda x: len(x), string.split('0')))

        if max_substructure > result:
            result = max_substructure

    # for each col
    for col in map(list, zip(*arr)):
        string = ''.join(col)
        max_substructure = max(map(lambda x: len(x), string.split('0')))

        if max_substructure > result:
            result = max_substructure

    return result


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]

    print(f'#{t} {ancient_ruins(N, M, arr)}')