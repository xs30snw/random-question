import json, random

# Записать данные из файла dictionary.json в словарь my_dict
my_dict = {}
with open("dictionary.json", encoding="UTF-8") as my_file:
    my_dict = json.load(my_file)

# Повторять ввод, пока пользователь не введет число
n = 0
while True:
    n = input("Введите количество вопросов и нажмите <Enter> чтобы начать программу: ")
    if n.isdigit():
        n = int(n)
        break

# Показать n вопросов в цикле
for i in range(n):

    # Выбрать случайный вопрос-ответ из словаря
    question, answer = random.choice(list(my_dict.items()))

    print("\n---")
    print('Вопрос ' + str(i+1) + ":")
    print(question)

    input()

    print(answer)

    input()

    # Удалить попавшийся вопрос из словаря, и прекратить программу, если в словаре ничего не осталось
    my_dict.pop(question)
    if len(my_dict) <= 0:
        break

input("\nНажмите <Enter> чтобы выйти из программы")