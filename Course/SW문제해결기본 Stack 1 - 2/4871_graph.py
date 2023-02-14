def graph(V, adjacent, query_v1, query_v2):
    '''
    function that return 1, if query_v2 is possibly reachable from query_v1
                         0, otherwise

    :param
    V (int) : the number of vertices
    adjacent (list) : list of list containing the information of vertices that
                      can be reached from each vertex
    query_v1 (int) : starting vertex
    query_v2 (int) : ending vertex

    :return
    result 1, if query_v2 is possibly reachable from query_v1
           0, otherwise
    '''

    # vertex starts from 1 (0 : dummy)
    # True : if not visited, False otherwise
    not_visited = [True] * (V+1)

    # initial point
    stack = [query_v1] + [0]*(V-1)
    top = 0 # top for stack
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


# number of test cases
T = int(input())

for t in range(1, T+1):
    # number of vertices and edges
    V, E = map(int, input().split())

    # initialize adjacency
    # 0 for dummy
    adjacent = [[] for _ in range(V+1)]

    # for each edge
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjacent[v1].append(v2)

    # check for the query
    query_v1, query_v2 = map(int, input().split())
    print(f'#{t} {graph(V, adjacent, query_v1, query_v2)}')

