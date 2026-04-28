import random


def generate_reverse_array():
    try:
        n = int(input("Скільки чисел згенерувати? "))

        data = [random.randint(1, 10000) for _ in range(n)]

        data.sort(reverse=True)

        result = " ".join(map(str, data))

        print("\nВаш результат:")
        print(result)

    except ValueError:
        print("Будь ласка, введіть ціле число.")

generate_reverse_array()