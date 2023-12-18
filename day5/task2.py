from math import ceil

# (time, distance)
race = (44826981, 202107611381458)

# T = race time
# t0 = charge time
# (T - t0) = run time
# t0 * (T - t0) = distance = Tt0 - t0^2

def dist(time, charge):
    return charge * (time - charge)

def one_race(time, distance):
    counter = 0
    for i in range(time):
        if dist(time, i) > distance:
            counter += 1
    return counter

print(one_race(race[0], race[1]))
