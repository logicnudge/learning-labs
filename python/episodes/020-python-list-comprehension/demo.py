numbers = [1, 2, 3, 4]
via_loop = []
for n in numbers:
    if n % 2 == 0:
        via_loop.append(n * n)
via_comp = [n * n for n in numbers if n % 2 == 0]
print(via_loop)
print(via_comp)
