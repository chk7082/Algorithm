class Queue:
    '''
    class of Queue
    '''
    def __init__(self, size, arr = None):
        self.size = size

        # if arr is None, use size to initialize it
        if not arr:
            self.content = [0] * size
            self.front = 0
            self.rear = -1
        else:
            self.size = len(arr)
            self.content = arr
            self.front = 0
            self.rear = self.size - 1


def pizza(N, M, C):
    '''
    function that return the index of pizza which remains in fire pot at the end

    :param
    N (int) : the size of fire pot
    M (int) : the total number of pizza
    C (list) : the amount of cheese in each pizza

    :return
    result (int) : the index of pizza which remains in fire pot at the end
    '''

    # index for entering pizza
    index = N

    # original pizza indices for each current position of fire pot
    original_indices = list(range(N))

    # initial pizza in the fire pot
    fire_pot = Queue(N, C[:N])

    # number of pizza in fire pot
    num_of_pizza_in_fire_pot = N

    # stage 1 : until we put all the pizza in the fire pot
    while index < M:
        # if it's 0
        if not fire_pot.content[fire_pot.front]:
            # change it to next pizza
            fire_pot.content[fire_pot.front] = C[index]
            original_indices[fire_pot.front] = index
            index += 1

        # melt it for the next loop
        fire_pot.content[fire_pot.front] //= 2
        fire_pot.front = (fire_pot.front + 1) % N
        fire_pot.rear = (fire_pot.rear + 1) % N

    # stage 2 : we can't put new one
    # find the last remaining one
    # convert it to binary & compute length
    # find the first index that makes the maximum from the last
    binary_length = list(map(lambda x: len(bin(x)), fire_pot.content))
    cur_index = fire_pot.rear
    max_val = -1
    max_index = -1
    for _ in range(N):
        # when we need to update
        if binary_length[cur_index] > max_val:
            max_val = binary_length[cur_index]
            max_index = cur_index

        # update for the next iteration
        cur_index = (cur_index - 1) % N

    # since original pizza index starts from 0
    return original_indices[max_index] + 1


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    print(f'#{t} {pizza(N, M, C)}')

