def beginners_palindrome_check(string):
    '''
    function that return 1, if given string is valid palindrome
                         0, otherwise
    '''

    return int(string == string[::-1])

T = int(input())
for t in range(1, T+1):
    string = input()
    print(f'#{t} {beginners_palindrome_check(string)}')