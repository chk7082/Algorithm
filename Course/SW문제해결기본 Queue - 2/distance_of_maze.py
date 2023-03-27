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


def distance_of_maze(N, arr):
    '''
    function that return the minimum distance from start(2) to end(3)
    (excluding start & end)
                  return 0, if there's no path between them

    :param
    N (int) : positive integer that represents the size of arr
    arr (list) : matrix (2-dim'l list) of size (N+2) by (N+2)
                 with border filled with wall(1)

    :return
    result (int) : the minimum distance from start(2) to end(3)
                   0, if there's no path between them
    '''

    # find start & end point
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 2:
                start_x, start_y = i, j
            elif arr[i][j] == 3:
                end_x, end_y = i, j

    # define possible actions
    # L R U D
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # initialize our queue
    # this q will contain [(pos_x, pos_y), current_distance]
    q = Queue(N*N)
    q.enQueue([(start_x, start_y), 0])

    # until empty
    while not q.isEmpty():
        # extract the first one
        pos, cur_dist = q.deQueue()

        # for its neighbor that we hadn't included in queue
        for action_index in range(4):
            new_x = pos[0] + dx[action_index]
            new_y = pos[1] + dy[action_index]

            # if new_pos is exactly the end point
            # done
            if new_x == end_x and new_y == end_y:
                return cur_dist

            if not arr[new_x][new_y]:
                q.enQueue([(new_x, new_y), cur_dist + 1])
                arr[new_x][new_y] = 1

    # if the end is not reachable from the start
    return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[1]*(N+2)] + [[1] + list(map(int, list(input()))) + [1]
                         for _ in range(N)] + [[1]*(N+2)]

    print(f'#{t} {distance_of_maze(N, arr)}')