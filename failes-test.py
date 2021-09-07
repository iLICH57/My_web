# *** Работа сфайлами ***

# Создание файла в режиме записи
# f = open("test.txt", 'w')
# # Метод записи
# f.write("Hello world")
# # Обязательный метод закрытия файла
# f.close()

# Контекстный менеджер
# with open("test.txt", 'w') as f:
#     # f.write("Python")
#     # f.write("\n")
#     # f.write("IT sen")
#     print("qwerty", file=f)
#     print("ALESHA", file=f)
#     print("VASYA", file=f)

# Добавление записи
# with open("test.txt", 'a') as f:
#     f.writelines(["qwerty", "python", "12345"])

# Чтение всего файла
# with open("test.txt") as f:
#     text = f.read()

# print(text)

# чтение отдельных строк из файла
with open("test.txt") as f:
    text = f.readline()
    print(text)
    text = f.readline()
    print(text)