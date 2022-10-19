import math
x = float (input("Введите x "))
a = float (input("Введите а "))
b = float (input("Введите b "))
Z = math.log(x + a*b) // 7
li = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
print(li[int(Z)])