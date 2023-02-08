valor = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos pretende quitar: '))
# Calculo de prestação de empréstimo
meses = anos * 12
prestacao = valor / meses

if ((sal/100) * 30) < prestacao:
    print('\033[31mEmpréstimo negado!\033[m a prestação ficaria {} reais.'.format(prestacao))
else:
    print('\033[32mEmpréstimo aprovado!\033[m A prestação ficará em torno de {:.2f} reais por {} meses.'.format(prestacao,meses))