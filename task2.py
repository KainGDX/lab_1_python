n = int(input("Число n: "))

print("Числа от 1 до n:")
for i in range(1, n + 1):
    print(i, end=" ")
print()

print("Квадраты чисел от 1 до n:")
for i in range(1, n + 1):
    print(i ** 2, end=" ")
print()

print("Сумма всех чисел от 1 до n:", sum(range(1, n + 1)))