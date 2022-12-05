f = open('input.txt', 'r')
buf = f.readlines()
f.close()

#Part 1

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

#Part 2

elflst = []


for h in lst:
    if len(h)< 1:
        elflst.append(int(total))
        total = 0
    else:
        total += int(h)

elflstprime = sorted(elflst, reverse = True)[1:4]
print(sum(elflstprime))
