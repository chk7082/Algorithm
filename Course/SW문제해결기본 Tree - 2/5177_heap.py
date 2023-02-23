def heap(N, arr):
    '''
    function that return the list representing the minimum heap tree

    :param
    N (int) : length of arr
    arr (list) : list containing elements
                 that come in to our heap (sequentially)

    :return
    min_heap (list) : list representation of minimum heap (complete binary tree)
    '''

    # initialize our min_heap
    min_heap = [0] * (N+1)
    index_to_put = 1

    # for each element that come in to our heap
    for element in arr:
        # put it at the last (just to maintain the complete binary tree structure)
        min_heap[index_to_put] = element

        # initial child & parent index
        child = index_to_put
        parent = child // 2

        # update it for the next iteration
        index_to_put += 1

        # trace up until we meet the min_heap condition
        while child > 1 and min_heap[parent] > min_heap[child]:
            # swap it
            min_heap[parent], min_heap[child] = min_heap[child], min_heap[parent]

            # update child & parent
            child = parent
            parent = child // 2

    return min_heap





T = int(input())
for t in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    min_heap = heap(N, arr)

    cum_sum = 0
    N //= 2
    while N:
        cum_sum += min_heap[N]
        N //= 2

    print(f'#{t} {cum_sum}')
