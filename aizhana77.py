text = input("Введите строку: ")

vowels = "аеёиоуыэюяaeiou"

vowel_count = 0
consonant_count = 0

for char in text.lower():
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Гласных =", vowel_count)
print("Согласных =", consonant_count)