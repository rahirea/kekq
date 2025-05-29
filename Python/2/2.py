dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

# Создаем множество ключей
keys_set = set(dct.keys())

# Создаем множество значений
values_set = set(dct.values())

# Объединяем множества
union_set = keys_set | values_set  # или keys_set.union(values_set)

# Выводим результаты
print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединение множеств:", union_set)