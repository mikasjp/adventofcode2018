import asyncio

data = list(open("data.txt").read())

def react(polymer):
    i = 0
    while(i < polymer.__len__()-1):
        if(abs(ord(polymer[i])-ord(polymer[i+1])) == 32):
            del polymer[i+1]
            del polymer[i]
            i = 0
        else:
            i = i+1

    return polymer.__len__()

print(react(data))

# Second part
components = list(zip(sorted(set(open("data.txt").read().upper())), sorted(set(open("data.txt").read().lower()))))

l = []
for x in components:
    l.append(react([z for z in data if z not in x]))

print(min(l))
