class Travels(object):

    def __init__(self, name: str, days: int, price: float):
        self.__name = name
        self.__days = days
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, days):
        self.__days = days

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__days = price

    def __str__(self):
        return f"Name: {self.__name}\nDays: {self.__days}\nPrice: {self.price}"


class Countries(object):

    company_name = "Cheap-Travel"

    def __init__(self, country: str):
        self.__country = country
        self.__offer = list()

    @property
    def country(self):
        return self.__country

    @property
    def offer(self):
        return self.__offer

    def add_offer(self, offer: Travels):
        self.__offer.append(offer) if self.find_offer(offer) == -1 else print('Данное предложение уже существет!')

    def find_offer(self, offer: Travels):
        index = 0
        for offers in self.__offer:
            if offers.name == offer.name:
                return index
            index += 1
        return -1

    def del_offer(self, offer: Travels):
        result = self.find_offer(offer)
        self.__offer.pop(result) if result != -1 else print('Данного предложение не существет!')

    def display(self):
        print(f'{" "*4}{self.__country}')
        [print(offer) for offer in self.__offer]


class TravelAgency(object):

    company_name = "Cheap-Travel"

    def __init__(self):
        self.__base = list()

    @property
    def base(self):
        return self.__base

    def add_country(self, country: Countries):
        self.__base.append(country) if self.find_country(country) == -1 else print('Данное предложение уже существет!')

    def find_country(self, country: Countries):
        index = 0
        for countries in self.__base:
            if countries.country == country.country:
                return index
            index += 1
        return -1

    def del_country(self, country: Countries):
        result = self.find_country(country)
        self.__base.pop(result) if result != -1 else print('Данного предложение не существет!')

    def display(self):
        print(f'---------------{TravelAgency.company_name}-----------------')
        [country.display() for country in self.__base]