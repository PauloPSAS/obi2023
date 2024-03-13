matches = list()

for x in range (6):
    matches.append(input().upper()[0])

win = matches.count('V')
if 5 <= win <= 6:
    print(1)
elif 3 <= win <= 4:
    print(2)
elif 1 <= win <= 2:
    print(3)
else:
    print(-1)
