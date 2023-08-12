n_diamantes = int(input())
for i in range(n_diamantes):
    extracao = str(input())
    diamantes = list()
    resultado = 0
    for particula in extracao:
        if particula == '<':
            diamantes.append('<')
        elif particula == '>' and diamantes[-1] == '<':
            diamantes.pop()
            resultado += 1
print(resultado)