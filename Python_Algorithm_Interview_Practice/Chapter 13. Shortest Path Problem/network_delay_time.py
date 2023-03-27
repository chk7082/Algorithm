import heapq

def network_delay_time(N, K, dist):
    '''
    function that return required minimum time for all vertices to receive signal
                         starting from vertex K
                         -1, if impossible

    :param
    N (int) : the number of vertices
    K (int) : index of the starting vertex
    dist (list) : matrix (2-dim'l list) of size (N+1) by (N+1)
                  where each element (i, j) denote the distance from vertex i to j
                  (if there's no directed edge -> inf
                  index 0 : dummy)

    :return
    result (int) : required minimum time for all vertices to receive signal
                   starting from vertex K
                   -1, if impossible
    '''

    # initialization of dijkstra
    visited = [True] + [False] * N
    min_dist_from_K = [inf] * (N+1)
    heap = []
    heapq.heappush(heap, (0, K))

    # until empty
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        # if we had visited there -> continue
        if visited[cur_node]:
            continue

        # otherwise
        else:
            # update it
            visited[cur_node] = True
            min_dist_from_K[cur_node] = cur_dist

            for destination, required_dist in dist[cur_node]:
                # if we hadn't visited there yet
                if (not visited[destination]) and (cur_dist + required_dist < min_dist_from_K[destination]):
                    min_dist_from_K[destination] = cur_dist + required_dist
                    heapq.heappush(heap, (min_dist_from_K[destination], destination))

    # if it's impossible
    if inf in min_dist_from_K[1:]:
        return -1
    # if it's possible
    else:
        return max(min_dist_from_K[1:])


times = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]

N = 8
K = 3

inf = 1e7

# index 0 : dummy
dist = [[] for _ in range(N+1)]

for u, v, w in times:
    dist[u].append((v, w))

print(network_delay_time(N, K, dist))