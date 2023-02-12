def colored_paper(N):
    '''
    function that return the area of union of N colored papers
    '''

    # initialize our interest
    filled_in = [[0] * 100 for _ in range(100)]

    # for each colored paper, fill in the corresponding region
    for _ in range(N):
        x_left, y_up = map(int, input().split())
        for x in range(x_left, x_left+10):
            for y in range(y_up, y_up+10):
                filled_in[x][y] = 1

    return sum(map(sum, filled_in))


N = int(input())
print(colored_paper(N))