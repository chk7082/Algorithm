def reverse_string(char_arr):
    '''
    function that reverse the given list of chars without return

    :param
    char_arr (list) : list of characters that we want to reverse

    :return
    None
    '''

    char_arr.reverse()

temp = ['a', 'b', 'c']
print(temp)
reverse_string(temp)
print(temp)