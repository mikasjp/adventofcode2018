data = list(map(ord, list(open("data.txt").read())))

# First part
i = 0
while(i < data.__len__()-1):
    if(abs(data[i]-data[i+1]) == 32):
        del data[i+1]
        del data[i]
        i = 0
    else:
        i = i+1

print(data.__len__())
