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
        self.create()

    def create(self) -> None:
        """
        Создать случайный лабиринт с помощью алгоритма поиска в глубину.
        """
        self.field = [[wall for i in range(self.width)] for i in range(self.height)]

        stack = [(1, 1)]
        self.field[1][1] = way

        while stack:
            x, y = stack[-1]

            neighbors = []
            for dx, dy in [(0, -2), (2, 0), (0, 2), (-2, 0)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.width - 1 and 0 < ny < self.height - 1:
                    if self.field[ny][nx] == wall:
                        neighbors.append((nx, ny, dx, dy))

            if neighbors:
                nx, ny, dx, dy = random.choice(neighbors)
                wx, wy = x + dx // 2, y + dy // 2
                self.field[wy][wx] = way
                self.field[ny][nx] = way
                stack.append((nx, ny))
            else:
                stack.pop()

        self.field[1][0] = way
        self.field[self.height - 2][self.width - 1] = way
        self.field[self.height - 2][self.width - 2] = finish
        self.player_x = 1
        self.player_y = 1

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