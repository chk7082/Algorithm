def GNS(arr, decoder):
    '''
    function that sort alien numbers

    :param
    arr (list) : list containing alien numbers
    decoder (dict) : dictionary containing (key, value) = (alien_num, our_num)

    :return:
    result (list) : sorted arr (in ascending order)
    '''

    return sorted(arr, key = lambda alien_num : decoder.get(alien_num))


alien_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
decoder = {alien_num : i for i, alien_num in enumerate(alien_nums)}

T = int(input())
for t in range(1, T+1):
    # we don't need #t length
    _ = input()
    arr = input().split()
    sorted_arr = GNS(arr, decoder)
    print(f'#{t} ', end='')
    print(*sorted_arr, sep=' ')
