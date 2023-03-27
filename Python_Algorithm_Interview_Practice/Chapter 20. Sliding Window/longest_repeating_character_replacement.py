from collections import Counter


def longest_repeating_character_replacement(S, k):
    '''
    function that return the length of the longest
    repeating character that could be made by replacing at most k characters
    '''

    # initialize our object
    max_length = 0
    start = 0
    end = k
    L = len(S)

    # trivial case
    if L <= k:
        return L

    count = Counter(S[:k])

    while True:
        most_common_number = count.most_common(1)[0][1]

        # when we need to increase end
        if end - start - most_common_number <= k:
            max_length = max(max_length, end-start)
            end += 1

            if end > L:
                return max_length
            else:
                count[S[end-1]] += 1
        # when we need to increase start
        else:
            count[S[start]] -= 1
            start += 1



S = "AAABBC"
k = 2

print(longest_repeating_character_replacement(S, k))  # 5

