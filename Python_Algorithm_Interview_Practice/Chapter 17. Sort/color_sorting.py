def color_sorting(left, right):
    '''
    quick sort (recursively)
    '''

    if left < right:
        # use last element as pivot
        i = left

        for j in range(left, right):
            if color[j] < color[right]:
                color[i], color[j] = color[j], color[i]
                i += 1
        color[i], color[right] = color[right], color[i]

        # recursive part
        color_sorting(left, i - 1)
        color_sorting(i + 1, right)


color = [2, 0, 2, 1, 1, 0]
color_sorting(0, len(color) - 1)
print(color)