A, B = map(int, input().split())

soma = A + B

# Se a soma de A e B for par
if soma % 2 == 0:
    C = soma // 2
# Se a soma de A e B for ímpar
else:
    # Verifica se A e B são consecutivos
    if (B - A) == ((B - 1) - A):
        C = (A + B) // 2
    else:
        C = (soma + 1) // 2

print(C - A)  # Imprime a diferença entre C e A
