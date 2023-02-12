def best_time_buy_and_sell_stock(prices):
    '''
    function that computes the largest margin of stock price
    with just a single buy_and_sell

    :param
    prices (list) : list containing the consecutive changes
                    of stock prices in certain period
    :return
    largest_margin (num) : the largest margin of stock price
                   with just a single buy_and_sell
    '''

    # from left to right
    # record previously minimum one
    # compare it with current value

    # initialization step
    prev_min = prices[0]
    largest_margin = 0

    # from left to right
    for cur_price in prices:
        # compute largest margin conditioned on selling it
        # right now
        cur_margin = cur_price - prev_min

        # if it's better than before, update it
        if cur_margin > largest_margin:
            largest_margin = cur_margin

        # when we need to update prev_min for the next iteration
        if cur_price < prev_min:
            prev_min = cur_price

    return largest_margin


prices = [7, 1, 5, 3, 6, 4]
print(best_time_buy_and_sell_stock(prices))


