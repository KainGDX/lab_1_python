import math

def safe_apply(func, data):
    results = []
    errors = []
    
    for item in data:
        try:
            #пытаемся применить функцию
            result = func(item)
            results.append(result)
        except Exception as e:
            #если ошибка - добавляем в список ошибок
            errors.append((item, type(e).__name__))
    
    return results, errors

#демонстрируем работу функции
data = ['4', '16', 'text', '-25', '9.0']
sqrt_func = lambda x: math.sqrt(float(x))

results, errors = safe_apply(sqrt_func, data)

print("Успешные результаты:", results)
print("Ошибки:", errors)