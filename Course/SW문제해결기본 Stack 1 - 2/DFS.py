def DFS(V, E, edges):
    '''
    function that return the path of the DFS process in given graph

    :param
    V (int) : number of vertices
    E (int) : number of edges
    edges (list) : list of length 2*E containing edge representations
                   (two vertices -> determine one edge)

    :return:
    path (list) : path of the DFS process in given graph
    '''

    # vertex starts from 1 (0 : dummy)
    # True : if not visited, False otherwise
    not_visited = [True] * (V+1)

    # arrange adjacency using edges
    adjacent = [[] for _ in range(V+1)]

    # update adjacency
    for i in range(E):
        v1, v2 = edges[2*i], edges[2*i+1]
        adjacent[v1].append(v2)
        adjacent[v2].append(v1)

    # initial point
    stack = [1] + [0]*(V-1)
    top = 0 # top for stack
    not_visited[1] = False

    # initialize our result (path)
    path = [1]

    # until stack is empty
    while top > -1:
        v = stack[top]
        for w in adjacent[v]:
            # if possible push
            if not_visited[w]:
                # visit w
                not_visited[w] = False
                path.append(w)
                top += 1
                stack[top] = w
                break
        # for-else, when there's no adjacent vertex of v
        # which hasn't been visited
        else:
            top -= 1

    return path


V, E = map(int, input().split())
edges = list(map(int, input().split()))

print(*DFS(V, E, edges), sep=' ')



