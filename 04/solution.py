import datetime
from dateutil import rrule
from collections import Counter

data = [x[1:].split("] ") for x in open("data.txt").read().split("\n")]

def epoch(x):
    x = x.split(" ")
    d = list(map(int,x[0].split("-")))
    t = list(map(int,x[1].split(":")))
    return datetime.datetime(d[0], d[1], d[2], t[0], t[1])#.timestamp()

data = [{"timestamp": epoch(x[0]), "cmd": x[1]} for x in data]
data = sorted(data, key = lambda k: k["timestamp"])

# Part 1
guards = {}
pointer = None

for row in data:
    if(row["cmd"][:5] == "Guard"):
        pointer = int(row["cmd"].split(" ")[1][1:])
    elif(row["cmd"] == "falls asleep"):
        guards[pointer] = guards.get(pointer, []) + [[row["timestamp"]]] 
    elif(row["cmd"] == "wakes up"):
        guards[pointer][-1].append(row["timestamp"])

naps = {}

for g,n in guards.items():
    naps[g] = sum([(x[-1]-x[0]).seconds//60 for x in n])

sleepyhead = max(naps, key=naps.get)

minutes = [[z.minute for z in rrule.rrule(rrule.MINUTELY, dtstart=x[0], until=x[-1])] for x in guards[sleepyhead]]

all_minutes = []

for x in minutes:
    all_minutes += x

print(Counter(all_minutes).most_common(1)[0][0] * sleepyhead)