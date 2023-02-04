def palindrome(string):
    '''
    function that return True, if given string is palindrome
                         False, otherwise
    (we only consider digis & alphabets,
    & don't consider the letter case)

    :param
    string (str) : string that we want to check if it's
                   palindrome or not

    :return:
    result (bool) : True, if palindrome
                    False, otherwise
    '''

    # filter it with our conditions
    # extract only alphabets & numbers
    filtered_string = ''.join([char for char in string
                               if char.isalnum()])

    # to make it lowercase
    filtered_string = filtered_string.lower()

    return filtered_string == filtered_string[::-1]


print(palindrome("A man, a plan, a canal: Panama")) # True
print(palindrome("race a car")) # False
print(palindrome('bob')) # True