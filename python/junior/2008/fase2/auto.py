C = int(input())

qtd = 0

a = input().upper()[:C]

for _ in a:
    if _ == "P" or _ == "C":
        qtd += 2
    elif _ == "A":
        qtd += 1

print(qtd)
