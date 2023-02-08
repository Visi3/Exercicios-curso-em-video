ld1 = float(input('Digite o primeiro comprimento '))
ld2 = float(input('Digite o segundo comprimento '))
ld3 = float(input('Digite o terceiro comprimento '))
# Dizer se pode tranformar um triangulo
if (ld1 + ld2) > ld3 and (ld2 + ld3)  > ld1 and (ld1 + ld3)  > ld2:
    print('Podem formar um triangulo!')
else:
    print('Não podem formar um triangulo!')