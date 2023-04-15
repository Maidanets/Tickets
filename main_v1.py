import datetime

# 000001
# ...
# 999999

numbers = []


def num():
    for i in range(1, 1000000):
        number = f'{i:06}'
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            numbers.append(number)


if __name__ == '__main__':

    datetime1 = datetime.datetime.now()
    num()
    datetime2 = datetime.datetime.now()
    print(f"Кількість щасливих квитків: {len(numbers)}")
    print(f"Час розрахунку склав: {datetime2 - datetime1}")
