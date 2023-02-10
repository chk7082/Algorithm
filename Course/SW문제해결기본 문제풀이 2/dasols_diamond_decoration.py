def dasols_diamond_decoration(string):
    '''
    function that decorate given string with diamonds

    :param
    string (str) : given string that we want to decorate

    :return
    decorated_string (list) : list of strings where each string
                              represents each row
    '''

    # length of string
    s_length = len(string)

    # initialize our object
    decorated_string = ['.' + s_length*'.#..', '.' + s_length*'#.#.']

    # append third col (which contain the original string)
    decorated_string.append('#.' + '.#.'.join(list(string))  + '.#')

    # use vertical symmetry
    decorated_string.append(decorated_string[1])
    decorated_string.append(decorated_string[0])

    return decorated_string


T = int(input())
for t in range(1, T+1):
    string = input()
    print(*dasols_diamond_decoration(string), sep='\n')