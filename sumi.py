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

