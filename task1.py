a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

print("Наибольшее число:", max(a, b, c))
print("Наименьшее число:", min(a, b, c))

if a == b == c:
    print("Все числа равны")
else:
    print("Числа не равны")
