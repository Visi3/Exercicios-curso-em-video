c  = ma = me = 0
escolha = ''
# Verificar informações
while True :
    if escolha == 'N':
        break
    else:
        sx = str(input('\nDigite o sexo: F/M')).upper().strip()
        idd = int(input('Digite a idade: '))

        if sx == 'M':
            c += 1
        elif sx == 'F' and idd <= 20:
            me += 1

        if idd > 18:
            ma += 1
    escolha = str(input('Escolha se quer continuar: S/N')).upper().strip()

print(f'''\nPessoas maiores de 18 anos: {ma}
Homens: {c}
Mulheres menores de 20 anos: {me}''')
