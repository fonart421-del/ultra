text = input("Введите строку: ")

text = text.lower()

for sign in ".,!?;:—":
    text = text.replace(sign, "")

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

sorted_words = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, count in sorted_words:
    print(f"{word}: {count}")