qtd_questoes = int(input())
while 1 > qtd_questoes > 80:
    qtd_questoes = int(input())

acertos = 0

gabarito = input().upper()[:qtd_questoes]
resposta = input().upper()[:qtd_questoes]

for v, r in enumerate(gabarito):
    if resposta[v] == gabarito[v]:
        acertos += 1

print(acertos)
