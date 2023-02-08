def palindrome(N, M, arr):
    '''
    function that find length M palindrome horizontally & vertically
    in N by N matrix arr

    :param
    N (int) : positive integer representing the size of arr
    M (int) : positive integer representing the length of palindrome
    arr (list) : 2-dim'l array containing alphabets

    :return:
    palindrome (string) : length M palindrome in arr
    '''

    for i in range(N):
        for j in range(N-M+1):
            # for each starting point (i, j) find horizontal palindrome
            # check if it's palindrome
            cur_list = arr[i][j:j+M]
            if cur_list == cur_list[::-1]:
                return ''.join(cur_list)

            # for each starting point (j, i) find vertical palindrome
            # check if it's palindrome
            cur_list = [arr[k][i] for k in range(j, j+M)]
            if cur_list == cur_list[::-1]:
                return ''.join(cur_list)

    # for-else
    else:
        return "There is no Palindrome"


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    print(f'#{t} {palindrome(N, M, arr)}')