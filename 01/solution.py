Data = [int(x) for x in open("./data.txt", "r").read().split("\n")]

# first part
Frequency = sum(Data)
print(Frequency)

#second part
Frequency = 0
Duplicates = []

i = 0

while True:
     Frequency += Data[i]
     if Frequency in Duplicates:
         break
     Duplicates.append(Frequency)
     i = (i + 1) % len(Data)

print(Frequency)
