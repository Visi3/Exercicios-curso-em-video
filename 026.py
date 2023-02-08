frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece {} vezes!'.format(frase.count('a')))
print('O primeiro aparece na posição {} '.format(frase.find('a') + 1))
print('O ultimo aparece na posição {} '.format(frase.rfind('a') + 1))
# Ver onde esta a letra A
