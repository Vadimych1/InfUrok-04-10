"""
Андрей очень любит чётные числа, но не может отличать их от нечётных. Помогите ему.
"""

x = int(input()) # ! Ввод числа

p = x % 10 # ! Берём только последний разряд цифры

if p % 2 == 0: # ! Если цифра чётная
    print("Чётное")
else: # ! Если цифра нечётная
    print("Нечётное")

# ! Улучшенный вариант

x = int(input()) # ! Ввод числа

p = x % 2 # ! Проверяем на чётность

if p == 0: # ! Если цифра чётная
    print("Чётное")
else: # ! Если цифра нечётная
    print("Нечётное")