def hoare_partition(A, l, r):
    pivot = A[l]              # 맨 왼쪽원소 기준
    i = l                     # 피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = r                     # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    
    while i <= j:
        # pivot보다 큰 애를 만나서 멈출 수도 있다
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:             # 교차하지 않은 경우
            A[i], A[j] = A[j], A[i]
    
    A[j], A[l] = A[l], A[j]   # pivot을 j자리로 넣어주자
    # pivot의 위치를 알려줄게
    return j


def qsort(A, l, r):
    # 하나짜리는 굳이 할 필요 X, 역전되어 있으면 구간이 아닌거
    if l < r:
        s = hoare_partition(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)
        

T = int(input())
for tc in range(1, T+ 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 원본 크기로 복사본을 하나 만들자
    # 합칠때 임시 저장용
    tmp = [0] * N

    # 왼쪽 인덱스와 오른쪽 인덱스
    qsort(arr, 0, N-1)

    print(arr)