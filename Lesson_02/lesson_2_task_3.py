import math
def square(number):
    return (number * number)
number = float(input("Введите длинну стороны: "))
result = math.ceil(square(number))
print (f"Площадь квадрата равна: {result}")