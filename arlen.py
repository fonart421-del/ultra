import random

secret_number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Введите число: "))
    attempts += 1

    if guess > secret_number:
        print("Меньше")
    elif guess < secret_number:
        print("Больше")
    else:
        print(f"Поздравляю! Вы угадали за {attempts} попыток.")
        break