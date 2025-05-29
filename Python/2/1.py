# Ввод списка элементов
elements = input("Введите числа через пробел: ").split()
power = int(input("Введите степень: "))

result = []

for element in elements:
    try:
        # Пробуем преобразовать элемент в число
        num = float(element)
        # Проверяем, является ли число целым (для красивого вывода)
        if num.is_integer():
            num = int(num)
        # Возводим в степень
        result.append(str(num ** power))
    except ValueError:
        # Если не число - умножаем строку на степень
        result.append(element * power)

print("Вывод:", " ".join(result))