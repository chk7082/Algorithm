def cultivate_crops():
    '''
    function that return the total amount of money we could get
    '''

    # size of the farm
    N = int(input()) # odd
    radius = N//2

    # save only the areas that we'll cultivate
    farm = [list(map(int, list(input())))[abs(radius-i): N-abs(radius-i)]
            for i in range(N)]

    return sum(map(sum, farm))


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {cultivate_crops()}')