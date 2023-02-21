def daily_temperature(T):
    '''
    function that return the list containing the amount of day
    we should wait for the warmer weather (for each day)

    :param
    T (list) : list of daily temperature (in fahrenheit)

    :return
    days_required (list) : the list containing the amount of day
                         we should wait for the warmer weather (for each day)
    '''

    # initialize our object
    L = len(T)
    days_required = [0] * L

    # initialize our stack
    stack = []

    # for each day
    # cumulate index
    for day, temperature in enumerate(T):
        # when stack is not empty & if current temperature is higher than that
        while stack and stack[-1][1] < temperature:
            prev_day, _ = stack.pop()
            days_required[prev_day] = day - prev_day

        # push current day info
        stack.append((day, temperature))

    return days_required


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperature(T))
