class Queue:
    '''
    class of Queue
    '''
    def __init__(self, size):
        self.size = size
        self.content = [0] * size
        self.front = -1
        self.rear = -1

    def enQueue(self, element):
        self.rear += 1
        self.content[self.rear] = element

    def deQueue(self):
        self.front += 1
        return self.content[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.size - 1


def distance_between_nodes(V, adjacent, S, G):
    '''
    function that computes the minimum distance from start(S) to end(G)

    :param
    V (int) : total number of vertices
    adjacent (list) : 2-dim'l list that represents the edges in each vertex
    S (int) : index of start
    G (int) : index of end

    :return
    result (int) : the minimum distance from start(S) to end(G)
                   0, if end is not reachable from start
    '''

    # initial setting
    q = Queue(V)
    q.enQueue(S)

    visited = [0] * (V+1)
    visited[S] = 1

    # until empty
    while not q.isEmpty():
        v = q.deQueue()

        # for each neighbor w of v
        for w in adjacent[v]:
            # if w is the end point
            if w == G:
                return visited[v]

            # if we hadn't visited w
            if not visited[w]:
                q.enQueue(w)
                visited[w] = visited[v] + 1

    # if G is not reachable from S
    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adjacent = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjacent[v1].append(v2)
        adjacent[v2].append(v1)

    S, G = map(int, input().split())

    print(f'#{t} {distance_between_nodes(V, adjacent, S, G)}')