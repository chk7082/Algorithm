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
            self.rear = self.size -1
        else:
            self.size = len(arr)
            self.content = arr
            self.front = 0
            self.rear = self.size - 1


def password_generator(arr):
    '''
    function that generate password by an iterative step
        iterative step consists of cycle
            1 cycle : for i in [1, 2, 3, 4, 5]:
                          1. dequeue first element
                          2. subtract it by i
                          3. append it to the last element
            if something becomes negative, make it 0 and then return it immediately
            -> our wanted password

    :param
    arr (list) : list containing original numbers

    :return
    result (str) : converted password
    '''

    # length of arr
    length = 8

    # our cycle
    cycle = [1, 2, 3, 4, 5]

    # save it in Queue instance
    queue = Queue(length, arr)

    # until return
    while True:
        # for each step in cycle
        for i in cycle:
            # subtract it
            queue.content[queue.front] -= i

            # check if it's non-positive
            if queue.content[queue.front] <= 0:
                queue.content[queue.front] = 0

                # when front == length - 1 -> front + 1 == length
                if queue.front == length - 1:
                    return ' '.join(map(str, queue.content))

                # else
                else:
                    return ' '.join(map(str, queue.content[(queue.front + 1) % length:] + queue.content[:(queue.rear + 2) % length]))

            queue.front = (queue.front + 1) % length
            queue.rear = (queue.rear + 1) % length


for _ in range(10):
    t = input()
    arr = list(map(int, input().split()))

    print(f'#{t} {password_generator(arr)}')
