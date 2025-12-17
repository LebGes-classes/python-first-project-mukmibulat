from maze import Maze
from menu import Menu
from utils import MAX_LEVELS
import sys


class Game:
    """Управляет всей игрой"""

    def __init__(self):
        self.maze = None
        self.level = 1
        self.moves = 0
        self.active = False

    def run(self):
        """Запускает игру"""

        while True:
            Menu.show_main()
            choice = input("Выберите: ")

            if choice == '1':
                self.start_new()
            elif choice == '2':
                Menu.show_instructions()
            elif choice == '3':
                print("До свидания!")

                sys.exit()

    def start_new(self):
        """Начинает новую игру с 1 уровня"""

        self.level = 1
        self.active = True
        self.play_levels()

    def play_levels(self):
        """Играет все уровни подряд"""

        while self.active and self.level <= MAX_LEVELS:
            """Создаем лабиринт для текущего уровня"""

            self.maze = Maze(self.level)
            self.moves = 0

            """Играем этот уровень"""
            self.play_level()

            # Если уровень пройден и есть еще уровни
            if self.active and self.level < MAX_LEVELS:
                Menu.level_win(self.level, self.moves)
                choice = input("Выберите: ")

                if choice == '1':
                    self.level += 1  # Следующий уровень
                elif choice == '2':
                    self.active = False  # Выход в меню

            # Если последний уровень пройден
            elif self.active and self.level == MAX_LEVELS:
                Menu.game_win()
                self.active = False

    def play_level(self):
        """Играет один уровень"""

        while self.active:
            Menu.show_game(self.maze, self.moves, self.level)

            # Проверяем победу
            if self.maze.at_exit():
                return

            # Получаем команду
            command = input("Команда: ").lower()

            # Обрабатываем команду
            if command == 'w':
                if self.maze.move_player(0, -1):
                    self.moves += 1
            elif command == 's':
                if self.maze.move_player(0, 1):
                    self.moves += 1
            elif command == 'a':
                if self.maze.move_player(-1, 0):
                    self.moves += 1
            elif command == 'd':
                if self.maze.move_player(1, 0):
                    self.moves += 1
            elif command == 'm':
                self.active = False  # Выход в меню
                return
            elif command == 'q':
                print("До свидания!")
                sys.exit()