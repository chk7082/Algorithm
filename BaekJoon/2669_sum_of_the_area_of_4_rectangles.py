def sum_of_the_area_of_4_rectangles():
    '''
    function that return the area of union of 4 rectangles
    '''

    # initialize our interest
    filled_in = [[0] * 100 for _ in range(100)]

    # for each rectangle, fill in the corresponding region
    for _ in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                filled_in[x][y] = 1

    return sum(map(sum, filled_in))


print(sum_of_the_area_of_4_rectangles())