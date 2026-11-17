


import random
import string
from collections import Counter

def to_num(text):
    """Строку -> int, если можно, иначе float."""
    text = text.strip()
    try:
        return int(text)
    except ValueError:
        return float(text)


def read_numbers(prompt, count):
    """Читает count чисел из одной строки (через запятую или пробел)."""
    while True:
        raw = input(prompt).replace(",", " ").split()
        if len(raw) != count:
            print(f"Нужно ввести ровно {count} чис(ла/ел).")
            continue
        try:
            return [to_num(x) for x in raw]
        except ValueError:
            print("Ошибка: введите числа.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def fmt(x):
    """Красивый вывод числа: целые без .0 не трогаем, дробные округляем до 2 знаков."""
    if isinstance(x, float):
        return f"{x:.2f}".rstrip("0").rstrip(".") if x != int(x) else str(x)
    return str(x)

def greet(name):
    name = name.strip()
    if not name:
        return "Имя не введено"
    return f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}"


def task_1():
    print(greet(input("Введите имя: ")))

def analyze_two(a, b):
    parts = [f"сумма={fmt(a + b)}", f"разность={fmt(a - b)}",
             f"произведение={fmt(a * b)}"]
    if b == 0:
        parts.append("деление на ноль")
    else:
        parts.append(f"частное={fmt(round(a / b, 2))}")
        parts.append(f"остаток={fmt(a % b)}")
    return ", ".join(parts)


def task_2():
    a, b = read_numbers("Введите a и b (через запятую): ", 2)
    print(analyze_two(a, b))

def classify(n):
    parity = "чётное" if n % 2 == 0 else "нечётное"
    if n > 0:
        sign = "положительное"
    elif n < 0:
        sign = "отрицательное"
    else:
        sign = "ноль"
    mult5 = "да" if n % 5 == 0 else "нет"
    return f"{parity}, {sign}, кратно 5: {mult5}"


def task_3():
    print(classify(read_int("Введите целое число: ")))



def order_three(a, b, c):
    nums = [a, b, c]
    asc = sorted(nums)
    desc = sorted(nums, reverse=True)
    return (f"по возрастанию: {' '.join(map(str, asc))}\n"
            f"по убыванию: {' '.join(map(str, desc))}\n"
            f"мин={asc[0]}, макс={asc[-1]}")


def task_4():
    a, b, c = read_numbers("Введите три числа (через запятую): ", 3)
    print(order_three(a, b, c))



def mult_table(n):
    width = len(str(n * n))
    lines = []
    for i in range(1, n + 1):
        lines.append(" ".join(str(i * j).rjust(width) for j in range(1, n + 1)))
    return "\n".join(lines)


def task_5():
    n = read_int("Введите N: ")
    if n < 1:
        print("N должно быть >= 1")
    else:
        print(mult_table(n))


def even_sum_prod(n):
    evens = list(range(2, n + 1, 2))
    if not evens:
        return "чётных чисел нет"
    prod = 1
    for e in evens:
        prod *= e
    return f"сумма={sum(evens)}, произведение={prod}"


def task_6():
    print(even_sum_prod(read_int("Введите N: ")))


def factorial_info(n):
    if n < 0:
        return "факториал отрицательного числа не определён"
    f = 1
    for i in range(2, n + 1):
        f *= i
    digits_sum = sum(int(ch) for ch in str(f))
    return f"{n}! = {f}, сумма цифр = {digits_sum}"


def task_7():
    print(factorial_info(read_int("Введите N: ")))


def reverse_words(s):
    return " ".join(s.split()[::-1])   


def task_8():
    print(reverse_words(input("Введите строку: ")))



def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def task_9():
    print(is_palindrome(input("Введите строку: ")))



VOWELS = set("аеёиоуыэюя") | set("aeiou")  


def count_letters(s):
    vowels = consonants = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in VOWELS:
                vowels += 1
            else:
                consonants += 1
    return f"гласных={vowels}, согласных={consonants}"


def task_10():
    print(count_letters(input("Введите строку: ")))



def squares_positive(lst):
    return [x ** 2 if x > 0 else 0 for x in lst]


def read_list():
    raw = input("Введите числа через пробел или запятую: ").replace(",", " ").split()
    return [to_num(x) for x in raw]


def task_11():
    print(squares_positive(read_list()))



def avg_without_even(lst):
    if not lst:
        return None
    odds = [x for x in lst if x % 2 != 0]
    source = odds if odds else lst      
    return sum(source) / len(source)


def task_12():
    print(avg_without_even(read_list()))



def dedupe_with_count(lst):
    counts = {}
    unique = []
    for x in lst:
        if x not in counts:
            counts[x] = 0
            unique.append(x)
        counts[x] += 1
    return unique, counts


def task_13():
    raw = input("Введите элементы через пробел: ").split()
    items = [to_num(x) if x.lstrip("-").replace(".", "", 1).isdigit() else x
             for x in raw]
    unique, counts = dedupe_with_count(items)
    print(unique)
    print(counts)



def min_max_index(lst):
    if not lst:
        return None
    mn_i = mx_i = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[mn_i]:
            mn_i = i
        if lst[i] > lst[mx_i]:
            mx_i = i
    return (f"мин={lst[mn_i]} (индекс {mn_i}), "
            f"макс={lst[mx_i]} (индекс {mx_i})")


