soma = 0
# Soma os valores múltiplos de 3 de 1 até 500
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c

print(soma)