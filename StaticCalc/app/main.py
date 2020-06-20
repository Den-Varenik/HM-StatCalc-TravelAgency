from lib.calc import StaticCalc


if __name__ == '__main__':

    with open('data.txt', 'r', encoding='utf-8') as file:
        data = [[int(i.strip()) for i in line.split()] for line in file.readlines()]
    for i in data:
        print(StaticCalc(i).coefficient_variation)
