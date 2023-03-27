def best_time_to_buy_and_sell_stock_2(prices):
    '''
    function that return the maximum profit
    given the stock prices
    '''

    # initialize our result
    result = 0

    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            result += prices[i+1] - prices[i]

    return result


prices = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_and_sell_stock_2(prices)) # 7