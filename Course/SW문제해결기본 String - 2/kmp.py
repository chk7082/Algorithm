# T : Target // P : Pattern

# 브루트포스를 할건데 그 비교하는 반복을 줄이려고 전처리를 하는 과정이다

def pre_process(p):
    # lps longest prefix suffix
    lps = [0] * len(p)

    # lps를 만들기 위해 패턴 인덱스
    j = 0

    # 처음부터 끝까지 순회
    for i in range(1, len(p)):
        # 패턴 발견, 해당 인덱스에 있는 char가 똑같다면
        if p[i] == p[j]:
            lps[i] = j + 1
            j += 1

        # 다르다면, j 인덱스를 초기화 -> pattern의 가장 처음부터 다시 인식하도록
        else:
            while True:
                if j > 0:
                    j = lps[j-1]
                    if p[j] == p[i]:
                        lps[i] = j + 1
                        j += 1
                        break
                else:
                    break

    return lps


def kmp(text, p):
    '''
    function that proceed kmp algorithm (pattern matching algorithm)
    find pattern p in text, and return index where the pattern starts
                            -1, if pattern doesn't exist

    :param
    text (str) : text string that we want to find pattern p
    p (str) : given pattern string

    :return
    result (int) : index where the pattern p starts in text
                   -1, if pattern doesn't exist
    '''

    # compute lps of pattern p with pre_process function
    lps = pre_process(p)
    lps = [-1] + lps

    # compute the length of text & p
    text_length = len(text)
    p_length = len(p)

    # i : index for text
    # j : index for p

    i = 0
    j = 0

    # proceed KMP step
    while True:
        # if we successfully find it
        if j == p_length:
            return i - j

        # if we reach the end of text without pattern p
        elif i == text_length:
            return -1

        elif text[i] == p[j]:
            i += 1
            j += 1

        # when text[i] != text[j] and j > 0
        # use pre-computed lps of pattern p
        elif j > 0:
            j = lps[j]

        # when text[i] != text[j] and j == 0
        else:
            i += 1


T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f'#{t} {kmp(str2, str1)}')