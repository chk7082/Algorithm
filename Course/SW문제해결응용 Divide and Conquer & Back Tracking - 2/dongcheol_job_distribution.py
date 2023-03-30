def dongcheol_job_distribution(i, N, cur_prob):
    '''
    function thatr recursively find the job distribution
    that maximize the success probability

    :param
    i (int) : number of currently considered tasks
    N (int) : number of people (= number of tasks)
    cur_prob (float) : currently cumulated probability (by production)
    '''

    # if we considered all tasks
    if i == N:
        if cur_prob > max_probability[0]:
            max_probability[0] = cur_prob
        return

    # pruning step, we don't need to go further
    elif cur_prob <= max_probability[0]:
        return

    # when we need to go further
    else:
        # for each possible job candidate for person i
        for candidate in range(N):
            if todo_job[candidate]:
                # allocate job to person i
                todo_job[candidate] = False

                dongcheol_job_distribution(i+1, N, cur_prob * probabilities[i][candidate])

                # free it for the other cases
                todo_job[candidate] = True


T = int(input())
for t in range(1, T+1):
    N = int(input())
    probabilities = [list(map(lambda x: float(x)/100.0, input().split())) for _ in range(N)]
    '''
    probabilities (list) : matrix(2-dim'l list) of size N by N where
                           each row i represents the probabilities that the person i
                           succeed each task
    '''

    # previously maximum probability => for pruning
    max_probability = [0.0]

    # set
    todo_job = [True] * N

    # proceed
    dongcheol_job_distribution(0, N, 1.0)

    rounded_string = str(round(max_probability[0]*100, 6))
    str_length = 7 + rounded_string.index('.')
    rounded_string = rounded_string.ljust(str_length, '0')

    print(f'#{t} {rounded_string}')

