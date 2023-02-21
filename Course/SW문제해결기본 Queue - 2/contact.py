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


def contact(V, start, adjacent):
    '''
    function that return the index of person who receive contact for the last time
    (when tie, return the largest index among them)

    :param
    V (int) : total number of vertices
    start (int) : index of start point
    adjacent (list) : 2-dim'l list that represents the edges in each vertex

    :return
    max_index (int) : the index of person who receive contact for the last time
    '''

    # initial setting
    q = Queue(V)
    q.enQueue(start)

    visited = [0] * (V+1)
    visited[start] = 1

    # until empty
    while not q.isEmpty():
        v = q.deQueue()

        # for each neighbor w of v
        for w in adjacent[v]:

            # if we hadn't visited w
            if not visited[w]:
                q.enQueue(w)
                visited[w] = visited[v] + 1

    # return the index that makes the maximum visited value
    # when tie, return the largest index among them
    max_val = -1
    max_index = V

    for v in range(V, 0, -1):
        if visited[v] > max_val:
            max_val = visited[v]
            max_index = v

    return max_index


T = 10
V = 100
for t in range(1, T+1):
    _, start = map(int, input().split())
    edges = list(map(int, input().split()))

    adjacent = [[] for _ in range(V+1)]
    for v1, v2 in zip(edges[::2], edges[1::2]):
        # since it's directed graph
        adjacent[v1].append(v2)

    print(f'#{t} {contact(V, start, adjacent)}')

