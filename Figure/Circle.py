from math import pi as pi

from Figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius

    # Метод, возвращающий длину окружности
    def get_length(self) -> float:
        return pi * 2 * self.radius

    # Метод, возвращающий площадь окружности
    def get_square(self) -> float:
        return pi * (self.radius ** 2)


if __name__ == '__main__':
    while True:
        try:
            r = int(input('Введите радиус окружности: '))
            break
        except ValueError as e:
            print(f'Ошибка! Повторите ввод!')
    print(r)
    cir_one = Circle(r)
    print(f'{cir_one.get_length():.2f}')
    print(f'{cir_one.get_square():.2f}')