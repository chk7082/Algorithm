def perm(i, k):
    if i==k:
        print(*p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
perm(0, 3)