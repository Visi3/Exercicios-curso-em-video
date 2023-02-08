num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
# Verificando o número maior
if num1 > num2:
    print('O primeiro é maior que o segundo'.format(num1,num2))
elif num2 > num1:
    print('O segundo é maior que o primeiro'.format(num2, num1))
else:
    print('Os dois são iguais!')
