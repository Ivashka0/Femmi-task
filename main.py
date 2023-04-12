from random import randint


def task(b):
    a = 0
    while a < len(b):  # Сортування бульбашкою списку, свій варіант(1 варіант знаходження найбільшого числа)
        a += 1
        for index in range(len(b) - 1):
            if b[index] > b[index + 1]:
                b[index], b[index + 1] = b[index + 1], b[index]
            else:
                continue
    print(b)
    print(f"Найбільше число - {b[-1]}")

    # print(b)  # 2 варіант знаходження найбільшого,але без циклу
    # print(max(b))

    if b[-1] % 3 == 0 or b[-1] % 5 == 0:
        print(f"Ваше число кратне 3 або 5 - {b[-1]}")  # Кінець
    else:
        while b[-1] % 3 != 0 and b[-1] % 5 != 0:
            if b[-1] % 3 != 0 or b[-1] % 5 != 0:
                if b[-1] % 10 == 0:
                    continue
                else:
                    b[-1] += 2
                    print(b[-1])
                b[-1] += 5
                print(b[-1])
            else:
                break
        print(f"Ваше число кратне 3 або 5 - {b[-1]}")  # Кінець


task([randint(0, 1000) for i in range(0, randint(3, 10))])  # Генератор числового списку
