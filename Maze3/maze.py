import random
from utils import *


class Maze:
    """Создает и управляет лабиринтом для одного уровня"""

    def __init__(self, level=1):
        self.level = level
        # Размер лабиринта увеличивается с каждым уровнем
        self.width = 15 + level * 2
        self.height = 11 + level * 2
        self.field = []
        self.player_x = 1
        self.player_y = 1
        self.visited = []
        self.create()

    def create(self):
        """Создает случайный лабиринт"""

        #Создаем поле из стен
        self.field = [[WALL for _ in range(self.width)] for _ in range(self.height)]

        #Алгоритм для генерации (простой DFS)
        stack = [(1, 1)]  # Начальная клетка
        self.field[1][1] = WAY

        while stack:
            x, y = stack[-1]

            # Ищем соседей (через одну клетку)
            neighbors = []
            for dx, dy in [(0, -2), (2, 0), (0, 2), (-2, 0)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.width - 1 and 0 < ny < self.height - 1:
                    if self.field[ny][nx] == WALL:
                        neighbors.append((nx, ny, dx, dy))

            if neighbors:
                # Берем случайного соседа
                nx, ny, dx, dy = random.choice(neighbors)

                # Убираем стену между клетками
                wx, wy = x + dx // 2, y + dy // 2
                self.field[wy][wx] = WAY
                self.field[ny][nx] = WAY
                stack.append((nx, ny))
            else:
                # Возвращаемся назад
                stack.pop()

        # 3. Делаем вход и выход
        self.field[1][0] = WAY  # Вход слева
        self.field[self.height - 2][self.width - 1] = WAY  # Выход справа
        self.field[self.height - 2][self.width - 2] = EXIT  # Помечаем выход

        # 4. Настраиваем игрока
        self.player_x = 1
        self.player_y = 1

        # 5. Отмечаем посещенные клетки
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.visited[1][1] = True

    def can_move(self, x, y):
        """Проверяет, можно ли идти в клетку"""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.field[y][x] != WALL

    def move_player(self, dx, dy):
        """Перемещает игрока"""
        new_x = self.player_x + dx
        new_y = self.player_y + dy

        if self.can_move(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y
            self.visited[new_y][new_x] = True
            return True
        return False

    def at_exit(self):
        """Проверяет, дошел ли игрок до выхода"""
        return self.field[self.player_y][self.player_x] == EXIT

    def draw(self):
        """Возвращает строку для отображения лабиринта"""
        result = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if x == self.player_x and y == self.player_y:
                    row.append(PLAYER)
                elif self.visited[y][x] and self.field[y][x] == WAY:
                    row.append(VISITED)
                else:
                    row.append(self.field[y][x])
            result.append(''.join(row))
        return '\n'.join(result)