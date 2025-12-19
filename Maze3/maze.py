import random
from utilities import *


class Maze:
    """
    Данный класс создает и управляет лабиринтом для одного уровня.
    """

    def __init__(self, level: int = 1) -> None:
        """
        Конструктор класса Maze

        :param level: Номер уровня для генерации лабиринта.
        """

        self.level = level
        self.width = 15 + level * 2
        self.height = 11 + level * 2
        self.field = []
        self.player_x = 1
        self.player_y = 1
        self._generate_recursive_backtracker()

    def _generate_recursive_backtracker(self) -> None:
        """
        Генерирует лабиринт с помощью алгоритма Recursive Backtracker
        """

        self.field = [[wall for _ in range(self.width)] for _ in range(self.height)]

        start_x, start_y = 1, 1
        self.field[start_y][start_x] = way

        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]

        def carve(x: int, y: int) -> None:
            """
            Рекурсивно 'прорубает' проходы из текущей клетки

            Args:
                x координата текущей клетки.
                y координата текущей клетки.
            """

            shuffled_directions = directions.copy()
            random.shuffle(shuffled_directions)

            for dx, dy in shuffled_directions:
                next_x, next_y = x + dx, y + dy

                wall_x, wall_y = x + dx // 2, y + dy // 2

                if (0 < next_x < self.width - 1 and
                        0 < next_y < self.height - 1 and
                        self.field[next_y][next_x] == wall):

                    self.field[wall_y][wall_x] = way
                    self.field[next_y][next_x] = way

                    carve(next_x, next_y)

        carve(start_x, start_y)

        self._create_entrance_and_exit()
        self.player_x = 1
        self.player_y = 1

    def _create_entrance_and_exit(self) -> None:
        """
        Создать вход и выход в лабиринте
        """

        self.field[1][0] = way
        self.field[self.height - 2][self.width - 1] = way
        self.field[self.height - 2][self.width - 2] = finish

    def can_move(self, x: int, y: int) -> bool:
        """
        Проверка: можно ли идти в клетку с координатами (x, y).

        Args:
            x: координата x для проверки.
            y: координата y для проверки.

        Returns:
            False: если нельзя двигаться в эту клетку
            True: если можно двигаться в эту клетку
        """

        if x < 0 or x >= self.width or y < 0 or y >= self.height:

            return False

        return self.field[y][x] != wall

    def move_player(self, dx: int, dy: int) -> bool:
        """
        Перемещает игрока на dx по горизонтали и dy по вертикали

        Args:
            dx: смещение по оси x (-1, 0, 1).
            dy: смещение по оси y (-1, 0, 1).

        Returns:
            True: движение выполнено успешно.
            False: движение невозможно.
        """

        new_x = self.player_x + dx
        new_y = self.player_y + dy

        if self.can_move(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y

            return True

        return False

    def at_exit(self) -> bool:
        """
        Проверка: дошел ли игрок до выхода.

        Returns:
            True: если игрок на клетке финиша($).
            False: если игрок не на клетке финиша($).
        """

        return self.field[self.player_y][self.player_x] == finish

    def draw(self) -> str:
        """
        Возвращает строку для отображения лабиринта

        Returns:
            Визуальное представление всего лабиринта с игроком, стенами, путями и финишем.
        """

        result = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                if x == self.player_x and y == self.player_y:
                    row.append(player)
                else:
                    row.append(self.field[y][x])
            result.append(''.join(row))

        return '\n'.join(result)