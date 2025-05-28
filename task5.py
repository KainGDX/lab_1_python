import random
numbers = [random.randint(1, 100) for _ in range(20)]

print("Список чисел:", numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print("Чётные числа:", even_numbers)

divisible_by_3 = [num for num in numbers if num % 3 == 0]
print("Числа, делящиеся на 3:", divisible_by_3)

average = sum(numbers) / len(numbers)
print("Среднее арифметическое:", average)