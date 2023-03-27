# def n_queen(a, k, N):
#     '''
#     function that computes the number of cases that N-many queens can be placed
#     in N by N chessboard s.t none of them can attack the others
#
#     :param
#     a (list) : current array info (ith element -> column index of queen in row i)
#     k (int) : current length of a
#     N (int) : size of chessboard & number of queens
#
#     :return
#     result (int) : the number of cases that N-many queens can be placed
#                    in N by N chessboard s.t none of them can attack the others
#     '''
#
#     # if it's valid queen placements
#     if k == N - 1:
#         global result
#         result += 1
#
#     # not yet
#     else:
#         k += 1
#
#         for i in range(N):
#             a[k] = i
#             if promising(k):
#                 n_queen(a, k, N)
#
#
# def promising(k):
#     '''
#     helper function that tell us whether a[:(k+1)] is valid or not
#     '''
#
#     for i in range(k):
#         # if col indices are equal
#         # or vertical difference is equal to horizontal difference
#         if a[k] == a[i] or k - i == abs(a[k] - a[i]):
#             return False
#     else:
#         return True
#
# result = 0
#
# N = int(input())
# k = -1
# a = [0] * N
# n_queen(a, k, N)
# print(result)


# use pypy3 & erase all comments
n = int(input())
ans = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(ans)