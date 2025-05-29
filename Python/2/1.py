elements = input("Введите числа через пробел: ").split()
power = int(input("Введите степень: "))

result = []

for element in elements:
    try:
        num = float(element)
        if num.is_integer():
            num = int(num)
        result.append(str(num ** power))
    except ValueError:
        result.append(element * power)

print("Вывод:", " ".join(result))