def task_14():
    print(min_max_index(read_list()))



def sort_by_parity(lst):
    # ключ: (0 для чётных / 1 для нечётных, само число)
    return sorted(lst, key=lambda x: (x % 2, x))


def task_15():
    print(sort_by_parity(read_list()))



def calculate(expr):
    parts = expr.split()
    if len(parts) != 3:
        return "неверный формат (пример: 10 + 5)"
    try:
        a, b = to_num(parts[0]), to_num(parts[2])
    except ValueError:
        return "неверный формат (пример: 10 + 5)"
    op = parts[1]
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return "деление на ноль" if b == 0 else a / b
    return "а че так можно"


def task_16():
    history = []
    print('Вводите выражения вида "10 + 5". Для выхода - "exit".')
    while True:
        expr = input("> ").strip()
        if expr.lower() == "exit":
            break
        result = calculate(expr)
        print(result)
        history.append(f"{expr} = {result}")
    if history:
        print("\nИстория:")
        for line in history:
            print(" ", line)



def task_17(secret=None):
    if secret is None:
        secret = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуйте угадать!")
    while True:
        guess = read_int("Ваша догадка: ")
        attempts += 1
        if guess == secret:
            word = "попытку" if attempts % 10 == 1 and attempts % 100 != 11 else \
                   "попытки" if attempts % 10 in (2, 3, 4) and attempts % 100 not in (12, 13, 14) else \
                   "попыток"
            print(f"угадал за {attempts} {word}")
            break
        print("меньше" if guess > secret else "больше")



def fizzbuzz(n):
    items = []
    counts = {"Fizz": 0, "Buzz": 0, "FizzBuzz": 0}
    for i in range(1, n + 1):
        if i % 15 == 0:
            items.append("FizzBuzz")
            counts["FizzBuzz"] += 1
        elif i % 3 == 0:
            items.append("Fizz")
            counts["Fizz"] += 1
        elif i % 5 == 0:
            items.append("Buzz")
            counts["Buzz"] += 1
        else:
            items.append(str(i))
    stats = ", ".join(f"{k}: {v}" for k, v in counts.items())
    return ", ".join(items), stats


def task_18():
    line, stats = fizzbuzz(read_int("Введите N: "))
    print(line)
    print(stats)



def phonebook_command(book, command):
    parts = command.strip().split()
    if not parts:
        return "пустая команда"
    cmd = parts[0].lower()

    if cmd == "add" and len(parts) == 3:
        book[parts[1]] = parts[2]
        return "добавлено"
    if cmd == "get" and len(parts) == 2:
        return book.get(parts[1], "не найдено")
    if cmd == "del" and len(parts) == 2:
        if parts[1] in book:
            del book[parts[1]]
            return "удалено"
        return "не найдено"
    if cmd == "list" and len(parts) == 1:
        if not book:
            return "книга пуста"
        return "\n".join(f"{name}: {phone}" for name, phone in book.items())
    return "неизвестная команда"


def task_19():
    book = {}
    print("Команды: add <имя> <телефон>, get <имя>, del <имя>, list, exit")
    while True:
        command = input("> ").strip()
        if command.lower() == "exit":
            break
        print(phonebook_command(book, command))



def word_frequency(text):
    cleaned = text.lower()
    for p in ".,!?;:":
        cleaned = cleaned.replace(p, "")
   
    words = [w for w in cleaned.split() if any(ch.isalnum() for ch in w)]
    counts = Counter(words)
    ordered = sorted(counts.items(), key=lambda kv: -kv[1])
    return ", ".join(f"{w}: {c}" for w, c in ordered)


def task_20():
    print(word_frequency(input("Введите строку: ")))



TASKS = {
    1: ("Приветствие с анализом имени", task_1),
    2: ("Анализ двух чисел", task_2),
    3: ("Класификация числа", task_3),
    4: ("Упорядочить три числа", task_4),
    5: ("Квадратная таблица умножения", task_5),
    6: ("Сумма и произведение чётных", task_6),
    7: ("Факториал и сумма цифр", task_7),
    8: ("Реверс слов", task_8),
    9: ("Палиндром", task_9),
    10: ("Гласные и согласные", task_10),
    11: ("Квадраты положительных", task_11),
    12: ("Среднее без чётных", task_12),
    13: ("Удаление дубликатов с подсчётом", task_13),
    14: ("Мин, макс и индексы", task_14),
    15: ("Сортировка по чётности", task_15),
    16: ("Калькулятор с историей", task_16),
    17: ("Угадай число", task_17),
    18: ("FizzBuzz с подсчётом", task_18),
    19: ("Телефонная книга", task_19),
    20: ("Частотный анализ слов", task_20),
}


def main():
    while True:
        print("\nРешения задач")
        for num, (title, _) in TASKS.items():
            print(f"{num:>2}. {title}")
        print(" 0. Выход")
        choice = input("Номер задачи: ").strip()
        if choice == "0":
            break
        if choice.isdigit() and int(choice) in TASKS:
            print()
            TASKS[int(choice)][1]()
        else:
            print("так нельзя")


if __name__ == "__main__":
    main()