idade = int(input('Digite a sua idade: '))
# Verificar categoria de acordo com a idade
if idade <= 9 :
    print('Sua categoria é a Mirim!')
elif 14 >= idade > 9:
    print('Sua categoria é a Infantil!')
elif 19 >= idade > 14:
    print('Sua categoria é a Júnior!')
elif 25 >= idade > 19:
    print('Sua categoria é a Sênior!')
elif idade > 25:
    print('Sua categoria é a Master!')
