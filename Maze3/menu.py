from utilities import wall, player, finish, clear_screen


class Menu:
    """
    Данный класс отвечает за взаимодействие с меню и отображение самой игры.
    """

    def __init__(self) -> None:
        """
        Конструктор класса Menu
        """

        pass

    def show_main(self) -> None:
        """
        Показать главное меню игры
        """

        clear_screen()
        print("-" * 35)
        print("         ИГРА ЛАБИРИНТ")
        print("-" * 35)
        print("1. Начать новую игру")
        print("2. Как играть")
        print("3. Выход")
        print("-" * 35)

    def show_instructions(self) -> None:
        """
        Показать инструкцию игры
        """

        clear_screen()
        print("-" * 35)
        print("          КАК ИГРАТЬ")
        print("-" * 35)
        print(f"Цель: пройти {5} уровней")
        print("Найдите выход из каждого лабиринта!")
        print("\nУправление:")
        print("  W - вверх")
        print("  S - вниз")
        print("  A - влево")
        print("  D - вправо")
        print("  M - меню")
        print("  Q - выход")
        print("\nСимволы:")
        print(f"  {player} - вы")
        print(f"  {wall} - стена")
        print(f"  {finish} - выход")
        print("-" * 35)
        input("\nНажмите Enter...")

    def show_game(self, maze: any, moves: int, level: int) -> None:
        """
        Показать игровой экран с лабиринтом
        """

        clear_screen()
        print("-" * 35)
        print(f"         ТЕКУЩИЙУРОВЕНЬ {level}")
        print("-" * 35)
        print(maze.draw())
        print("-" * 35)
        print(f"Ходов: {moves}")
        print("Управление: WASD - движение, M - меню, Q - выход")

    def level_win(self, level: int, moves: int) -> None:
        """
        Показать экран победы на уровне
        """

        clear_screen()
        print("-" * 35)
        print(f"        УРОВЕНЬ {level} ПРОЙДЕН!")
        print("-" * 35)
        print(f"Ходов: {moves}")
        print("\n1. Следующий уровень")
        print("2. Меню(Выход)")
        print("-" * 35)

    def game_win(self) -> None:
        """
        Показать экран победы во всей игре
        """

        clear_screen()
        print("-" * 35)
        print("         ВЫ ПРОШЛИ ВСЕ УРОВНИ!")
        print("-" * 35)
        print("         Поздравляем с победой!")
        print("-" * 35)
        input("\nНажмите Enter для продолжения.")