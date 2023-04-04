def find_set(x):        # x가 속한 집합의 대표 리턴
    while x != rep[x]:  # 같을 때까지 계속 찾아가줘, x == rep[x]가 될 때까지
        x = rep[x]      # 그 집합의 대표를 찾을 때까지
    return x


def union(x, y):
    # y가 속한 집합의 대표원소가 자기자신을 가리키고 있었을텐데
    # 걔가 가리키던 걸 x의 대표원소로 바꿔줘
    rep[find_set(y)] = find_set(x)



# makeset()
rep = [i for i in range(6)] # 각각이 대표인 상황
print(rep)