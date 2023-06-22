viagem1, viagem2, viagem3 = [int(i) for i in input().split()]
if viagem1 == viagem2 or viagem1 == viagem3 or viagem2 == viagem3:
    print('S')
elif viagem1 + viagem2 - viagem3 == 0 or viagem1 - viagem2 + viagem3 == 0 or -viagem1 + viagem2 + viagem3 == 0:
    print('S')
else:
    print('N')