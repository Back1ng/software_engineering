user_input = input("Введите числа, разделенные пробелом: ")
numbers_list = list(map(str.strip, user_input.split()))
numbers_tuple = tuple(numbers_list)

# Вывод результатов
print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)
