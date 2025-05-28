n = int(input("Число n: "))

print("Числа от n до 1 в обратном порядке:")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"Факториал {n}:", factorial)
