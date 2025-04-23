digitos = {
    "":1, "abc": 2, "def": 3,
    "ghi": 4, "jkl": 5, "mno": 6,
    "pqrs": 7, "tuv": 8, "wxyz": 9,
    "-":"-"}

entrada = input().lower()
saida = ""

for letra in entrada:
    for chave, valor in digitos.items():
        if letra in chave:
            saida += str(valor)
            break

print(saida)
