# Завдання 1. Варіант 8
# Знайти добуток всіх елементів масиву з непарними індексами

n = int(input("Введіть кількість елементів масиву: "))

arr = []

print("Введіть елементи масиву:")
for i in range(n):
    element = int(input(f"arr[{i}] = "))
    arr.append(element)

product = 1
found = False

for i in range(len(arr)):
    if i % 2 != 0:
        product *= arr[i]
        found = True

print("Масив:", arr)

if found:
    print("Добуток елементів з непарними індексами:", product)
else:
    print("У масиві немає елементів з непарними індексами.")