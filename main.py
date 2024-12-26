# Регистр LV номеров \\ by Eddy
import random
import string

# Выбираются две случайные заглавные буквы
random_letter1 = random.choice(string.ascii_uppercase)
random_letter2 = random.choice(string.ascii_uppercase)

# Выбираются рандомные цифры 
a = str(random.randint(0, 9))
b = str(random.randint(0, 9))
c = str(random.randint(0, 9))
d = str(random.randint(0, 9))

# Циклы
if a == "0":
    a = " "
if a == " " and b == "0":
    b = " "
if a == " " and b == " " and c == "0":
    c = " "
# XX-0110
if a == " " and d == "0":
    d = str(random.randint(0, 1))
    if d == "1":
        a = " "
        d = " "
# XX-0001 -> XX-0100
if a == " " and b == " " and c == " ":
    b = d
    d = " "
# XX-0011 -> XX-0110
if a == " " and b == " ":
    b = c
    c = d
    c = " "
    d = " "
# Вывод
result = random_letter1 + random_letter2 + '-' + a + b + c + d
print(result)