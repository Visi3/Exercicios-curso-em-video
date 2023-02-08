nome = str(input('Digite seu nome completo: ')).strip()
print('O primeiro nome é {} e o último é {}'.format(nome[:nome.find(' ')],nome[nome.rfind(' '):]))
# Mostrar o primeiro e o último nome