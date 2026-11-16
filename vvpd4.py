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

def f6(arr):
    n = 1
    for string in arr:
        s = sum(string)
        print(f"Сумма {n} строки равна {s}")
        n += 1
    n = 1
    col_s = sum(arr,axis=0)
    for i in range(len(col_s)):
        print(f"Сумма {n} столбца равна {col_s[i]}")
        n += 1
        
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
        if choice == "5":
            break
        if choice == "1":
            a,b = get_size()
        if choice == "2":
            if a == 0 or b == 0:
                print("Сначала введите размер массива в пункте 1")
                continue
            print("1 - Вручную")
            print("2 - Автоматически (случайные числа от 0 до 100)")
            print("0 - Назад")
            choice1 = input("Выберите действие: ")
            if choice1 == "0":
                continue
            if choice1 == "1":
                arr = hands(a,b)
            if choice1 == "2":
                arr = auto(a,b)
        if choice == "3":
            if arr is None:
                print("Сначала заполните массив в пункте 2")
                continue
            print("Массив:")
            print(arr)