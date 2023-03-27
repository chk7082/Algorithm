def simple_prime_factorization(N):
    '''
    function that factorize N = 2^a * 3^b * 5^c * 7^d * 11^e
    (N should meets the condition)

    :param
    N (int) : positive integer that we want to factorize

    :return:
    exponents (list) : list containing each exponents
    '''

    # initialize it
    # exponents of 2, 3, 5, 7, 11 (int this order)
    exponents = [0] * 5

    # list of basis we want to use
    filter = [2, 3, 5, 7, 11]

    # for each base
    for i, base in enumerate(filter):

        # while N is divisible by base
        while not (N % base):
            # divide it with base & add 1 to corresponding exponents
            N //= base
            exponents[i] += 1

    return exponents

# number of test cases
T = int(input())

for t in range(1, T+1):
    N = int(input())
    exponents = simple_prime_factorization(N)

    print(f'#{t}', end='')
    for exponent in exponents:
        print(f' {exponent}', end='')

    print()
