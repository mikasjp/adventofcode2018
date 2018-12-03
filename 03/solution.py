data = open("data.txt").read().split("\n")

# Part 1
rect = {}

for row in data:
    a =row.split(" @ ")[1].split(": ")
    xy = list(map(int, a[0].split(",")))
    wh = list(map(int, a[1].split("x")))
    for y in range(xy[1], xy[1] + wh[1]):
        for x in range(xy[0], xy[0] + wh[0]):
            coords = str(x) + "x" + str(y)
            rect[coords] = rect.get(coords, 0) + 1

counter = 0
for k,v in rect.items():
    if v>1:
        counter += 1

print(counter)

# Part 2
rect = {}
for row in data:
    a =row.split(" @ ")[1].split(": ")
    xy = list(map(int, a[0].split(",")))
    wh = list(map(int, a[1].split("x")))
    id = row.split(" @ ")[0]
    for y in range(xy[1], xy[1] + wh[1]):
        for x in range(xy[0], xy[0] + wh[0]):
            coords = str(x) + "x" + str(y)
            rect[coords] = rect.get(coords, []) + [id]

for row in data:
    a =row.split(" @ ")[1].split(": ")
    xy = list(map(int, a[0].split(",")))
    wh = list(map(int, a[1].split("x")))
    id = row.split(" @ ")[0]
    colliding = False
    for y in range(xy[1], xy[1] + wh[1]):
        for x in range(xy[0], xy[0] + wh[0]):
            coords = str(x) + "x" + str(y)
            if len(rect[coords])>1 or id not in rect[coords]:
                colliding = True
                break
    if not colliding:
        print(id)
        break