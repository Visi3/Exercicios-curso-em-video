import random
# Criando uma ordem aleatória
a1 = input('Digite o nome do aluno 1:')
a2 = input('Digite o nome do aluno 2:')
a3 = input('Digite o nome do aluno 3:')
a4 = input('Digite o nome do aluno 4:')

lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('Ordem de apresentação\n {}'.format(lista))
