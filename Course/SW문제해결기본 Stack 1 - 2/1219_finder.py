def finder(adjacent):
    '''
    function that return 1, if 99 is reachable from 0 in this graph specified by adjacent
                  return 0, otherwise

    :param
    adjacent (list) : list of list containing the information about vertices that
                      can be reached from each vertex

    :return
    result (int) : 1, if 99 is reachable from 0 in this graph specified by adjacent
                   0, otherwise
    '''

    # total number of vertices (some of them don't have any edges)
    V = 100

    # vertex starts from 0
    # True : if not visited, False otherwise
    not_visited = [True] * V

    # our target
    query_v1 = 0
    query_v2 = 99

    # initial point
    stack = [query_v1] + [0] * (V-1)
    top = 0  # top for stack
    not_visited[query_v1] = False

    # until stack is empty
    while top > -1:
        v = stack[top]
        for w in adjacent[v]:
            # if possible push
            if not_visited[w]:
                # visit w
                not_visited[w] = False
                top += 1
                stack[top] = w

                # check if it's query_v2
                # it means query_v2 is reachable from query_v1
                if w == query_v2:
                    return 1

                break
        # for-else, when there's no adjacent vertex of v
        # which hasn't been visited
        else:
            top -= 1

    # if it's unreachable
    return 0


while True:
    # if there's new t & E
    try:
        t, E = map(int, input().split())

        # initialize adjacency
        adjacent = [[] for _ in range(100)]

        # given flattened directed edges
        flattened_edges = list(map(int, input().split()))

        # for each edge, embed the info to adjacent
        for i in range(E):
            adjacent[flattened_edges[2*i]].append(flattened_edges[2*i+1])

        print(f'#{t} {finder(adjacent)}')

    # if there's no new line, i.e) no new t & E
    except:
        break