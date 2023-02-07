def my_sort(arr, N):
    '''
    function that sort arr internally
    (in ascending order)
    (using selection sort)

    :param
    arr (list) : list of array that we want to sort

    :return
    None, just overwrite arr
    '''

    for i in range(N-1):
        # initialize min_val & min_index
        min_val = arr[i]
        min_index = i

        # find true min_val & min_index
        for j in range(i+1, N):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j

        # swap it
        arr[i], arr[min_index] = min_val, arr[i]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    my_sort(arr, N)
    print(f'#{t} ', end='')
    for num in arr:
        print(num, end=' ')
    print()