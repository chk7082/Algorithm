def largest_number_combination(arr):
    '''
    function that return string representation of the maximum number
    which could be generated by concatenating the elements of arr
    '''

    # initialize our object
    result = ''

    for string in sorted(map(special_string, arr), reverse=True):
        # concatenate it
        result = result + string.data

    return str(int(result))


class special_string:
    '''
    customized string class
    '''
    def __init__(self, data):
        self.data = str(data)

    def __lt__(self, other):
        return self.data + other.data < other.data + self.data


arr = [3, 30, 34, 5, 9]
print(largest_number_combination(arr))