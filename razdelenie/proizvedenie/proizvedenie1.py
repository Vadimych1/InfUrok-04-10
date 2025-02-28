"""
Юля очень любит умножать числа, но она затрудняется умножить больше 2 чисел сразу. Все числа, которые нужно умножить, в промежутке от 0 до 9 включительно.
"""

x = int(input()) # ! Ввод числа
result = 1 # ! Объявляем переменную результата

while x:
    d = x % 10 # ! Берём только последний разряд цифры
    result *= d # ! Умножаем на цифру
    x = x // 10 # ! Убираем последний разряд цифры

print(result) # ! Вывод результата