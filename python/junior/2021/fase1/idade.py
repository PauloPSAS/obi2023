ages = list()

for x in range(3):
    ages.append(int(input()))

if (ages[0] <= max(ages[1], ages[2]))  and (ages[0] >= min(ages[1], ages[2])):
    print(ages[0])
elif (ages[1] <= max(ages[0], ages[2]))  and (ages[1] >= min(ages[0], ages[2])):
    print(ages[1])
else:
    print(ages[2])
    