def spaceship_landing(N, M, arr):
    '''
    function that return the number of preliminary landing spots

    :param
    N, M (int) : integers representing the size of arr
    arr (list) : N by M matrix (2-dim'l list) containing heights of regions

    :return
    num_pre_landing_spots (int) : the number of preliminary landing spots
    '''

    # initialize our object
    num_pre_landing_spots = 0

    # for each points
    for i in range(N):
        for j in range(M):
            # initialize counts to count the number of neighbors which has lower altitude
            counts = 0

            # consider neighbors of (i, j)
            for x in range(max(i-1, 0), min(i+2, N)):
                for y in range(max(j-1, 0), min(j+2, M)):
                    if arr[x][y] < arr[i][j]:
                        counts += 1

            # if there are at least 4-many such neighbors
            if counts >= 4:
                num_pre_landing_spots += 1

    return num_pre_landing_spots




T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    # N by M matrix
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {spaceship_landing(N, M, arr)}')