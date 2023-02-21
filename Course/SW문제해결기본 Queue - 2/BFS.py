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


def BFS(V, start_v, adjacent):
    '''
    function that return the path of BFS route (starting from start_v)

    :param
    V (int) : total number of vertices
    start_v (int) : the index of starting vertex
    adjacent (list) : 2-dim'l list that represents the edges in each vertex

    :return
    path (list) : list containing the path of BFS route
    '''

    # initialize our object
    path = []

    # initialize visited
    # index 0 : dummy
    visited = [0] * (V+1)

    # initialize our queue
    q = Queue(V)
    q.enQueue(start_v)
    visited[start_v] = 1

    # until queue is empty
    while not q.isEmpty():
        # dequeue first element
        v = q.deQueue()
        path.append(v)

        # for each neighbor of v, which we hadn't visited yet
        for w in adjacent[v]:
            if not visited[w]:
                q.enQueue(w)
                visited[w] = 1

    return path


V, E = map(int, input().split())
adjacent = [[] for _ in range(V+1)]

edges = list(map(int, input().split()))
for v1, v2 in zip(edges[::2], edges[1::2]):
    adjacent[v1].append(v2)
    adjacent[v2].append(v1)

path = BFS(V, 1, adjacent)
print(*path, sep='-')
