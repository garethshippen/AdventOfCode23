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
    opt_time = ceil(time/2)
    var = time / 2 - (time**2 / 4 - distance)**0.5
    return (opt_time - ceil(var))*2
    
print(one_race(race[0], race[1]))