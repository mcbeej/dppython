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
    elif path_costs[currentMonth] < lowestCost:
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
