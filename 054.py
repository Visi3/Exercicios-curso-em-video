import datetime
maiores = 0
menores = 0
# Verificar a maioridade de 7 pessoas
for c in range (1,8,1):
   idade = datetime.date.today().year - int(input('Digite o {} ano de nascimento: '.format(c)))

   if  idade >= 18:
       maiores += 1
   else:
       menores += 1

print('{} são maiores de idade\n{} são menores de idade'.format(maiores,menores))

