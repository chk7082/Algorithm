def palindrome1(arr, p_length):
    '''
    function that return the number of palindrome
    with length : p_length in arr

    :param
    arr (list) : list of string, where each string represent each row
    p_length (int) : integer representing the length of wanted palindrome

    :return:
    counts (int) : the number of palindrome we wanted
    '''

    # initialize our object
    counts = 0

    for i in range(8):
        for j in range(9 - p_length):
            # for horizontal palindrome
            cur_str = arr[i][j:j+p_length]
            if cur_str == cur_str[::-1]:
                counts += 1

            # for vertical palindrome
            # we don't need to join this list to string
            cur_str = [arr[k][i] for k in range(j, j+p_length)]
            if cur_str == cur_str[::-1]:
                counts += 1

    return counts


T = 10
arr_size = 8
for t in range(1, T+1):
    p_length = int(input())
    arr = [input() for _ in range(arr_size)]
    print(f'#{t} {palindrome1(arr, p_length)}')