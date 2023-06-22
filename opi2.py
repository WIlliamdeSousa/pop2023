n = int(input())
notas = [int(i) for i in input().split()]
notas.sort()
resultados = []
for i in range(n):
    valor_ini = notas[i]
    c = 1
    for j in range(i + 1, n):
        if valor_ini + 5 >= notas[j]:
            c += 1
        else:
            break
    resultados.append(c)
print(notas)
print(resultados)
print(max(resultados))
