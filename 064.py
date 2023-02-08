cont = soma = num = 0
# Mostrando quanto e quantos
while num != 999:
    if num != 999:
        soma += num
        num = int(input('Digite um número: [999 para PARAR] '))
        cont += 1
print('\n\nVocê digitou {} números e a soma deles foi {}.'.format(cont - 1, soma))
print('\nFIM')
