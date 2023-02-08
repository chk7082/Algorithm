def practice1_reverse(string):
    '''
    function that return reversed string
    :param
    string (str) : string that we want to reverse

    :return
    result (str) : reversed string
    '''

    return string[::-1]

T = int(input())
for t in range(1, T+1):
    string = input()
    print(f'#{t} {practice1_reverse(string)}')