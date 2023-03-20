from cmath import sqrt
from math import calc

message: str = 'Добро пожаловать в самую лучшую программу для вычисления ' \n
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(number: int) -> int:
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number: int) -> int:
    if your_number <= 0:
        return


    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {CalculateSquareRoot(your_number)}')


print(message)
calc(25.5)