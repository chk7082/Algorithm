import pprint

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# first sort each word w.r.t alphabetical order
words_sorted = [''.join(sorted(word)) for word in words]

# now we could compare
# we're going to group it
group = []

# list of boolean, denote whether element of words_sorted
# in that position is in group or not
in_group = [False] * len(words)

# for each word in words_sorted
for i, word in enumerate(words_sorted):
    if in_group[i]:  # if it's already in group
        continue

    # create current empty group
    current_group = []
    for j in range(i, len(words_sorted)):
        if in_group[j]:  # if it's already in group
            continue
        if words_sorted[j] == word:  # check if i & j th elements are in the same group
            current_group.append(words[j])  # words[i] : original word
            in_group[j] = True  # update the state

    group.append(current_group)  # append current group to group

pprint.pprint(group, width=30)

# [['eat', 'tea', 'ate'],
#  ['tan', 'nat'],
#  ['bat']]


