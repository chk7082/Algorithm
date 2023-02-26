def course_schedule(n, course, path):
    '''
    function that return True, if we could possibly take all the courses
                               (if the graph is cycle-free (tree or forest))
                        False, otherwise
                               (if the graph has cycle)

    :param
    n (int) : total number of courses
    course (int) : current course we're interested in
    path (set) : set containing courses in recorded path until current course
    '''

    for pre in prerequisites.get(course):
        if not (pre in path):
            # if it's False, recursively return False
            if not course_schedule(n, pre, path.union(set([pre]))):
                return False
            else:
                return True
        else:
            return False
    # for-else, when there's no cycle in current path
    else:
        return True

n = 3
prerequisite_list = [[0, 1], [0, 2], [1, 2]]
prerequisites = dict()

for course in range(n):
    prerequisites.setdefault(course, [])

for course, needed_prerequisite in prerequisite_list:
    prerequisites[course].append(needed_prerequisite)

print(course_schedule(n, 0, set([0])))