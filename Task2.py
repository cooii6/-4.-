# Завдання 2. Варіант 8
# Заповнити двовимірний масив 7x7 за зразком

n = 7
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(n - j)
    matrix.append(row)

print("Двовимірний масив 7x7:")

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()