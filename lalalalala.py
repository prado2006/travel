# ==========================================
# ИГРА "ВОКРУГ СВЕТА"
# Большой пример проекта на Python
# ==========================================

import random
import time

# ==========================================
# ДАННЫЕ ИГРОКА
# ==========================================

player_name = input("Введите имя путешественника: ")

money = 500
health = 100
score = 0
days = 1

inventory = []

# ==========================================
# СПИСОК ГОРОДОВ
# ==========================================

cities = {
    "Лондон": ["Париж", "Берлин"],
    "Париж": ["Рим", "Мадрид"],
    "Берлин": ["Москва", "Прага"],
    "Рим": ["Каир", "Афины"],
    "Москва": ["Пекин", "Токио"],
    "Пекин": ["Сеул", "Бангкок"],
    "Токио": ["Сидней"],
}

current_city = "Лондон"

# ==========================================
# СЛУЧАЙНЫЕ СОБЫТИЯ
# ==========================================

events = [
    {
        "text": "Вы нашли клад!",
        "money": 100,
        "health": 0
    },
    {
        "text": "На вас напали грабители!",
        "money": -50,
        "health": -20
    },
    {
        "text": "Вы вкусно поели в ресторане.",
        "money": -30,
        "health": 10
    },
    {
        "text": "Вы заболели в дороге.",
        "money": -20,
        "health": -30
    },
    {
        "text": "Вы выиграли билет!",
        "money": 80,
        "health": 0
    }
]

# ==========================================
# ВОПРОСЫ ВИКТОРИНЫ
# ==========================================

questions = [
    {
        "question": "Столица Франции?",
        "answer": "Париж"
    },
    {
        "question": "Столица Японии?",
        "answer": "Токио"
    },
    {
        "question": "Столица Италии?",
        "answer": "Рим"
    },
    {
        "question": "Столица России?",
        "answer": "Москва"
    }
]

# ==========================================
# ФУНКЦИЯ ПОКАЗА СТАТИСТИКИ
# ==========================================

def show_stats():
    print("\n========================")
    print("Игрок:", player_name)
    print("Город:", current_city)
    print("День:", days)
    print("Деньги:", money)
    print("Здоровье:", health)
    print("Очки:", score)
    print("Инвентарь:", inventory)
    print("========================\n")

# ==========================================
# ФУНКЦИЯ СЛУЧАЙНОГО СОБЫТИЯ
# ==========================================

def random_event():
    global money
    global health

    event = random.choice(events)

    print("\nСЛУЧАЙНОЕ СОБЫТИЕ")
    print(event["text"])

    money += event["money"]
    health += event["health"]

    print("Изменение денег:", event["money"])
    print("Изменение здоровья:", event["health"])

# ==========================================
# ФУНКЦИЯ ПОКУПКИ
# ==========================================

def shop():
    global money

    items = {
        "Аптечка": 50,
        "Компас": 30,
        "Еда": 20,
        "Фонарик": 40
    }

    print("\nМАГАЗИН")

    for item, price in items.items():
        print(item, "-", price)

    choice = input("Что купить? ")

    if choice in items:

        if money >= items[choice]:
            money -= items[choice]
            inventory.append(choice)

            print("Вы купили:", choice)

        else:
            print("Недостаточно денег")

    else:
        print("Такого предмета нет")

# ==========================================
# ФУНКЦИЯ ВИКТОРИНЫ
# ==========================================

def quiz():
    global score

    question = random.choice(questions)

    print("\nВИКТОРИНА")
    print(question["question"])

    answer = input("Ваш ответ: ")

    if answer.lower() == question["answer"].lower():
        print("Правильно!")
        score += 10
    else:
        print("Неправильно!")
        print("Правильный ответ:", question["answer"])

# ==========================================
# ФУНКЦИЯ ПУТЕШЕСТВИЯ
# ==========================================

def travel():
    global current_city
    global money
    global days

    if current_city not in cities:
        print("Из этого города нельзя путешествовать")
        return

    print("\nДоступные города:")

    available = cities[current_city]

    for city in available:
        print("-", city)

    destination = input("Куда поехать? ")

    if destination in available:

        cost = random.randint(40, 120)

        print("Стоимость поездки:", cost)

        if money >= cost:

            money -= cost
            current_city = destination
            days += 1

            print("Вы прибыли в:", current_city)

            random_event()

        else:
            print("Недостаточно денег")

    else:
        print("Нельзя поехать в этот город")

# ==========================================
# ФУНКЦИЯ ОТДЫХА
# ==========================================

def rest():
    global health
    global days

    print("\nВы отдыхаете...")
    time.sleep(1)

    health += 20

    if health > 100:
        health = 100

    days += 1

    print("Здоровье восстановлено")

# ==========================================
# ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ
# ==========================================

while True:

    if health <= 0:
        print("\nИгра окончена.")
        print("Ваш персонаж потерял здоровье.")
        break

    if money <= 0:
        print("\nИгра окончена.")
        print("У вас закончились деньги.")
        break

    show_stats()

    print("1 - Путешествовать")
    print("2 - Магазин")
    print("3 - Викторина")
    print("4 - Отдых")
    print("5 - Выход")

    choice = input("Выберите действие: ")

    # ======================================
    # ВЫБОР ДЕЙСТВИЯ
    # ======================================

    if choice == "1":
        travel()

    elif choice == "2":
        shop()

    elif choice == "3":
        quiz()

    elif choice == "4":
        rest()

    elif choice == "5":
        print("\nСпасибо за игру!")
        break

    else:
        print("Неверный выбор")

# ==========================================
# КОНЕЦ ИГРЫ
# ==========================================

print("\n======== ИТОГИ ========")
print("Игрок:", player_name)
print("Очки:", score)
print("Прожито дней:", days)
print("Финальный город:", current_city)
print("=======================")
