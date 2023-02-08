n = int(input('Digite o número: '))
limite = n
fatorial = 1
# Calcular fatorial
while n > 0:
    if n != 0:
        fatorial = fatorial * n
    n -= 1
print('Fatorial de {} é {}'.format(limite, fatorial))
