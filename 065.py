cont = soma = num = ma = me = 0
parada = ''
# Maior, menor e média
while parada in 'Ss' :
    num = int(input('\nDigite um número: '))
    soma += num
    if cont == 1:
        ma = me = num
    else:
        if num > ma:
            ma = num
        if num < me:
            me = num

    cont += 1
    parada = str(input('Deseja continuar? S/N')).strip().upper()
print('''\nA média dos valores é {}\nO menor é {}\nO maior é {}'''.format(soma/cont,me,ma))
print('\nFIM')
