def baby_gin(string):
    '''
    function that return True, if the given string of length 6 is baby-gin
                        False, otherwise
    '''

    # initialization step
    multiplicity = [0] * 10

    # for each char in string, cumulate the multiplicity
    for char in string:
        multiplicity[int(char)] += 1

    # we could use greedy algorithm
    # since the string having the digit with multiplicity >= 3 is baby-gin
    # only if they're used as triple

    # reduce the multiplicity by checking the triples
    multiplicity = list(map(lambda x: x % 3, multiplicity))

    # iterate the multiplicity to find if the remaining one is composed of the run
    for i in range(10):
        pivot = multiplicity[i]  # pivot <= 2
        if pivot:
            if i+2 < 10 and multiplicity[i+1] >= pivot and multiplicity[i+2] >= pivot:
                multiplicity[i] -= pivot
                multiplicity[i+1] -= pivot
                multiplicity[i+2] -= pivot
            else:
                return False

    return True


T = int(input())
for _ in range(T):
    string = input()
    print(baby_gin(string))