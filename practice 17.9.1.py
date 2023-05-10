def binary_search(arr, x):
    """
    Функция двоичного поиска в отсортированном массиве.
    Возвращает индекс первого элемента, который больше или равен искомому элементу.
    Если такой элемент не найден, возвращает -1.
    """
    l = 0
    r = len(arr) - 1
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

def sort_list(arr):
    """
    Функция сортировки списка arr по возрастанию элементов.
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

input_str = input("Введите последовательность чисел через пробел: ")
input_list = input_str.split()

# Проверка соответствия ввода данных
try:
    input_list = [float(x) for x in input_list]
except ValueError:
    print("Ошибка: введены некорректные данные")
    exit()

x_str = input("Введите число: ")

# Проверка соответствия ввода данных
try:
    x = float(x_str)
except ValueError:
    print("Ошибка: введены некорректные данные")
    exit()

sort_list(input_list)
pos = binary_search(input_list, x)

if pos == -1:
    print("Введенное число меньше всех элементов в последовательности")
else:
    print("Номер позиции элемента: ", pos)
