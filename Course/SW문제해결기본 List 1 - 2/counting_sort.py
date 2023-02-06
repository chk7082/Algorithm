def counting_sort(arr, max_val, mode='ascending'):
    count = [0] * (max_val + 1)
    result = [-1] * len(arr)

    for num in arr:
        count[num] += 1

    # ascending order
    if mode == 'ascending':
        # cumulative multiplcity
        # to make 0 ~ i -> there exists count[i]
        for i in range(1, len(count)):
            count[i] += count[i - 1]

    if mode == 'descending':
        for i in range(len(count)-2, -1, -1):
            count[i] += count[i + 1]

    # sorting process
    # by reducing 1 of count[arr[j]] at a time,
    # we could successfully index each element of result properly
    for j in range(len(arr)-1, -1, -1):
        count[arr[j]] -= 1
        result[count[arr[j]]] = arr[j]


    return result

temp = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(temp, max(temp), mode='ascending'))
print(counting_sort(temp, max(temp), mode='descending'))
# [0, 1, 1, 1, 2, 3, 4, 4]