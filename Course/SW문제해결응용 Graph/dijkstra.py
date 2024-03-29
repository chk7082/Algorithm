'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

def dijkstra(s, V):  # s 출발, V 마지막 정점 번호
    # U : 최소비용이 결정된 정점 집합 (set으로 in 연산보다 그냥 저렇게 리스트로 스위치처럼 하는게 편할듯)
    U = [0] * (V+1)
    U[s] = 1          # U = {s}

    for i in range(V+1):  # s에서 나머지 정점 i로 가는 비용 복사
        D[i] = adjM[s][i]
    
    # 남은 정점의 비용 결정
    N = V+1               # N개의 정점 (이미 1개 결정함, 출발점 => 비용 0)
    for _ in range(N-1):  # N-1개 정점의 비용 결정 (while로 하고 break 걸어도 갠춘)
        # D[w]가 최소인 w를 결정
        minV = INF
        w = 0

        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:  # 남은 정점 i 중, 최소
                w = i                      # 얘를 w의 후보로 둔다
                minV = D[i]

        # 이제 w 확정 => U에 포함시키자
        U[w] = 1    # 최소인 w는 기존 비용 D[w] 확정
        # w에 인접인 정점에 대해, 기존비용 vs w를 거쳐가는 비용 비교
        for v in range(V+1):
            # 0은 자기자신이니까 빼고
            if 0 < adjM[w][v] < INF:  # w에 인접인 v의 조건
                D[v] = min(D[v], D[w] + adjM[w][v])


INF = 1e8   # 문제에 따라서 조절
V, E = map(int, input().split())  # 0~V번 정점, E 간선 수
adjM = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0      # 자기자신으로 가는 비용 : 0

for _ in range(E):
    u, v, w = map(int, input().split())  # u -> v, w 가중치
    adjM[u][v] = w

# print(adjM)
D = [INF] * (V+1)

dijkstra(0, V)
print(D)