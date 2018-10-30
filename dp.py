def opt_path(currentCity, currentMonth):
    if currentMonth == 0:
        return 0
    present_costs = paths[currentCity][currentMonth]
    lastCities = list({opt_path(0, currentMonth - 1) + fixed_costs[0][currentCity],
                        opt_path(1, currentMonth - 1) + fixed_costs[1][currentCity],
                        opt_path(2, currentMonth - 1) + fixed_costs[2][currentCity]})
    lowestCost = min(lastCities)
    if optimal[currentMonth] is None:
        optimal[currentMonth] = city_names[lastCities.index(lowestCost)]
        path_costs[currentMonth] = present_costs
    elif path_costs[currentMonth] > lowestCost:
        optimal[currentMonth] = city_names[lastCities.index(lowestCost)]
        path_costs[currentMonth] = lowestCost
    return lowestCost + present_costs


paths = []
city_names = ["NY", "LA", "DEN"]
paths.append([0, 8, 3, 10, 43, 15, 48, 5, 40, 20, 30, 28, 24])
paths.append([0, 18, 1, 35, 18, 10, 19, 18, 10, 8, 5, 8, 20])
paths.append([0, 40, 5, 8, 13, 21, 12, 4, 27, 25, 10, 5, 15])

fixed_costs = [[0, 20, 15],
                [20, 0, 10],
               [15, 10, 0]]

optimal = [None for i in range(len(paths[0]))]
path_costs = [None for i in range((len(paths[0])))]

print (opt_path(2, 12))
print (optimal)
print (path_costs)


def opt_path_dp(cities, months):

    # Initialize matrix
    M = [[0 for j in range(len(months[0]))] for i in range(len(cities))]

    # Initialize first column (starting costs from each city)
    M[0][1] = months[0][1]
    M[1][1] = months[1][1]
    M[2][1] = months[2][1]

    # Populate cells column-major
    for j in range(2, len(months[0])):
        for i in range(len(cities)):
            if i == 0:
                min_cost_0 = min(M[i][j-1], M[i+1][j-1] + fixed_costs[i][i+1], M[i+2][j-1] + fixed_costs[i][i+2])
                min_cost_0 += paths[i][j]
                M[i][j] = min_cost_0
            elif i == 1:
                min_cost_1 = min(M[i][j-1], M[i-1][j-1] + fixed_costs[i][i-1], M[i+1][j-1] + fixed_costs[i][i+1])
                min_cost_1 += paths[i][j]
                M[i][j] = min_cost_1
            elif i == 2:
                min_cost_2 = min(M[i][j-1], M[i-1][j-1] + fixed_costs[i][i-1], M[i-2][j-1] + fixed_costs[i][i-2])
                min_cost_2 += paths[i][j]
                M[i][j] = min_cost_2
#
# <<<<<<< HEAD
    for c, m in enumerate(M):
        M[c] = m[1:]
# =======
#     print(M)
#     num_months = len(months[0]) - 1
#     min_cost = min(M[0][num_months], M[1][num_months], M[2][num_months])
#
#     return min_cost
# >>>>>>> 48792ea2213563cf5f3a0b6242db884dd30ca13c

    min_cost = min(M[0][11], M[1][11], M[2][11])
    mc_loc = [M[0][11], M[1][11], M[2][11]].index(min_cost)
    trace = city_names[mc_loc]
    for m, cost in reversed(list(enumerate(M[0][:-1]))):
        temp_arr = [M[0][m] + fixed_costs[0][mc_loc],
                    M[1][m] + fixed_costs[1][mc_loc],
                    M[2][m] + fixed_costs[2][mc_loc]]
        temp_min = min(temp_arr)
        mc_loc = temp_arr.index(temp_min)
        trace = city_names[mc_loc] + " " + trace

    return min_cost, trace

ans = opt_path_dp(city_names, paths)
print(ans[0], "\n", ans[1])

# TODO: traceback
