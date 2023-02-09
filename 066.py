v = c = s = 0
# Verificar quantidade e soma
while True:
    v = int(input('Digite um valor: 999 - SAIR\n'))
    if v == 999:
        break
    s += v
    c += 1
print(f'Você digitou {c} números e a soma entre eles é {s}')
