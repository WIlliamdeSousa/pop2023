campo = [
    [. . . o .],
    [. o . l .],
    [. . o . .]
]
for i, fileira in enumerate(campo):
    for j, espaco_atual in enumerate(fileira):
        if espaco_atual.lower() == 'l':
            lobo_atacou = False
            if i > 0:
                if campo[i - 1][j].lower() == 'o':
                    lobo_atacou = True
            if i < len(campo) - 1:
                if campo[i + 1][j].lower() == 'o':
                    lobo_atacou = True
            if j > 0:
                
