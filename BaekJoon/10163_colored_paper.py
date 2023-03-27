def colored_paper(N):
    '''
    (colored_paper problem in BaekJoon 10163)
    function that print the visible area of each ordered papers

    :param
    N (int) : number of colored papers
    '''

    # initialize our plane
    plane = [[0]*1001 for _ in range(1001)]

    # for each ordered colored paper
    for i in range(1, N+1):
        # (x, y) : upper left position of that colored paper
        # having width & height
        # with (0, 0) : the top upper left
        y, x, width, height = map(int, input().split())

        # overwrite the previous color with current color
        for row in range(x, x+height):
            plane[row][y:y+width] = [i] * width

    # count our result
    # 0 index : dummy
    counts = [0] * (N+1)
    for row in plane:
        for num in row:
            if num:
                counts[num] += 1

    # print it
    for i in range(1, N+1):
        print(counts[i])


N = int(input())
colored_paper(N)