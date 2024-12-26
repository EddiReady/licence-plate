# Регистр LV номеров \\ by Eddy

# В разработке: 
# - Пользователь мог выбрать конкретные буквы или цифры, с которыми соответственно будут генерироваться цифры или буквы
# - Добавление тех номеров в текстовый файл, которые пользователь захочет

import random
import string
import os
import time

def show_menu():
    # Приветствие, начало программы
    print("Добро пожаловать в программу \"Регистр LV номеров\"!")
    time.sleep(2.5)
    print("Здесь, с помощью рандома, вы можете выбить номер типа XX-1234 для своей тачки! (В разработке)")
    time.sleep(2.5)
    print("Номера, которые Вам понравятся, можно добавить в текстовый файл. (В разработке)")
    time.sleep(2.5)

def full_random():
    pass

def numbers_random():
    pass

def letters_random():
    pass

def main():
    show_menu()
    print()
    print("Выберите желаемое действие:")
    print("1. Рандомные номера")
    print("2. Номер с конкретными буквами, цифры выбираются рандомные")
    print("3. Номер с конкретными цифрами, буквы выбираются рандомные")
    print("4. Выход")
    time.sleep(1.5)
    print()
    choise = int(input("Введите цифру, которую выбрали (1-4): "))
    print()
    if choise == 1:
        full_random()
    elif choise == 2:
        numbers_random()
    elif choise == 3:
        letters_random()
    elif choise == 4:
        print("Спасибо за использование программы! Надеюсь, она вам понравилась!")
        time.sleep(0.5)
        print("Буду рад вашему отзыву и предложениям по улучшению!")
        time.sleep(0.5)
        print("Связь со мной по почте: eduards.levsa@gmail.com")
        input()
        

if __name__ == "__main__":
    main()
