def pile_the_dice(N, dice):
    '''
    function that return the maximum possible summation of side face
    of piled dice,
    (the upper face of the lower one & the lower face for the upper one
    should have the same number)

    :param
    N (int) : the number of dice
    dice (list) : list of list containing the number combination of each die

    :return
    max_side_face_sum (int) : the maximum possible summation of side face of piled dice
    '''

    # each die in dice represents numbers in this way
    # A B C D E F where A-F, B-D, C-E denotes the opposite face pairs

    # if we determine the lower face of the lower one, then every lower & upper
    # face of each die would be determined

    # initialize our object
    max_side_face_sum = 0

    # for each lower face of dice 1
    for first in range(1, 7):
        side_faces = [set(range(1, 7)) for _ in range(N)]

        lower = first

        # for each level
        for level in range(N):
            upper = opposite_one(dice[level], lower)
            side_faces[level] -= set([lower, upper])

            # if it's the last level, break
            if level == N-1:
                break
            else:
                lower = upper

        # compute maximum sum in the current setting
        cur_max_sum = sum(map(max, side_faces))

        if cur_max_sum > max_side_face_sum:
            max_side_face_sum = cur_max_sum

    return max_side_face_sum


convertor = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}


def opposite_one(row, query):
    '''
    function that return the opposite one for the query
    '''

    return row[convertor[row.index(query)]]


# the number of dice
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

print(pile_the_dice(N, dice))