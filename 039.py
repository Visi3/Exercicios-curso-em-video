import datetime
ano = int(input('Digite seu ano de nascimento:'))

idade = datetime.date.today().year - ano
# Verificar idade de alistamento militar
if idade > 18:
    print('Já passou {} anos da idade de se alistar.'.format(idade - 18))
elif idade == 18:
    print('Esta na idade de se alistar.')
elif idade < 18:
    print('Faltam {} anos para você se alistar.'.format(18 - idade))