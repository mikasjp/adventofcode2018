import datetime
data = [x[1:].split("] ") for x in open("data.txt").read().split("\n")]

def epoch(x):
    x = x.split(" ")
    d = list(map(int,x[0].split("-")))
    t = list(map(int,x[1].split(":")))
    return datetime.datetime(d[0], d[1], d[2], t[0], t[1]).timestamp()

data = [{"timestamp": epoch(x[0]), "cmd": x[1]} for x in data]
data = sorted(data, key = lambda k: k["timestamp"])

# Part 1
guards = {}
pointer = None

print(data[:20])

#for row in data:
#    if(row["cmd"][:5] == "Guard"):
#        pointer = row["cmd"].split(" ")[1][1:]
#    elif(row["cmd"] == "wakesup")
