import numpy as np

#создаем случайные матрицы 5x5
A = np.random.randint(1, 11, (5, 5))
B = np.random.randint(1, 11, (5, 5))

print("Матрица A:")
print(A)
print("Матрица B:")
print(B)

#поэлементное произведение
elementwise = A * B
print("Поэлементное произведение:")
print(elementwise)

#матричное произведение
matrix_product = np.dot(A, B)
print("Матричное произведение:")
print(matrix_product)

#определитель A
det_A = np.linalg.det(A)
print(f"Определитель A: {det_A:.2f}")

#транспонированная B
B_transposed = B.T
print("Транспонированная B:")
print(B_transposed)

#обратная матрица A (если возможно)
try:
    A_inv = np.linalg.inv(A)
    print("Обратная матрица A:")
    print(A_inv)
except:
    print("Матрица A необратима")

#решаем систему уравнений A*x = C
C = A.sum(axis=1)  #сумма строк матрицы A
x = np.linalg.solve(A, C)
print("Решение системы A*x = C:")
print(x)