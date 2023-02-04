def reordering_log(log_list):
    '''
    reorder logs with following rules

    :param
    log_list (list) : list of logs(str) that we want to reorder

    :return
    result (list) : reordered logs
    '''

    # split letter_logs & digit_logs
    letter_logs = []
    digit_logs = []

    # for each log
    for log in log_list:
        # if it is alphabet
        if log.split()[1].isalpha():
            letter_logs.append(log)
        # if it is digit
        else:
            digit_logs.append(log)

    # sort letter_logs with letters, if same, use identifier
    letter_logs.sort(key = lambda log: (log.split()[1:], log.split()[0]))

    return letter_logs + digit_logs


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reordering_log(logs))
# ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']

