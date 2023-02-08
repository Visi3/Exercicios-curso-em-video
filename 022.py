nome = str(input('Digite um nome:')).strip()


print(nome.upper()) # Todas Maiusculas
print(nome.lower()) # Todas Minusculas

print('Possui {} letras.'.format(len(nome) - nome.count(' '))) # Quantas letras tem

print('O primeiro nome tem {} letras.'.format(nome.find(' '))) # Quantas letras tem o primeiro nome

#Separa = nome.split()
#print('O primeiro nome tem {} letras'.format(len(Separa[0])))
