from lib.assistant import Menu
from lib.provider import Provider


if __name__ == '__main__':

    menu = Menu()
    provider = Provider()
    index = 0
    while True:
        if index == 0:
            menu.main_display()
        else:
            menu.mange_display()
        choice = menu.get_choice()

        if choice == 1:
            provider.show_offer() if index == 0 else provider.create_offer()
        elif choice == 2:
            provider.select_by_country() if index == 0 else provider.create_country()
        elif choice == 3:
            provider.select_by_price() if index == 0 else provider.del_offer()
        elif choice == 4:
            provider.select_by_time() if index == 0 else provider.del_country()
        elif choice == 5:
            provider.search_by_name() if index == 0 else provider.change_offer()
        elif choice == 6:
            index = 1 if index == 0 else 0
        else:
            print('ВЫ выбрали несуществующий вариант!')
