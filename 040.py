nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
# Mostrando resultado de acordo com a média
media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado! Sua média foi {}'.format(media))
elif 5 <= media < 7:
    print('Recuperação! Sua média foi {}'.format(media))
else:
    print('Aprovado! Sua média foi {}'.format(media))
