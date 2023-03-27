import heapq

def K_nearest_points_from_origin(points, K):
    '''
    function that extract top K nearest points in points from origin

    :param
    points (list) : list containing points (ex. [[x1, y1], [x2, y2]])
    K (int) : the number of points that we want to extract

    :return
    result (list) : list containing top K nearest points in points from origin
    '''

    # initialize our object
    result = []

    # for each point in points
    # compute squared euclidean distance from origin
    # pair it with coordinates
    points_with_distance = list(map(lambda pos: (pos[0]**2 + pos[1]**2, pos), points))

    # make it minimum heap
    heapq.heapify(points_with_distance)

    for _ in range(K):
        result.append(heapq.heappop(points_with_distance)[1])

    return result


points = [[3, 3], [5, -1], [-2, 4]]
K = 2
print(K_nearest_points_from_origin(points, K))