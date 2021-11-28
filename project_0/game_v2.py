"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число, по умолчанию = 1.

    Returns:
        int: Число попыток.
    """
    count = 0
    left_limit = 1 # левая граница предполагаемого числа
    right_limit = 101 # правая граница предполагаемого числа

    while True:
        count += 1
        
        predict_number = np.random.randint(left_limit, right_limit) # предполагаемое число
        if predict_number == number:
            break  # выход из цикла если угадали
        elif predict_number > number:
            right_limit = predict_number # изменяем правую гарницу предполагаемого числа
        else:
            left_limit = predict_number # изменяем левую гарницу предполагаемого числа
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number)) # вызываем функцию, угадывающую число и добавляем в список число попыток

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
