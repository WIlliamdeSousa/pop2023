n = float(input())
intervalos = ('[0,25]', '(25,50]', '(50,75]', '(75,100]')
for intervalo in intervalos:
    if intervalo[0] == '[':
        cond1 = n >= int(intervalo.split(',')[0][1:])
    else:
        cond1 = n > int(intervalo.split(',')[0][1:])
    cond2 = n <= int(intervalo.split(',')[1][:-1])
    if cond1 and cond2:
        print('Intervalo', intervalo)
        break
else:
    print('Fora de intervalo')