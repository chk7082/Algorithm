# 그래프(Graph)

> 실제 세계의 현상이나 사물을 노드(Node)와 간선(Edge)으로 표현하는 자료구조

-   아이템들 간의 **연결 관계**를 표현
-   정점 (Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성
-   `|V|` 정점의 개수
-   `|E|` 간선의 개수
-   선형 자료 구조나 트리로 표현하기 어려운 **N:N 관계 표현** 가능

## 1. 주요 용어 정리

-   **`노드(Node)` == `정점(Vertex)`**
    -   **위치**를 의미한다.
-   **`간선(Edge)`**
    -   **위치들을 연결한 선**을 의미한다.
-   `인접 정점(Adjacent Vertex)`
    -   특정 정점(노드)에서 간선으로 직접 연결된 정점(노드)

## 2. 그래프의 종류

### 2.1 무방향 그래프(Undirected Graph)

💡 **방향이 없는 그래프**

-   노드는 간선을 통해 양방향으로 갈 수 있다.
-   일반적으로 노드 A, B가 연결되어 있는 경우 (A, B) 혹은 (B, A)로 표기한다.
-   **정점의 차수(Degree)**
    -   무방향 그래프에서 **하나의 정점에 인접한 정점의 개수**
    -   A의 차수는 2(B, C)
![Pasted image 20230404092809](https://user-images.githubusercontent.com/79408992/229664750-107d7f56-58e4-46b7-9f2e-2886945dbeab.png)
### 2.2 방향(유향) 그래프(Directed Graph)

💡 **간선에 방향이 있는 그래프**



-   일반적으로 노드 A, B가 A→B로 가는 간선이 연결되어 있을 때, <A, B>로 표기한다.
    -   <B, A>는 B→A로 가는 간선이므로 <A, B>와 다르다.
-   **진입차수(In-Degree)**
    -   방향 그래프에서 **외부에서 오는 간선**의 수
    -   D의 진입차수는 2(B→D, C→D), C의 진입차수는 1(A→C)
-   **진출차수(Out-Degree)**
    -   방향 그래프에서 **외부로 향하는 간선**의 수
    -   D의 진출차수는 0, C의 진출차수는 1(C→D)
![Pasted image 20230404092845](https://user-images.githubusercontent.com/79408992/229664818-1df1f550-5154-4194-96d4-3597f234f0b0.png)

### 2.3 가중치 그래프(Weighted Graph) 또는 네트워크(Network)

💡 **간선에 비용 또는 가중치가 할당된 그래프**



-   두 노드 간의 **최소 비용 경로(최단 경로)**를 찾는 문제가 유명하다.
    -   예를 들어 노드를 도시라고 생각하고, 간선을 도시를 연결하는 도로라고 가정하자. 간선에 매겨진 가중치는 이동하는데 걸리는 비용(시간, 통행료, 기름값 등)이라고 모델링할 수 있다.
    -   서울에서 광주로 이동하는데 걸리는 비용
        -   서울 → 구미 → 광주 : 9
        -   서울 → 대전 → 광주 : 3 (⇒ 최소비용)
![Pasted image 20230404092915](https://user-images.githubusercontent.com/79408992/229664877-528d1e71-6922-41bd-91f8-1ce6c54e8eae.png)
### 2.4 연결 그래프(Connected Graph)와 비연결 그래프(Disconnected Graph)

-   **연결 그래프**
    
    -   무방향 그래프에 있는 **모든 노드의 경로가 존재**하는 경우
![Pasted image 20230404092944](https://user-images.githubusercontent.com/79408992/229664932-6b8e75e7-50a1-497e-8fcd-ef095801b003.png)

        
        
-   **비연결 그래프**
    
    -   무방향 그래프에서 **특정 노드의 경로가 존재하지 않**는 경우
        
![Pasted image 20230404092955](https://user-images.githubusercontent.com/79408992/229665023-61f18245-333b-4880-b9fb-e88b8532ffdc.png)

### 2.5 완전 그래프

💡 그래프의 **모든 노드가 서로 연결**되어 있는 그래프
![Pasted image 20230404093021](https://user-images.githubusercontent.com/79408992/229665054-3cb23a1f-9b3d-4237-b6ef-1fe2a7fff1fe.png)
## 3. 그래프 성질 및 표현

### 3.1 그래프 성질

-   인접(Adjacency)
    -   두 개의 정점에 간선이 존재하면 서로 인접
    -   완전 그래프에 속한 모든 정점은 서로 인접
-   경로(Path)
    -   간선을 순서대로 나열한 것
    -   단순 경로 : 경로 중 한 정점을 최대 한 번만 지나는 경로
    -   **사이클(Cycle)** : 시작한 정점에서 끝나는 경로 (1 - 3 - 5 - 1)
-   차수
    -   각 노드에 연결된 간선의 수

### 3.2 그래프 표현

-   **인접 행렬(Adjacent matrix)**
    -   |V| * |V| 행렬로 표현
    -   연결 되어있으면 1로 표현, 아닐 경우 0
    -   데이터가 없는 공간이 큼 (**공간 비효율**)
-   **인접 리스트(Adjacent List)**
    -   각 정점에 대한 인접 정점들을 순차적으로 표현
    -   연결 리스트(Linked List)로 저장
-   간선의 배열

### 3.3 그래프 vs 트리

💡 **트리는 그래프의 하위 개념**이다.

|   | 그래프 | 트리 |
| ----| -------|-----|
|  정의    |  노드와 간선으로 표현되는 자료구조      |그래프의 한 종류로, 방향성이 있는 비순환 그래프     |
|  방향성    |    방향 그래프O, 무방향 그래프O    |  방향 그래프O, 무방향 그래프X   |
| 루트 노드|     X   |   O  |
|부모/ 자식관계 |   X  |  O   |     |





---

## 4. 서로소 집합

### 4.1 개념

-   **서로소 집합(Disjoint-sets)**
    -   “상호 배타적 집합”
    -   서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합 = 교집합이 없음
    -   한 집합 내부에 다른 특성을 갖는 집합을 배제 한다는 의미
    -   집합에 속한 **하나의 대표자(representative)를 통해 각 집합을 구분**
-   서로소 집합을 표현하는 방법
    -   리스트, 연결 리스트

### 4.2 3가지 연산 방법

> 주로 **`Find set`** 연산을 사용하여 노드의 대표 원소를 알아내는데 사용

1.  **`Make set`** : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

-   내 번호와 같은 Index에 놓는 작업
    
    ```python
    # p: 노드 x 의 부모 저장
    # rank: 루트 노드가 x 인 트리의 랭크값 저장
    
    def Make_Set(x):
        p[x] = x
        rank[x] = 0
    ```
    

2.  **`Find set`** : x를 포함하는 집합을 찾는 연산

-   내용물이 내 Index와 같으면, 내 집합의 대표자를 찾음
    
-   나 자신을 가리키는 원소를 찾을 때 까지 찾다가, 자기 자신을 가리키는 원소가 있으면 리턴
    
    ```python
    def Find_Set(x):
        if x == p[x]:
            return x
        else:
            return Find_Set(p[x])
    ```
    

3.  **`Union`** : x와 y를 포함하는 두 집합을 통합하는 연산

-   대표 원소가 다른 집합의 대표 원소를 가리키도록 변경
    
    ```python
    def Union(x, y):
        # p[Find_Set(y)] = Find_Set(x)
        Link(Find_set(x), Find_set(y))
    
    def Link(x, y):
        if rank[x] > rank[y]:
            p[y] = x
        else:
            p[x] = y
    
        if rank[x] == rank[y]:
            rank[y] += 1
    ```
    
-   **Rank를 이용한 Union**
    
    -   subtree의 높이를 랭크로 저장
    -   루트에서 노드에 이르는 간선의 수를 의미
    -   이러한 방법을 사용하는 이유는 루트를 찾아가는데 필요한 연산을 최소한으로 줄이기 위함
 
- path compression

![Pasted image 20230404093636](https://user-images.githubusercontent.com/79408992/229665093-6aeb066f-579b-4bac-a177-eb9cbb08a793.png)

> 찾는 h의 경로에 있는 정점들을 모두 루트 정점을 가리키게 하는 작업



# 최소 신장 트리(Minimum Spanning Tree, MST)

### ****Spanning Tree (신장 트리)****

💡 그래프 내의 모든 정점을 포함하는 트리

![Pasted image 20230404093736](https://user-images.githubusercontent.com/79408992/229665120-9a15f2ea-e6db-4f4a-bb44-ca28f623a25d.png)

-   그래프에서 일부 간선을 선택해서 만든 트리
-   그래프의 **최소 연결 부분 그래프**
    -   최소 연결 == 간선의 수가 가장 적음
    -   예시) n개의 정점을 가지는 그래프의 최소 간선의 수는 (n-1)개이고, (n-1)개의 간선으로 연결되어 있으면 필연적으로 트리 형태가 되고 이것이 바로 Spanning Tree가 됨


### MST

<aside> 💡 Spanning Tree 중에서 사용된 간선들의 가중치 합이 최소인 트리

</aside>

**개념**

-   그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
    
    → 모든 노드가 포함되어 연결되면서 사이클이 존재하지 않는 그래프 → 트리
    
-   간선에 가중치를 고려하여 최소 비용의 이동경로를 선택
    
-   **모든 노드를 연결할 때 가장 적은 비용이 드는 방법을 찾아라!**
    
![Pasted image 20230404093802](https://user-images.githubusercontent.com/79408992/229665155-5e51f841-e3ec-47ac-b5c2-070a1f8c5f3a.png)


**조건(특징)**

-   간선의 가중치의 합이 최소여야 한다.
-   n개의 정점을 가지는 그래프에 대해 반드시 (n-1)개의 간선만을 사용해야 한다.
-   사이클이 포함되어서는 안된다.

## MST 구현 방법

### 1. Prim 알고리즘

**개념**

-   시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장 해나가는 방법
-   하나의 정점에서 연결된 간선들 중에서 하나씩 선택하면서 MST를 만들어 가는 방식
-   임의 정점을 하나 선택
    -   선택한 정점과 **인접하는 정점들 중, 최소 비용의 간선이 존재하는 정점을 선택**

**조건**

-   정점 선택을 기반으로 하는 알고리즘
    
-   임의의 간선을 선택하고 선택한 간선의 정점으로부터 가장 낮은 가중치를 갖는 정점을 선택
    
    -   이전 단계에서 만들어진 신장 트리를 확장
    -   모든 정점이 선택될 때까지 반복
    
![Pasted image 20230404093835](https://user-images.githubusercontent.com/79408992/229665175-61fc2955-88d1-4072-8e81-787f4797b6c8.png)
- 수도 코드 파이썬 변환
```python
def MST_PRIM(G, s): # G: 그래프, s: 시작점
    key = [INF] * N # 가중치를 무한대로 초기화 (최대값으로 설정)
    pi = [None] * N # 트리에서 연결될 부모 정점 초기화
    visited = [False] * N # 방문 여부 초기화
    key[s] = 0 # 시작 정점의 가중치를 0 으로 설정

    for _ in range(N):
        minIndex = -1
        min = INF
        for i in range(N):
            # 방문 안한 정점중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < min:
                min = key[i]
                minIndex = i
        visited[minIndex] = True # 최소 가중치 정점 방문 처리

        for v, val in G[minIndex]: # 선택 정점의 인접한 정점
            if not visited[v] and val < key[v]:
                key[v] = val       # 가중치 갱신
                pi[v] = minIndex   # 트리에서 연결될 부모 정점
```

- 실사용 코드 
```python
"""
5 6
1 2 3
1 3 7
2 3 1
3 4 4
2 5 2
5 4 2
"""

def prim(start, V):  # MST 가중치의 합을 리턴하는 함수. 1~V번 노드인 경우
    key = [INF] * (V + 1)  # key[i] i가 MST에 연결되는 비용
    key[1] = 0
    MST = [0] * (V + 1)
    pi = [0] * (V + 1)

    for _ in range(V):  # 모든 정점이 MST에 포함될 때 까지
        # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
        u = 0
        minV = INF

        for i in range(1, V + 1):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1  # key[u]가 최소인 u를 MST에 추가

        for v in range(V + 1):  # u에 인접인 v에 대해
            if MST[v] == 0 and adj[u][v] != 0:
                if key[v] > adj[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 MST에 연결된다면
                    key[v] = adj[u][v]
                    pi[v] = u  # v는 u와 연결해서 MST에 포힘될 예정

    return sum(key[start:])  # MST 가중치의 합 리턴

V, E = map(int, input().split())
INF = 10000
# 인접행렬
adj = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w  #  무방향 그래프에서 MST 구성

# print(prim(0, V))  # 노드 시작 번호 0인 경우(교재 예시)
print(prim(1, V))  # 노드 시작 번호 1인 경우(코드 주석의 예시)
```

```python
# 우선순위큐를 사용하지 않는 코드
'''
5 6
1 2 3
1 3 7
2 3 1
3 4 4
2 5 2
5 4 2
'''

V, E = map(int, input().split())
INF = 10000
# 인접행렬
adj = [[INF]*(V+1) for _ in range(V+1)]

for i in range(V+1):
    adj[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w  #  무방향 그래프에서 MST 구성

key = [INF]*(V+1)  # key[i] i가 MST에 연결되는 비용
key[1] = 0
MST = [0] * (V+1)
pi = [0] * (V+1)

for _ in range(V):  # 모든 정점이 MST에 포함될 때 까지
    # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
    u = 0
    minV = INF
    for i in range(1, V+1):
        if MST[i]==0:
            if key[i] < minV:
                u = i
                minV = key[i]
    MST[u] = 1  # key[u]가 최소인 u를 MST에 추가
    for v in range(1, V+1):  # u에 인접인 v에 대해
        if MST[v] == 0 and u!=v and adj[u][v]< INF:
            if key[v] > adj[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 MST에 연결된다면
                key[v] = adj[u][v]
                pi[v] = u    # v는 u와 연결해서 MST에 포힘될 예정
print(key)
print(pi)
```

### 2. Kruskal 알고리즘

-   대표적인 MST 알고리즘
-   그리디 알고리즘
-   간선을 하나씩 선택해서 MST를 찾는 알고리즘
-   최초, **모든 간선을 가중치에 따라 오름차순으로 정렬**
-   **가중치가 낮은 간선부터** 선택하면서 트리를 증가시킴
-   사이클이 존재하면 다음으로 가중치가 낮은 간선을 선택
-   n-1 개의 간선이 선택될 때 까지 반복

**동작 과정**

1.  간선 데이터를 비용에 따라 오름차순으로 정렬
2.  간선 데이터를 확인하며 형제의 간선이 사이클을 발생시키는지 확인
	1.  사이클이 발생하지 않는 경우 MST에 **포함**
	2.  사이클이 발생하는 경우 MST에 **포함 X**
3. 모든 간선에 대하여 2번 위 과정을 반복
![Pasted image 20230404094110](https://user-images.githubusercontent.com/79408992/229665216-bccaed98-2081-4ed6-bf22-21d3e8a2e5eb.png)

- 수도 코드 파이썬 변환
```python
def MST_KRUSKAL(G):
    mst = []

    for i in range(N):
        Make_Set(i)

    G.sort(key = lambda t:t[2]) # 가중치 기준으로 정렬
    mst_cost = 0 # MST 가중치

    while len(mst) < N-1:
        node_a, node_b, weight = G.pop(0) # 최소 가중치 간선 가져오기
        if Find_Set(node_a) != Find_Set(node_b): # 다른 집합인지 확인
            Union(node_a, node_b)
            mst.append((node_a, node_b)) # 트리에 (node_a, node_b) 추가
            mst_cost += weight
```

- 실사용 코드
```python
"""
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
"""

def find_set(x):
    while x != p[x]:  # 대표원소가 아니면
        x = p[x]  # x가 가리키는 정점으로 이동
    return x

V, E = map(int, input().split())
edge = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))
    
edge.sort()  # 가중치 기준 오름차순 정렬

p = [i for i in range(V + 1)]  # 대표원소 초기화

# N개의 정점이 있으면 사이클이 생기지 않도록 N-1개의 간선을 선택
# MST에 포함된 간선의 가중치의 합 구하기
N = V + 1  # 0~V번 까지의 정점
cnt = 0
total = 0  # 가중치의 합

for w, u, v in edge:  # N-1개의 간선 선택 루프
    if find_set(u) != find_set(v):  # 사이클을 형성하지 않으면 선택
        cnt += 1
        total += w  # 가중치의 합
        p[find_set(v)] = find_set(u)  # v의 대표원소를 u의 대표원소로 바꿈
        if cnt == N - 1:
            break
print(total)
```

### 3. 다익스트라(Dijkstra) 알고리즘

<aside> 💡 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산

</aside>

-   간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
-   시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방법
    -   `최단 경로` 알고리즘 중 가장 유명한 것이 다익스트라 알고리즘
-   다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
    -   그리디 기법을 사용한 알고리즘으로 프림 알고리즘과 유사
    -   매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
    -   BFS를 이용
-   단순하고 실행 속도 빠름
-   음(`-`)의 간선은 고려되지 않음
![Pasted image 20230404094211](https://user-images.githubusercontent.com/79408992/229665254-44343b50-e186-44eb-9458-e65910236226.png)
![Pasted image 20230404094219](https://user-images.githubusercontent.com/79408992/229665325-5a983506-6f19-47b0-ac65-b974b6876a14.png)



- 수도 코드 파이썬 코드 변환
```python
# D : 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
# P : 최단 경로 트리 저장
def Dijkstra(G, r): # r: 시작 정점
    D = [float('inf')] * N
    P = [None] * N
    visited = [False] * N
    D[r] = 0

    for _ in range(N):
        minIndex = -1
        min = float('inf')
        for i in range(N):
            if not visited[i] and D[i] < min:
                min = D[i]
                minIndex = i
        visited[minIndex] = True

        for v, val in G[minIndex]:
            if not visited[v] and D[minIndex] + val < D[v]:
                D[v] = D[minIndex] + val
                P[v] = minIndex

```


- 실사용 코드
```python
"""
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
"""

def dijkstra(s, V):  # 시작정점 s, 마지막 정점 V
    U = [0] * (V + 1)
    U[s] = 1
    for v in range(V + 1):
        D[v] = adj[s][v]

    # while len(U) != V:
    for _ in range(V):  # V = 정점개수-1과 같으므로.. 남은 정점개수와 같음
        minV = INF
        w = 0
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1  # 선택된 집합에 포함

        for v in range(V + 1):  # 정점 v가
            if 0 < adj[w][v] < INF:  # w에 인접이면 , 시작정점에서 w를 거쳐 v로 가능 비용과
                D[v] = min(D[v], D[w] + adj[w][v])  # 시작정점에서 v로 가는 기존 비용을 비교 후 선택

INF = 10000
V, E = map(int, input().split())
adj = [[INF] * (V + 1) for _ in range(V + 1)]

for i in range(V + 1):
    adj[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w  # 방향성 그래프

D = [0] * (V + 1)

dijkstra(0, V)

print(D)  # 시작 정점 0에서 각 정점으로 가는 최소 비용

"""
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
"""
```