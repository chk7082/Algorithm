import heapq


def cheapest_airline_ticket(n, adjacency, src, dst, K):
    '''
    function that return the cheapest airline ticket
    with the number of stopover points <= K
    '''

    # since all the edges have positive distance -> use dijkstra

    # initialization
    can_visit = [True] * n
    inf = 1e7
    min_dist = [inf] * n
    min_dist[src] = 0

    heap = []
    heapq.heappush(heap, (0, -1, src)) # (dist, number of stopover points, node)

    # until it's empty
    while heap:
        cur_dist, cur_stopover, cur_v = heapq.heappop(heap)

        # ending condition
        # by the below condition, cur_stopover should be <= K
        if cur_v == dst:
            return cur_dist

        # if the min_dist of it isn't determined yet,
        elif can_visit[cur_v] and cur_stopover <= K - 1:
            can_visit[cur_v] = False

            # for each adjacent edges
            for new_v, needed_dist in adjacency[cur_v]:
                if cur_dist + needed_dist < min_dist[new_v]:
                    heapq.heappush(heap, (cur_dist + needed_dist, cur_stopover + 1, new_v))
                    min_dist[new_v] = cur_dist + needed_dist


n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 0

adjacency = [[] for _ in range(n)]
for v1, v2, dist in edges:
    adjacency[v1].append((v2, dist))

print(cheapest_airline_ticket(n, adjacency, src, dst, K))

