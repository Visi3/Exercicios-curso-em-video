maior = 0
menor = 0
# Verifica o maior peso entre 5 pessoas
for c in range(1,6,1):
    peso = float(input('Digite o {} peso: '.format(c)))

    if peso > maior:
        maior = peso
        menor = peso
    if peso < menor:
        menor = peso
print('O maior peso é {:.2f}\nO menor peso é {:.2f}'.format(maior,menor))
