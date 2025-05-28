import random
numbers = [random.randint(1, 100) for _ in range(10)]
print("Список чисел:", numbers)
print("Максимальное значение:", max(numbers))
print("Минимальное значение:", min(numbers))
print("Сумма всех элементов списка:", sum(numbers))
sorted_numbers = sorted(numbers)
print("Отсортированный список:", sorted_numbers)