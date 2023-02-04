def longest_sub_palindrome(string):
    '''
    function that return the longest sub palindrome in string

    :param
    string (str) : string that we want to find longest sub palindrome

    :return
    longest_palindrome (str) : longest sub palindrome of string
    '''

    # initialize our interest
    longest_palindrome_length = 0
    longest_palindrome = ''

    # find possible candidates sequentially
    # consider i to j (w.r.t index)
    for i in range(len(string)):
        # we don't need to consider string of length
        # <= current longest_palindrome_length
        for j in range(i + 1 + longest_palindrome_length, len(string), 1):
            # current word (from index i to j)
            cur_word = string[i:j+1]

            # check if it's valid palindrome
            if cur_word == cur_word[::-1]:
                # update it
                longest_palindrome = cur_word
                longest_palindrome_length = j - i + 1

    return longest_palindrome

print(longest_sub_palindrome("babad")) # bab
print(longest_sub_palindrome("cbbd")) # bb