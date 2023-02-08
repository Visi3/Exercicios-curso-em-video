peso = float(input('Digite o seu peso: (Kg)'))
alt = float(input('Digite a sua altura: (M)'))
# Verificar IMC

imc = peso / (alt * alt)
if imc <= 18.5 :
    print('Abaixo do peso!! \nIMC = {:.2f}'.format(imc))
elif 25 >= imc > 18.5:
    print('Peso Ideal!! \nIMC = {:.2f}'.format(imc))
elif 30 >= imc > 25:
    print('Sobrepeso! \nIMC = {:.2f}'.format(imc))
elif 40 >= imc > 30:
    print('Obesidade! \nIMC = {:.2f}'.format(imc))
elif imc > 25:
    print('Obesidade Mórbida! \nIMC = {:.2f}'.format(imc))
