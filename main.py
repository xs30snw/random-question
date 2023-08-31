import json, random

# Записать данные из файла dictionary.json в словарь my_dict
my_dict = {}
with open("dictionary.json", encoding="UTF-8") as my_file:
    my_dict = json.load(my_file)

input("Нажмите <Enter> чтобы начать программу")

# Показать 3 вопроса в цикле
for n in range(3):

    # Выбрать случайный вопрос-ответ из словаря
    question, answer = random.choice(list(my_dict.items()))

    print("\n---")
    print('Вопрос ' + str(n+1) + ":")
    print(question)

    input()

    print(answer)

    input()

    # Удалить попавшийся вопрос из словаря, и прекратить программу, если в словаре ничего не осталось
    my_dict.pop(question)
    if len(my_dict) <= 0:
        break

input("\nНажмите <Enter> чтобы выйти из программы")