N, P = map(int, input().split())
s = 0

for jogador in range(N):
    x, y = map(int, input().split())
    if (x+y) >= P:
        s += 1

print(s)