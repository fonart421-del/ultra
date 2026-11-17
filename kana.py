numbers = [1, -2, 3, -4, 0]

result = []

for num in numbers:
    if num > 0:
        result.append(num ** 2)
    else:
        result.append(0)

print(result)