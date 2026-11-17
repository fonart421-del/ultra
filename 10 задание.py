def count_letters(s):
    vowels = set("аеёиоуыэюяaeiou")
    v = c = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

s = input("Введите строку: ")
v, c = count_letters(s)
print(f"гласных={v}, согласных={c}")