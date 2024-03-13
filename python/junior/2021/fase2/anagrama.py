tamanho = int(input())
frase1 = input().lower().replace('.', ' ').replace(',', ' ')
frase2 = input().lower().replace('.', ' ').replace(',', ' ')

status = ''

if len(frase1) != len(frase2):
    status = 'N'
else:
    status = 'S'

for i in frase1:
    if frase1.count(i) == frase2.count(i):
        continue
    else:
        status = 'N'
print(status)
