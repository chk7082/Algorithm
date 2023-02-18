def password(N, string):
    '''
    function that create a password by iterative elimination of repeated digits

    :param
    N (int) : the length of string
    string (str) : original string that we wanted to make corresponding password

    :return
    password (str) : password made by iterative elimination of repeated digits
    '''

    # use it as a stack
    password = []

    # for each character in string
    for char in string:
        # if password is nonempty & repeated char detected -> pop it
        if password and password[-1] == char:
            password.pop()

        # otherwise append it
        else:
            password.append(char)

    return ''.join(password)


T = 10
for t in range(1, T+1):
    N, string = input().split()
    N = int(N)
    print(f'#{t} {password(N, string)}')