N = 10
count = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            count += 1
            print(i, j, k)

print(count)