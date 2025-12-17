from utils import*


class Menu:
    """Управляет меню и отображением игры"""

    @staticmethod
    def show_main():
        """Показывает главное меню"""

        clear_consol()
        print("-" * 35)
        print("          ИГРА ЛАБИРИНТ")
        print("-" * 35)
        print("1 - Начать новую игру")
        print("2 - Инструкция для игры")
        print("3 - Выход")
        print("-" * 35)

    @staticmethod
    def show_instructions():
        """Показывает инструкцию"""

        clear_consol()
        print("-" * 35)
        print("            КАК ИГРАТЬ")
        print("-" * 35)
        print(f"Цель: пройти {MAX_LEVELS} уровней")
        print("Найдите выход из каждого лабиринта!")
        print("\nУправление:")
        print("  W - вверх")
        print("  S - вниз")
        print("  A - влево")
        print("  D - вправо")
        print("  M - меню")
        print("  Q - выход")
        print("\nСимволы:")
        print(f"  {PLAYER} - вы")
        print(f"  {WALL} - стена")
        print(f"  {EXIT} - выход")
        print(f"  {VISITED} - ваш путь")
        print("-" * 35)
        input("\nНажмите Enter...")

    @staticmethod
    def show_game(maze, moves, level):
        """Показывает игровой экран"""

        clear_consol()
        print("-" * 35)
        print(f"           УРОВЕНЬ {level}")
        print("-" * 35)
        print(maze.draw())
        print("-" * 35)
        print(f"Ходов: {moves}")
        print("Управление: WASD - движение, M - меню, Q - выход")

    @staticmethod
    def level_win(level, moves):
        """Показывает победу на уровне"""

        clear_consol()
        print('-' * 35)
        print(f"          УРОВЕНЬ {level} ПРОЙДЕН!")
        print('-' * 35)
        print(f"Ходов было сделано Вами: {moves}")
        print("\n1. Следующий уровень")
        print("2. Меню")


    @staticmethod
    def game_win():
        """Показывает победу во всей игре"""

        clear_consol()
        print('-' * 35)
        print('          ИГРА ПРОЙДЕНА!')
        print('-' * 35)