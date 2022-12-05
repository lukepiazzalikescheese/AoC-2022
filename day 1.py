f = open('input.txt', 'r')
buf = f.readlines()
f.close()

total = 0
maxelf = 0

lst = [x.strip() for x in buf]

for g in lst:
    if len(g)< 1:
        if total > maxelf:
            maxelf = total
        total = 0
    else:
        total += int(g)


print(maxelf)
