arr = [3, 6, 7, 1, 5, 4]

# number of elements in arr
n = len(arr)

# 1<<n : total number of subsets of arr
for i in range(1<<n):
    # compare i's bit for n-many times
    # whether to know j-th element of arr is in this current subset or not
    for j in range(n):
        # if j-th bit of i is 1
        # include j-th element of arr
        if i & (1<<j):
            print(arr[j], end=", ")
    print()
print()

# 3,
# 6,
# 3, 6,
# 7,
# 3, 7,
# 6, 7,
# 3, 6, 7,
# 1,
# ...
# ...