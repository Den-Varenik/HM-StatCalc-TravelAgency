from lib.agency import Travels, Countries, TravelAgency
import pickle


class Provider(object):

    def __init__(self):
        self.__agency = TravelAgency()
        self.__storage = "data.dat"
        self.load_data()

    def load_data(self) -> None:
        try:
            with open(self.__storage, 'rb') as file:
                self.__agency = pickle.load(file)
        except FileNotFoundError or EOFError:
            self.save_data()
            self.load_data()

    def save_data(self) -> None:
        with open(self.__storage, 'wb') as f:
            pickle.dump(self.__agency, f)

    def show_offer(self):
        self.__agency.display()

    def select_by_country(self):
        countries = input('Введите название стран через запятую: ').split(', ')
        for target in countries:
            for country in self.__agency.base:
                if target == country.country:
                    country.display()

    def select_by_price(self):
        print("При поиске по конкретной ценне, одно из полей должно остаться пустым.")
        select_min = input('Введите нижнюю границу поиска: ')
        select_max = input('Введите вернюю границу поиска: ')
        result = None
        try:
            if select_max == '':
                result = self.__search_price(float(select_min))
            elif select_min == '':
                result = self.__search_price(float(select_max))
            elif select_min != '' and select_max != '':
                result = self.__search_range(float(select_min), float(select_max))
            else:
                print('Данные введены не верно')
        except ValueError:
            print('Ошибка, данные введены не верно!')
        if result is not None:
            [print(offer) for offer in result]
        else:
            print('Ничего не найдено!')

    def __search_price(self, price: float) -> list:
        result = list()
        for country in self.__agency.base:
            for offer in country.offer:
                if offer.price == price:
                    result.append(offer)
        return result

    def __search_range(self, select_min: float, select_max: float) -> list:
        result = list()
        for country in self.__agency.base:
            for offer in country.offer:
                if select_min <= offer.price <= select_max:
                    result.append(offer)
        return result

    def select_by_time(self):
        days = None
        try:
            days = int(input('Введите верхнюю границу поиска: '))
        except ValueError:
            print('Число должно быть целым!')
        for country in self.__agency.base:
            for offer in country.offer:
                if offer.days <= days:
                    print(offer)

    def search_by_name(self, target=None):
        if target is None:
            target = input('Введите название тура: ')
        for country in self.__agency.base:
            for offer in country.offer:
                if offer.name == target:
                    print(offer)
                    return offer

    def create_offer(self):
        name = input('Введите название тура: ')
        days = None
        price = None
        try:
            days = int(input('Введите продолжительность тура: '))
        except ValueError:
            print('Длительность тура, должно быть указано в целых числах.')
        try:
            price = float(input('Введите цену: '))
        except ValueError:
            print('Ошибка!')
        target = Travels(name, days, price)
        [print(country.country) for country in self.__agency.base]
        country = input('Введите странну для действующего предложения: ') if len(self.__agency.base) != 0 \
            else self.create_country()
        if country == '':
            country = self.create_country()
        for countries in self.__agency.base:
            if countries.country == country:
                countries.add_offer(target)
        self.save_data()

    def create_country(self):
        country = input('Введите название странны: ')
        if country != '':
            self.__agency.add_country(Countries(country))
            self.save_data()
        else:
            print('Название не может быть пустым!')
            country = self.create_country()
        return country

    def del_offer(self):
        target = input('Введите название тура: ').strip()
        for country in self.__agency.base:
            for offer in country.offer:
                if offer.name == target:
                    country.del_offer(offer)
                    print('Successful')
        self.save_data()

    def del_country(self):
        target = input('Введите название страны для удаления: ').strip()
        for country in self.__agency.base:
            if country.country == target:
                self.__agency.del_country(country)
                print('Successful')
        self.save_data()

    def change_offer(self):
        offer = self.search_by_name(input('Введите название предложения: '))
        if offer is not None:
            while True:
                print('Выберите что вы хотите изменить')
                answer = input('1. Название тура\n'
                               '2. Длительность тура\n'
                               '3. Цену тура\n'
                               '0. Завершить\n'
                               'choice - ')
                if answer == '1':
                    offer.name = input('Введите новое название: ')
                elif answer == '2':
                    long = None
                    try:
                        long = int(input('Введите длительность тура: '))
                    except ValueError:
                        print('Ошибка значения!')
                    offer.days = long
                elif answer == '3':
                    price = None
                    try:
                        price = int(input('Введите новую цену: '))
                    except ValueError:
                        print('Ошибка значения!')
                    offer.price = price
                elif answer == '0':
                    break
                else:
                    print('Не верный ввод!')
                self.save_data()
        else:
            print('Такого тура нет!')
