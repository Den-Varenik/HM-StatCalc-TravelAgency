from math import sqrt


class StaticCalc(object):

    def __init__(self, sequence: list):
        self.__sequence = sorted(sequence)
        self.__variant = sorted(list(set(sequence)))
        self.__frequency = [sequence.count(i) for i in self.__variant]
        self.__average = sum(sequence)/len(sequence)
        self.__mediana = self.__variant[len(self.__variant)//2]
        self.__moda = self.__variant[self.__frequency.index(max(self.__frequency))]
        self.__amp = max(sequence) - min(sequence)
        self.__variance = sqrt(sum(map(lambda x: x**2, sequence))/len(sequence))
        self.__coefficient_variation = self.__variance/self.__average

    @property
    def average(self):
        return self.__average

    @property
    def mediana(self):
        return self.__mediana

    @property
    def moda(self):
        return self.__moda

    @property
    def amp(self):
        return self.__amp

    @property
    def variance(self):
        return self.__variance

    @property
    def coefficient_variation(self):
        return self.__coefficient_variation

    def __str__(self):
        return f'{self.__sequence}\n{self.__variant}\n{self.__frequency}'
