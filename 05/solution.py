data = list(open("data.txt").read().rstrip())

def react(polymer):
    buff = [" "]
    for i in range(polymer.__len__()):
        if(polymer[i]!=buff[-1] and polymer[i].lower()==buff[-1].lower()):
            buff.pop()
        else:
            buff.append(polymer[i])
    return buff.__len__()-1

# First part
print(f"First part: %i" % react(data))

# Second part
components = list(zip(sorted(set([x.upper() for x in data])), sorted(set([x.lower() for x in data]))))

l = []
for x in components:
    l.append(react([z for z in data if z not in x]))

print(f"Second part: %i" % min(l))
