from random import randint
from answers import students
from questions import questions

print("Добро пожаловать в игру Акинатор!")
print("Загадайте студента из группы K3121 и Aкинатор его угадает!")
print("Отвечайте на вопросы в формате: 'да' / 'нет'\n")

student = list(range(len(students)))  # список индексов студентов
question = [i for i in questions.keys()]  # список ключей вопросов
while len(student) != 1:
    n_question = randint(0, len(question) - 1)  # выбираем случайный вопрос
    print(questions[question[n_question]])
    answer = input()
    while answer.lower() != "да" and answer.lower() != "нет":
        print("Неккоректный ответ! Скажите 'да' или 'нет'!")
        answer = input()
    if answer.lower() == "да":
        answer = True
    else:
        answer = False
    for i in student:
        if students[i][question[n_question]] != answer:
            student.remove(i)  # удаляем студента
    if not student:  # если удалили всех студентов
        print("Такого студента нет в списке! Попробуйте сыграть ещё раз.")
        exit(0)
    del question[n_question]  # удаляем вопрос
print("Ваш студент:", students[student[0]]["name"])
