valor = float(input('Digite o valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0
# Simulador caixa eletrônico
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} nota de {ced}')
            totced = 0
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            if total == 0:
                break

