import math

from Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int = None, side_c: int = None):
        self.side_a = side_a
        if side_b == None and side_c == None:
            self.side_b = side_a
            self.side_c = side_a
        else:
            self.side_b = side_b
            self.side_c = side_c

    # Метод, возвращающий периметр
    def get_length(self) -> float:
        return self.side_a + self.side_b + self.side_c

    # Метод, возвращающий площадь
    def get_square(self) -> float:
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def check_right_triangle(self):
        if ((self.side_a ** 2 + self.side_b ** 2 == self.side_c ** 2)
                or (self.side_c ** 2 + self.side_b ** 2 == self.side_a)
                or (self.side_a + self.side_c == self.side_b ** 2)):
            return f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} прямоугольный'
        else:
            return f'Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} не прямоугольный'


if __name__ == '__main__':
    while True:
        try:
            a, b, c = map(int, input('Введите параметры сторон треугольника через пробел: ').split())
            break
        except ValueError as e:
            print(f'Ошибка! Повторите ввод!')
    triangle = Triangle(a, b, c)
    print(f'{triangle.get_length():.2f}')
    print(f'{triangle.get_square():.2f}')
    print(triangle.check_right_triangle())
