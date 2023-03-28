def ncr(n, r, s):  # n개에서 r개를 고르는 조합, s : 선택할 수 있는 구간의 시작
    if r==0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            ncr(n, r-1, i+1)



n = 5
r = 3

A = list(range(n))
comb = [0]*r

ncr(n, r, 0)
