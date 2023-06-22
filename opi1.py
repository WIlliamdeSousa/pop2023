n = [int(i) for i in input()]
d = int(input())
for i, j in enumerate(n):
    if d > j:
        n.insert(i, d)
        break
else:
    n.append(d)
print(''.join([str(i) for i in n]))