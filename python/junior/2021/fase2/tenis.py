j1 = int(input())
j2 = int(input())
j3 = int(input())
j4 = int(input())

e = [j1+j2, j1+j3, j1+j4, j2+j3, j2+j4, j3+j4]
proxZero = list()

proxZero = [e[0]-e[5], e[1]-e[4], e[2]-e[3], e[5]-e[1]]
proxZeroAbs = []

for x in proxZero:
    proxZeroAbs.append(abs(x))

proxZeroAbs.sort()
print(proxZeroAbs[0])