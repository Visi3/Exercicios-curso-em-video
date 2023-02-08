sexo = 'p'
# Só parar quando digitar M ou F
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo: ')).upper()
print('Fim! o sexo sigitado foi {}'.format(sexo))

# sexo = str(input('Digite o sexo: ')).strip().upper()[0]
# while sexo not in 'MmFf':
#   sexo = str(input('Dados inválidos! Por favor, informe seu sexo:')).strip().upper()[0]
#print('Sexo {} registrado com sucesso!'.format(sexo))