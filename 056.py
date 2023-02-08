media = 0
velho = 0
mulheres = 0
# Verficar várias informações
for c in range(1,5,1):
    nome = str(input('Digite o nome da {} pessoa: '.format(c)))
    idade = int(input('Digite a idade da {} pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {} pessoa: m ou f  '.format(c)))

    media += idade
    if sexo == 'm' and idade > velho:
        homem = nome
    if sexo == 'f' and idade <= 20:
        mulheres += 1
    print('\n')
print('''Média de idade : {}
O homem mais velho: {}
Mulheres com menos de 20 anos: {}'''.format(media / c,homem,mulheres))
