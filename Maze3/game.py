from utilities import clear_screen
from maze import Maze
from menu import Menu
import sys


class Game:
    """
    Данный класс управляет всей игрой.
    """

    def __init__(self) -> None:
        """
        Конструктор класса Game
        """
        self.maze = None
        self.level = 1
        self.moves = 0
        self.active = False
        self.menu = Menu()

    def run(self) -> None:
        """
        Главный метод игры, который запускает бесконечный цикл меню
        """
        while True:
            self.menu.show_main()
            choice = input("Выберите: ")
            clear_screen()

            if choice == '1':
                self.start_new()
            elif choice == '2':
                self.menu.show_instructions()
            elif choice == '3':
                print("До свидания!")

                sys.exit()

    def start_new(self) -> None:
        """
        Начать новую игру с первого уровня
        """
        self.level = 1
        self.active = True
        self.play_levels()

    def play_levels(self) -> None:
        """
        Играть все уровни от 1 до 5 подряд.
        """
        while self.active and self.level <= 5:
            self.maze = Maze(self.level)
            self.moves = 0
            self.play_level()

            if self.active and self.level < 5:
                self.menu.level_win(self.level, self.moves)
                choice = input("Выберите: ")
                clear_screen()

                if choice == '1':
                    self.level += 1
                elif choice == '2':
                    self.active = False

            elif self.active and self.level == 5:
                self.menu.game_win()
                self.active = False

    def play_level(self) -> None:
        """
        Играть один уровень лабиринта.
        """
        while self.active:
            self.menu.show_game(self.maze, self.moves, self.level)

            if self.maze.at_exit():

                return

            command = input("Команда: ").lower()
            clear_screen()

            if command in 'WwЦц':
                if self.maze.move_player(0, -1):
                    self.moves += 1
            elif command in 'SsЫы':
                if self.maze.move_player(0, 1):
                    self.moves += 1
            elif command in 'AaФф':
                if self.maze.move_player(-1, 0):
                    self.moves += 1
            elif command in 'DdВв':
                if self.maze.move_player(1, 0):
                    self.moves += 1
            elif command in 'Mm':
                self.active = False

                return

            elif command == 'q':
                print("До свидания!")
                sys.exit()