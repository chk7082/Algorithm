from collections import deque

def palindrome(string):
    '''
    function that return True, if given string is palindrome
                        False, otherwise
    :param
    string (list) : given list of characters that we want to check whether it's palindrome or not

    :return
    result (bool) : True, if given string is palindrome
                   False, otherwise
    '''

    # convert it to deque
    str_deque = deque(string)

    # until it has at least 2 elements
    while len(str_deque) > 1:
        # check the conditions
        if str_deque.popleft() != str_deque.pop():
            return False

    # otherwise it's valid palindrome
    return True

string = '1->2->1'
print(palindrome(string.split('->')))