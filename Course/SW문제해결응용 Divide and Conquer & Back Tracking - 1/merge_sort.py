def msort(s, e):
    # 하나짜리인 경우 => s와 e가 같다 => 딱히 할거 없다, 그냥 return
    if s == e:
        return
    m = (s+e)//2
    # index를 알려줄테니 그 구간에 대해서 정렬을 수행해줘
    msort(s, m)
    msort(m+1, e)
    # 여기 코드를 읽을 때는 각 반씩은 정렬 되어 있는 상태
    # 저거를 정렬하면서 어딘가는 넣어놔야하니까 아까 임시 저거 만든거
    # 항상 그 위치를 찾으면서 swap 하는거보다 편할수도?
    # merge()
    l, r = s, m+1  # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    k = 0          # temp에 복사해둘 index
    while True:          #l <= m and r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m:
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1
            break
        elif r <= e:
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1
            break

    i = 0
    while i < k:
        arr[s+i] = tmp[i]
        i += 1
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 원본 크기로 복사본을 하나 만들자
    # 합칠때 임시 저장용
    tmp = [0]*N
    
    # 왼쪽 인덱스와 오른쪽 인덱스
    msort(0, N-1)

    print(arr)