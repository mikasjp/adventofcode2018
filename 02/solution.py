data = [list(x) for x in open("data.txt", "r").read().split("\n")]

# First part
occurences = {}

for row in data:
    unique = set(row)
    cnt = set([row.count(x) for x in unique if row.count(x) in [2, 3]])
    for i in cnt:
        if i==1:
            continue
        occurences[i] = occurences.get(i, 0) + 1

total = 1
for k,v in occurences.items():
    total *= v

print("First part: " + str(total))

# Second part
def hamming(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def diff(s1, s2):
    return [s1[i]==s2[i] for i in range(s1.__len__())].index(False)

for i in range(data.__len__()):
    for j in range(i, data.__len__()):
        a = "".join(data[i])
        b = "".join(data[j])
        if hamming(a, b) == 1:
            print("Second part: " + "".join([x for i,x in enumerate(data[i]) if i!=diff(a,b)]))
            break
    else:
        continue
    break
