import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(options):
    clear_screen()
    print("=" * 50)
    print("МОЙ СОФТ(ПРОВЕРКА)".center(50))
    print("=" * 50)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("=" * 50)


def main():
    options = [
        "Открыть",
        "сделать",
        "выход"
    ]

    while True:
        print_menu(options)
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            input("Открываем файл... Нажмите Enter для возврата в меню.")
        elif choice == "2":
            input("Делаем файл... Нажмите Enter для возврата в меню.")
        elif choice == "3":
            input("Выход из софта...")
            break
if __name__ == "__main__":
    main()