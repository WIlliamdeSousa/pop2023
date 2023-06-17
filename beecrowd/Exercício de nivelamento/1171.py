n = int(input())
nums = list()
for i in range(n):
    nums.append(int(input()))
unicos = set(nums)
for num in sorted(unicos):
    print(f'{num} aparece {nums.count(num)} vez(es)')