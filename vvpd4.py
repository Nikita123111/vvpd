from numpy import *

def get_size():
    print("Введите ширину и высоту массива через пробел:")
    a, b = map(int,input().split())
    return a, b

def hands(a,b):
    arr = zeros((b,a), dtype=int)
    for i in range(b):
        for j in range(a):
            arr[i][j] = int(input(f"Введите элемент под индексом [{i}],[{j}]: "))
    print("Массив создан")
    return arr

def auto(a,b):
    arr = random.randint(0,101, size=(b,a))
    print("Массив создан")
    return arr

def main():
    a, b = 0, 0
    arr = None
    while True:
        print("МЕНЮ")
        print("1 - Ввод размера массива")
        print("2 - Создание массива")
        print("3 - Просмотр созданного массива")
        print("4 - Выполнение функций")
        print("5 - Выход")

        choice = input("Выберите действие: ")