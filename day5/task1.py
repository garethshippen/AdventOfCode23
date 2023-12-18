from math import ceil

# (time, distance)
races = ((44, 202)
        , (82, 1076)
        , (69, 1138)
        , (81, 1458))

# T = race time
# t0 = charge time
# (T - t0) = run time
# t0 * (T - t0) = distance = Tt0 - t0^2

def equation(time, charge):
    return charge * (time - charge)

def one_race(time, distance):
    counter = 0
    for i in range(time):
        if equation(time, i) > distance:
            counter += 1
    return counter

methods = 1
for race in races:
    methods *= one_race(race[0], race[1])
    
print(methods)
