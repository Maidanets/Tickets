import datetime
from multiprocessing import Process

numbers1 = []  # Для одного процесу
numbers2 = []  # Для двох процесів


def num():  # Для одного процесу
    for i in range(1, 1000000):
        number = f'{i:06}'
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            numbers1.append(number)


def num1():  # Для двох процесів
    for i in range(1, 500000):
        number = f'{i:06}'
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            numbers2.append(number)


def num2():  # Для двох процесів
    for i in range(500000, 1000000):
        number = f'{i:06}'
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            numbers2.append(number)


if __name__ == '__main__':
    # Розрахунок в один процес

    datetime1 = datetime.datetime.now()
    num()
    datetime2 = datetime.datetime.now()
    print(f"\nРозрахунок в один процес:")
    print(f"Кількість щасливих квитків: {len(numbers1)}")
    print(f"Час розрахунку склав: {datetime2 - datetime1}")

    # Розрахунок в два процеси

    proces1 = Process(target=num1())
    proces2 = Process(target=num2())

    datetime1 = datetime.datetime.now()

    proces1.start()
    proces2.start()

    proces1.join()
    proces2.join()

    datetime2 = datetime.datetime.now()
    print(f"\nРозрахунок розділений на два процеси:")
    print(f"Кількість щасливих квитків: {len(numbers2)}")
    print(f"Час розрахунку склав: {datetime2 - datetime1}")

