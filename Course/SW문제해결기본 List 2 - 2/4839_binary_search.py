def binary_search(P, page_num):
    '''
    function that return the total number of binary search step
    to find page_num in P-page book

    :param
    P (int) : total number of page
    page_num (int) : exact page that we want to find

    :return
    iteration (int) : total number of binary search step to find page_num
                      in P-page book
    '''

    # initialize iteration & left, right page of our interest
    iteration = 0
    l = 1
    r = P

    # safe guard
    # when it's impossible
    if P < page_num or page_num < 1:
        return -1

    # binary search step
    # by our safe guard, this algorithm always terminate successfully
    # i.e we could always find sol exactly without checking l <= r
    # (since the page contains all integers between 1 ~ P)
    while True:
        iteration += 1

        # center
        c = (l + r) // 2

        # binary search step
        if c == page_num:
            return iteration
        elif page_num < c:
            r = c #- 1
        else: # when c < page_num
            l = c #+ 1


T = int(input())
for t in range(1, T+1):
    P, A, B = map(int, input().split())

    # compute iteration for each person
    iter_A = binary_search(P, A)
    iter_B = binary_search(P, B)

    print(f'#{t} ', end='')
    if iter_A < iter_B:
        print('A')
    elif iter_B < iter_A:
        print('B')
    else: # when tie
        print(0)



