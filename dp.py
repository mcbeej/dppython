def opt_path(currentCity, currentMonth):
    """ Recursive function that returns the lowest cost from city k at month i"""

    if currentMonth == 0:
        return 0
    present_costs = paths[currentCity][currentMonth]
    lastCities = list({opt_path(0, currentMonth - 1) + fixed_costs[0][currentCity],
                        opt_path(1, currentMonth - 1) + fixed_costs[1][currentCity],
                        opt_path(2, currentMonth - 1) + fixed_costs[2][currentCity]})
    lowestCost = min(lastCities)
    # if optimal[currentMonth] is None:
    #     optimal[currentMonth] = city_names[lastCities.index(lowestCost)]
    #     path_costs[currentMonth] = present_costs
    # elif path_costs[currentMonth] > lowestCost:
    #     optimal[currentMonth] = city_names[lastCities.index(lowestCost)]
    #     path_costs[currentMonth] = lowestCost
    return lowestCost + present_costs


def opt_path_dp(cities, months, fixed_costs):
    """ DP function that takes in cities, months
        and returns the lowest cost/optimal path """

    # Initialize matrix
    M = [[0 for j in range(len(months[0]))] for i in range(len(cities))]

    # Initialize first column (starting costs from each city)
    # M[0][1] = months[0][1]
    # M[1][1] = months[1][1]
    # M[2][1] = months[2][1]
    for i in  range(len(cities)):
        M[i][0] = months[i][0]

    # Populate cells column-major
    nc = len(cities)
    for j in range(1, len(months[0])):
        for i in range(nc):
            costs = []
            for c, nothing in enumerate(cities):
                costs.append(M[(i + c) % nc][j-1] + fixed_costs[i][(i + c) % nc])
            min_cost_0 = min(costs)

                            # M[i % nc][j-1] + fixed_costs[i][i % nc],
                            #  M[(i+1) % nc][j-1] + fixed_costs[i][(i+1) % nc],
                            #  M[(i+2) % nc][j-1] + fixed_costs[i][(i+2) % nc])
            min_cost_0 += months[i][j]
            M[i][j] = min_cost_0
            # elif i == 1:
            #     min_cost_1 = min(M[i][j-1], M[i-1][j-1] + fixed_costs[i][i-1], M[i+1][j-1] + fixed_costs[i][i+1])
            #     min_cost_1 += months[i][j]
            #     M[i][j] = min_cost_1
            # elif i == 2:
            #     min_cost_2 = min(M[i][j-1], M[i-1][j-1] + fixed_costs[i][i-1], M[i-2][j-1] + fixed_costs[i][i-2])
            #     min_cost_2 += months[i][j]
            #     M[i][j] = min_cost_2

    # Traceback
    last_costs = []
    for i in range(len(cities)):
        last_costs.append(M[i][-1])
    min_cost = min(last_costs)
    mc_loc = last_costs.index(min_cost)
    trace = cities[mc_loc]
    for m, cost in reversed(list(enumerate(M[0][:-1]))):
        temp_arr = []
        for c in range(len(cities)):
            temp_arr.append(M[c][m] + fixed_costs[c][mc_loc])
        temp_min = min(temp_arr)
        mc_loc = temp_arr.index(temp_min)
        trace = cities[mc_loc] + " " + trace

    return min_cost, trace

def main():
    city_names = []
    paths = []
    fixed_costs = []
    additional_city = raw_input("New city name: [Enter N when done] ")
    while additional_city != "N" and additional_city != "n":
        city_path = raw_input("Enter month-by-month cost for city (use spaces): ")
        city_names += [additional_city]
        paths.append([int(x) for x in city_path.split(',')])
        additional_city = raw_input("New city name: [Enter N when done] ")

    # Fixed costs input
    # fixed_costs = [[0, 20, 15],
    #                [20, 0, 10],
    #                [15, 10, 0]]

    for i in range(len(city_names)):
        transport_costs = []
        for j in range(len(city_names)):
            fij = int(raw_input("Cost to move from " + city_names[i] + " to " + city_names[j] + ": "))
            transport_costs.append(fij)
        fixed_costs.append(transport_costs)

    optimal = [None for i in range(len(paths[0]))]
    path_costs = [None for i in range((len(paths[0])))]

    # print(opt_path(2, 12))
    # print(optimal)
    # print(path_costs)

    ans = opt_path_dp(city_names, paths, fixed_costs)
    print(ans[0])
    print(ans[1])



main()

