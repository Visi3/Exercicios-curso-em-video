nmr = int(input('Digite um número inteiro:'))
print(''' Escolha uma opção:
1 - Binário
2 - Octal
3 - Hexadecimal''')
# Converter decimal para outras bases
escolha = int(input('Digite sua escolha: '))

if escolha  == 1:
    print('{} convertido para binário é igual a {}'.format(nmr,bin(nmr)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(nmr, oct(nmr)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(nmr, hex(nmr)[2:]))
else:
    print('Escolha incorreta!!')