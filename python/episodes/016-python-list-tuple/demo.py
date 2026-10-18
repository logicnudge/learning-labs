numbers = [1, 2]
numbers.append(3)
print(numbers)
fixed = (1, 2)
try:
    fixed.append(3)
except AttributeError:
    print("tuple has no append")
