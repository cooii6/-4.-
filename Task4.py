# Завдання 4. Варіант 8
# Сортування бульбашкою

def bubble_sort():
    A = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

    print("Початковий список:", A)

    n = len(A)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    print("Відсортований список:", A)

    return A

bubble_sort()
