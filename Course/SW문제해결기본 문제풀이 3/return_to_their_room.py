def return_to_their_room(N):
    '''
    function that return minimum required time for students to go to their room

    :param
    N (int) : number of students who must go to their room

    :return
    result (int) : minimum required time for students to go to their room
    '''

    # for each corridor space, count the number of students
    # who should pass that space
    corridor_counter = [0]*200

    for _ in range(N):
        # map it w.r.t the indices of corridor_counter
        start, end = map(lambda x: (int(x)-1)//2, input().split())

        # if start > end -> swap it
        if start > end:
            start, end = end, start

        # count it
        corridor_counter[start: end + 1] = map(lambda x: x+1, corridor_counter[start: end + 1])

    return max(corridor_counter)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t} {return_to_their_room(N)}')