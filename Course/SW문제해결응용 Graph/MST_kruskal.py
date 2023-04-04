'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


def find_set(x):        # x가 속한 집합의 대표 리턴
    while x != rep[x]:  # 같을 때까지 계속 찾아가줘, x == rep[x]가 될 때까지
        x = rep[x]      # 그 집합의 대표를 찾을 때까지
    return x


def union(x, y):
    # y가 속한 집합의 대표원소가 자기자신을 가리키고 있었을텐데
    # 걔가 가리키던 걸 x의 대표원소로 바꿔줘
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split()) # 0~V 정점번호, E : edge의 개수
# makeset()
rep = [i for i in range(V+1)]
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])   # append 하기 싫으면 크기를 미리 읽어서 거기다가 넣어도 갠춘

# (1) 가중치 기준 오름차순 정렬
graph.sort(key=lambda x: x[2])  # 이걸 쓰기 싫으면, w를 앞에다가 저장하면 될듯 => 바로 sort 가능
# print(graph)

# (2) N개 정점(V+1)에 대해서, N-1개의 간선 선택
N = V + 1
s = 0        # MST에 포함된 간선의 가중치 합
cnt = 0
MST = []     # MST가 어떤 얘들로 구성되었는지 확인하려면
for u, v, w in graph:  # 가중치가 작은 것부터...
    if find_set(u) != find_set(v):  # 사이클이 생기지 않으면
        cnt += 1
        s += w         # 가중치 합
        MST.append([u, v, w])
        union(u, v)    # 그래야 나중에 cycle이 생기는걸 막는다
                       # => edge로 연결되었으니, 같은 서로소집합에 들어가는거 생각
        if cnt == N-1:
            break

print(MST)
print(s)

