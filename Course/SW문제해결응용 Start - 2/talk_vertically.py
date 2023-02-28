def talk_vertically(words):
    '''
    function that return the vertical string representation of words

    :param
    words (list) : list containing strings

    :return
    result (str) : vertical string representation of words
    '''

    # find the maximum length of the strings
    max_len = max(map(len, words))

    # left justified version
    enlarged_string = list(map(lambda string: string.ljust(max_len, '-'), words))

    # delete all '-'
    return (''.join(map(''.join, zip(*enlarged_string)))).replace('-', '')


T = int(input())
for t in range(1, T+1):
    words = [input() for _ in range(5)]
    print(f'#{t} {talk_vertically(words)}')
