"""Задача 19. Телефонная книга с командами.

В начальной телефонной книге 20 демонстрационных записей.
Имена и номера вымышлены. Номера с нулевым кодом оператора
используются только как учебные примеры и не предназначены для звонков.

Команды:
  add <имя> <телефон> [учитель] — добавить или обновить запись
  get <имя>                      — показать телефон
  del <имя>                      — удалить запись
  list                           — показать все записи
  exit                           — завершить программу
"""

contacts = {
    "Айдана": "+996 000 000 001",
    "Бакыт": "+996 000 000 002",
    "Нурбек": "+996 000 000 003",
    "Алина": "+996 000 000 004",
    "Эрлан": "+996 000 000 005",
    "Мээрим": "+996 000 000 006",
    "Тимур": "+996 000 000 007",
    "Айпери": "+996 000 000 008",
    "Данияр": "+996 000 000 009",
    "Жылдыз": "+996 000 000 010",
    "Азат": "+996 000 000 011",
    "Арууке": "+996 000 000 012",
    "Мирлан": "+996 000 000 013",
    "Каныкей": "+996 000 000 014",
    "Самат": "+996 000 000 015",
    "Нуриза": "+996 000 000 016",
    "Бегайым": "+996 000 000 017",
    "Эмир": "+996 000 000 018",
    "Айбек": "+996 000 000 019",
    "Чолпон": "+996 000 000 020",
}
teachers = {"Бакыт"}


def handle_command(command_line):
    parts = command_line.strip().split()
    if not parts:
        return True

    command = parts[0].lower()

    if command == "add":
        if len(parts) not in (3, 4):
            print("Формат: add <имя> <телефон> [учитель]")
        else:
            name, phone = parts[1], parts[2]
            contacts[name] = phone
            if len(parts) == 4 and parts[3].lower() == "учитель":
                teachers.add(name)
            else:
                teachers.discard(name)
            print("добавлено")

    elif command == "get":
        if len(parts) != 2:
            print("Формат: get <имя>")
        elif parts[1] in contacts:
            print(contacts[parts[1]])
        else:
            print("не найдено")

    elif command == "del":
        if len(parts) != 2:
            print("Формат: del <имя>")
        elif parts[1] in contacts:
            del contacts[parts[1]]
            teachers.discard(parts[1])
            print("удалено")
        else:
            print("не найдено")

    elif command == "list":
        for name, phone in contacts.items():
            marker = " (учитель)" if name in teachers else ""
            print(f"{name}: {phone}{marker}")

    elif command in ("exit", "quit"):
        return False

    else:
        print("Неизвестная команда. Доступно: add, get, del, list, exit")

    return True


print("Телефонная книга. Введите list для просмотра записей или exit для выхода.")
while True:
    try:
        line = input("> ")
    except (EOFError, KeyboardInterrupt):
        print()
        break
    if not handle_command(line):
        break
