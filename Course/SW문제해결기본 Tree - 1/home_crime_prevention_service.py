def home_crime_prevention_service(N, M, building):
    '''
    function that return the maximum number of buildings that the
    crime prevention service can be offered without loss

    :param
    N (int) : integer that represent the size of the city
    M (int) : the amount of money that one house could pay
    building (list) : matrix (2-dim'l list) of size N by N
                      1, if there is building
                      0, otherwise

    :return
    max_num (int) : the maximum number of buildings that the
                   crime prevention service can be offered without loss
    '''

    max_num = 0

    # for each positive integer K that represents the size of service area
    for K in range(1, N+2):
        # compute the required number of building to avoid loss
        required_num = (K**2 + (K-1)**2 - 1)//M + 1

        # for each center position (i, j)
        for i in range(N):
            for j in range(N):
                # count the number of building on that service area
                building_count = 0

                # for each position in service area
                for x in range(max(i-K+1, 0), min(i+K, N)):
                    # compute K for current row
                    K_temp = K - abs(x-i)
                    for y in range(max(j-K_temp+1, 0), min(j+K_temp, N)):
                        # if there's building
                        if building[x][y]:
                            building_count += 1

                # if there's at least required_num & it's greater than or
                # equal to previous max_num -> update it
                if building_count >= max(max_num, required_num):
                    max_num = building_count

    return max_num


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    building = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {home_crime_prevention_service(N, M, building)}')