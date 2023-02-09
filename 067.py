# Tabuada de vários números
while True:
    n = int(input('\nDigite um número: '))
    if n < 0:
        break
    for c in range(0,11,1):
        print(f'{c} x {n} = {c*n}')
    