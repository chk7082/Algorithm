def security_guard(width, height, N, shops, pos_guard):
    '''
    function that return the minimum possible distance sum from the
    security_guard & shops

    :param
    width (int) : width of the block
    height (int) : height of the block
    N (int) : number of shops (len(shops))
    shops (list) : list containing the position of shops
    pos_guard (tuple) : tuple containing the position of guard
                        (direction, distance)

    :return
    result (int) : the minimum possible distance sum
                   from the security_guard & shops
    '''

    # initialize our object
    result = 0

    # for each shop, compute the minimum distance from guard
    for pos_shop in shops:
        result += minimum_distance(width, height, pos_shop, pos_guard)

    return result


def minimum_distance(width, height, pos_shop, pos_guard):
    '''
    helper function that return the minimum distance between guard & shop
    '''

    # north : 1, south : 2, west : 3, east : 4
    # compute the manhattan distance
    # if those two direction is not opposite to each other,
    # then manhattan distance is what we wanted
    x_shop, y_shop = coordinate_converter(width, height, pos_shop)
    x_guard, y_guard = coordinate_converter(width, height, pos_guard)

    base_distance = abs(x_shop - x_guard) + abs(y_shop - y_guard)

    # if one lies on north & the other lies on south
    if {pos_shop[0], pos_guard[0]} == {1, 2}:
        base_distance += min(2 * min(y_shop, y_guard), 2 * (width - max(y_shop, y_guard)))

    # if one lies on west & the other lies on east
    elif {pos_shop[0], pos_guard[0]} == {3, 4}:
        base_distance += min(2 * min(x_shop, x_guard), 2 * (height - max(x_shop, x_guard)))

    return base_distance


def coordinate_converter(width, height, pos):
    '''
    helper function that convert (direction, distance) to (x, y) coordinate
    '''

    if pos[0] == 1:
        return (0, pos[1])
    elif pos[0] == 2:
        return (height, pos[1])
    elif pos[0] == 3:
        return (pos[1], 0)
    else:
        return (pos[1], width)


width, height = map(int, input().split())

# number of shops
N = int(input())

# position of shops
shops = [tuple(map(int, input().split())) for _ in range(N)]

# position of security guard (direction, distance)
pos_guard = tuple(map(int, input().split()))

print(security_guard(width, height, N, shops, pos_guard))