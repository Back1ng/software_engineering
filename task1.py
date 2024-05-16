from datetime import datetime
from math import sqrt

def main(**kwargs):
    """
    Основная функция, которая принимает именованные аргументы (kwargs)
    
    :param kwargs: именованные аргументы, где ключ - имя точки, значение - список из двух координат [x, y].
    """
    for key in kwargs.items():
        # key[1] - это список координат [x, y]
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        
        # Печатаем результат
        print(result)

if __name__ == '__main__':
    # Фиксируем время начала выполнения программы
    start_time = datetime.now()

    # Вызов основной функции с передачей нескольких пар координат
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )

    # Вычисляем затраченное время
    time_costs = datetime.now() - start_time

    # Печатаем время выполнения программы
    print(f"Время выполнения программы: {time_costs}")
