def merge_intervals(intervals):
    '''
    function that merge the intervals if they have nonempty intersection

    :param
    intervals (list) : list containing closed intervals ([left, right])

    :return
    merged_intervals (list) : list containing the merged intervals
    '''

    # initialize our object
    merged_intervals = []
    start = 0
    end = 0
    L = len(intervals)

    # sort intervals
    intervals.sort()

    # assume L >= 1
    right = intervals[0][1]

    # until break
    while True:
        # if it's the end
        if end == L - 1:
            merged_intervals.append([intervals[start][0], right])
            return merged_intervals
        # if those two adjacent intervals have nonempty intersection
        elif right >= intervals[end + 1][0]:
            right = max(right, intervals[end + 1][1])
            end += 1
        # otherwise, cumulate current closed intervals & update start, end, right
        else:
            merged_intervals.append([intervals[start][0], right])
            end += 1
            start = end
            right = intervals[end][1]



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))