import random

def generate_reverse_array():
    try:
        n = int(input("Скільки чисел згенерувати? "))
        data = sorted([random.randint(1, 10000) for i in range(n)], reverse=True)
        print("\nВаш результат:\n" + " ".join(map(str, data)))
    except ValueError:
        print("Будь ласка, введіть ціле число.")

generate_reverse_array()