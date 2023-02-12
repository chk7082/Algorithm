def rainwater_trapping(height_arr):
    '''
    function that return the maximum amount of
    volume that the structure could contain

    :param
    height_arr (list) : list containing the heights of
                        each position of the structure

    :return
    result (num) : the maximum amount of volume
                   that the structure could contain
    '''

    # maximum height
    max_height = max(height_arr)

    # initialize our interest
    result = 0

    # for each level of altitude,
    # compute the number of empty spaces between
    # the first & last position that height >= current level
    for cur_height in range(1, max_height):
        # string representation
        # string of length len(height) composed of '1' & '0'
        # where '1' means that position >= cur_height
        # & '0' means the otherwise
        str_rep = ''.join(map(lambda height: str(int(height >= cur_height)), height_arr))

        # strip '0' on bothsides
        # and count '0's (the empty spaces) in the middle
        result += (str_rep.strip('0')).count('0')

    return result


height_arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rainwater_trapping(height_arr))