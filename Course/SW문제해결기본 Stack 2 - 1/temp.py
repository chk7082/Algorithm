def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)


N = 5
bit = [0]*N
f(0, 5)

