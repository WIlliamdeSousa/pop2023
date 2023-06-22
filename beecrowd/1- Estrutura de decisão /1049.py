vertebrado = input() == 'vertebrado'
if vertebrado:
    ave = input() == 'ave'
    if ave:
        carnivoro = input() == 'carnivoro'
        if carnivoro:
            print('aguia')
        else:
            print('pomba')
    else:
        onivoro = input() == 'onivoro'
        if onivoro:
            print('homem')
        else:
            print('vaca')
else:
    inseto = input() == 'inseto'
    if inseto:
        hematofago = input() == 'hematofago'
        if hematofago:
            print('pulga')
        else:
            print('lagarta')
    else:
        hematofago = input() == 'hematofago'
        if hematofago:
            print('sanguessuga')
        else:
            print('minhoca')
