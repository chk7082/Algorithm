def card(start, end):
    '''
    function that return the winner of card_tournament (recursively)

    :param
    start, end (int) : index of the range we're now focusing

    :return:
    result (int) : index of the winner
    '''

    # when there's only one person in this range
    if start == end:
        return start

    # when there's more than on person
    else:
        middle = (start + end)//2
        start = card(start, middle)
        end = card(middle + 1, end)
        return rock_paper_scissors(start, end)


def rock_paper_scissors(ind1, ind2):
    '''
    function that proceed rock-paper-scissors game
    value 1 -> scissor, 2 -> rock, 3 -> paper

    :param
    ind1 (int) : index of person (lower)
    ind2 (int) : index of person (upper)

    :return
    result (int) : index of winner
    '''

    # when tie
    if arr[ind1] == arr[ind2]:
        return ind1
    # when person1 wins
    elif arr[ind1] % 3 == (arr[ind2] + 1) % 3:
        return ind1
    # when person2 wins
    else:
        return ind2


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # since our index starts from 0
    print(f'#{t} {card(0, N-1) + 1}')