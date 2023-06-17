c = 1
while (n := int(input())) != 0:
    ingressos = [int(i) for i in input().split()]
    print(f'Teste {c}')
    c += 1
    for i, num, in enumerate(ingressos):
        if i + 1 == num:
            print(num)
            break
    print()