def most_frequent_word(paragraph, banned):
    '''
    function that return the most frequent word in paragraph
    (except for the words in banned list)
    (we don't consider letter case & punctuation)

    :param
    paragraph (str) :
    banned (list) :

    :return
    result (str) : most frequent word in paragraph
                   (except for the words in banned list)
    '''

    # define the list containing punctuations
    punctuations = '!@#$%^&*()_-+={}:<>,./\\;[]\''

    # ignore punctuation
    for punctuation in punctuations:
        paragraph = paragraph.replace(punctuation, '')

    # make it lower
    paragraph = paragraph.lower()

    # split it into words
    # abandon banned word
    split_words = [word for word in paragraph.split()
                   if (not word in banned)]

    # count the multiplicity with dictionary
    dict_counter = dict()
    for word in split_words:
        # set default to 0
        dict_counter.setdefault(word, 0)
        # count it
        dict_counter[word] += 1

    return max(dict_counter, key=dict_counter.get)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(most_frequent_word(paragraph, banned))
# ball
