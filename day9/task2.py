def determ(point_a, point_b):
    #print(point_a[0] * point_b[1], "-", point_b[0] * point_a[1])
    return point_a[0] * point_b[1] - point_b[0] * point_a[1] 

def shoelace(points):
    total = 0
    points.append(points[0])
    for i in range(len(points)-1):
        #print(points[i], points[i+1])
        a = points[i]
        b = points[i+1]
        total += determ(a,b)
    return total/2

def pick(area, verts):
    return area + 1 - (verts/2)

filename = "day9\\pathcoords.txt"
coords = []
with open(filename) as source:
    for line in source.readlines():
        x, y = line.rstrip("\n").split()
        coords.append((int(x), int(y)))

points = len(coords)
area = shoelace(coords)
verts = pick(area, points)
print(verts)
# 527