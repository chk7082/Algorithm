def pascal_triangle(max_depth):
    '''
    function that return the pascal triangle of depth : max_depth

    :param
    max_depth (int) : wanted maximum depth of pascal_triangle

    :return
    pascal_triangle (list) : list of list where
                             each list contains each depth of pascal_triangle
    '''

    # when depth == 1 or 2
    if max_depth <= 2:
        return [[1] * i for i in range(max_depth)]

    # initialize pascal_triangle
    full_pascal_triangle = [[1], [1, 1]]

    # from 2 ~ max_depth - 1
    for i in range(2, max_depth + 1):
        # compute current depth from the previous one
        # consider 0 for the outer range
        cur_depth = [x_i_minus_1 + x_i for x_i_minus_1, x_i
                     in zip([0]+full_pascal_triangle[i-1], full_pascal_triangle[i-1]+[0])]

        # append current depth
        full_pascal_triangle.append(cur_depth)

    return full_pascal_triangle


T = int(input())
depth_list = [int(input()) for _ in range(T)]
max_depth = max(depth_list)

# precompute full pascal triangle
full_pascal_triangle = pascal_triangle(max_depth)

for t in range(1, T+1):
    print(f'#{t}')
    for depth in range(depth_list[t-1]):
        print(*full_pascal_triangle[depth], sep=' ')