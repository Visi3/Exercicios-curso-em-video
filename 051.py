count = 1
# 10 primeiros termos dessa progressão
razao = int(input('Digite a razão: '))
termo = int(input('Digite o primeiro termo: '))
dec = termo + (10 - 1) * razao

for c in range(termo,dec + razao,razao):
    print(c)

