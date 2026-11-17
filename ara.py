
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

numbers = [a, b, c]
numbers.sort()
ascending = numbers
descending = sorted(numbers, reverse=True)

minimum = min(numbers)
maximum = max(numbers)

print(f"по возрастанию: {ascending[0]} {ascending[1]} {ascending[2]}")
print(f"по убыванию: {descending[0]} {descending[1]} {descending[2]}")
print(f"мин={minimum}, макс={maximum}")