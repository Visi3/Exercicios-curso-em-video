from random import randint
computador = randint(0,5) # Computador pensa em um número

print('\033[33m-=-' * 20)
print('\033[mPensei em um número entre 0 e 5, adivinhe!')
print('\033[33m-=-' * 20)

nmr = int(input('\033[mEm que número pensei? '))

if nmr == computador:
    print('\033[32mVocê ganhou!')
else:
    print('\033[31mVocê perdeu! Eu pensei no número {}'.format(computador))

