def exponentiation(base, exponent):
    '''
    function that compute base^exponent
    '''

    # trivial cases
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base

    # when exponent >= 2
    # use recursion
    # when exponent is odd
    if exponent % 2:
        new_base = exponentiation(base, (exponent-1)//2)
        return new_base * new_base * base
    # when even
    else:
        new_base = exponentiation(base, exponent//2)
        return new_base * new_base


T = 10
for t in range(1, T+1):
    _ = input()
    base, exponent = map(int, input().split())
    print(f'#{t} {exponentiation(base, exponent)}')