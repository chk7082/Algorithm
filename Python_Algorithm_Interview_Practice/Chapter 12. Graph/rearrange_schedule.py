def rearrange_schedule(start):
    '''
    function that rearrange the cities that will be visited
    starting from the city 'start'

    :param
    start (str) : string that represents the starting city
    '''

    # initialize current city
    cur_city = start

    # until break
    while True:
        # if it's non-empty
        if flight_dict.get(cur_city):
            # pop it (we deliberately sorted it in decreasing order
            #         just to make the lexically ordered schedule)
            cur_city = flight_dict[cur_city].pop()

            # append it to our schedule
            schedule.append(cur_city)

        # otherwise (if it's empty)
        else:
            return


flights = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
flight_dict = dict()

# record adjacency
for city_from, city_to in flights:
    flight_dict.setdefault(city_from, [])
    flight_dict[city_from].append(city_to)

# sort it in decreasing order
for city_from in flight_dict.keys():
    flight_dict[city_from].sort(reverse=True)

start = "JFK"
schedule = [start]
rearrange_schedule(start)
print(schedule)