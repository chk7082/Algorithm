def fly_between_trains(D, A, B, F):
    '''
    function that computes the moving distance of fly
    before the collision of trains

    :param
    D (int) : distance between the forehead of trains
    A (int) : velocity of train A
    B (int) : velocity of train B
    F (int) : velocity of fly

    :return
    result (num) : moving distance for fly until collision of trains
    '''

    # we don't need to use infinite series
    # since the velocity of each A, B, fly is consistent through all time,
    # we just need to calculate the time difference between start and collision
    time_for_collision = D / (A + B)

    return time_for_collision * F


# number of test cases
T = int(input())

for t in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f'#{t} {fly_between_trains(D, A, B, F)}')