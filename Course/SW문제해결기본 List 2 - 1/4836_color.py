def color(boxes):
    '''
    function that return the number of boxes colored with both red & blue

    :param
    boxes (list) : list of list, where each list represent [r1, c1, r2, c2, color]
                   (r1, c1) : upper left corner of that box
                   (r2, c2) : lower right corner of that box
                   color : 1, if red
                           2, if blue
    :return
    result (int) : number or regions colored with both red & blue
    '''

    # initialize our result
    result = 0

    # initialize red_box & blue_box
    # 1, if it's spatial region is colored with corresponding color
    # 0, otherwise
    red_box = [[0]*10 for _ in range(10)]
    blue_box = [[0]*10 for _ in range(10)]

    # for each box in boxes
    for r1, c1, r2, c2, color in boxes:
        # if color : red
        if color == 1:
            for row in range(r1, r2 + 1):
                red_box[row][c1:c2 + 1] = [1] * (c2 - c1 + 1)
        # if color : blue
        elif color == 2:
            for row in range(r1, r2 + 1):
                blue_box[row][c1:c2 + 1] = [1] * (c2 - c1 + 1)

    # compute our result
    for i in range(10):
        for j in range(10):
            if red_box[i][j] & blue_box[i][j]:
                result += 1

    return result

# number of test cases
T = int(input())

for t in range(1, T+1):
    N = int(input())
    boxes = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {color(boxes)}')





