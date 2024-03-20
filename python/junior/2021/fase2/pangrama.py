# Dá para melhorar...

alfabeto = ("a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","x","z")

frase = input().lower()
frase = frase.replace(' ', '')

for l in frase:
    if ord(l) < 97 and ord(l) > 122:
        frase = frase.replace(l, '')

for l in alfabeto:
    if l not in frase:
        print('N')
        break
    else:
        if l == alfabeto[-1]:
            print('S')
