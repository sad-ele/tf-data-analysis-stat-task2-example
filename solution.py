import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 170380561 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Вычисляем выборочное среднее и выборочную дисперсию
    mean = np.mean(distances)
    variance = np.var(distances)

    # Вычисляем статистику критерия
    chi2_stat = sum([(d ** 2) / (24 * variance) for d in distances])

    # Находим границы доверительного интервала
    alpha = 1 - confidence_level
    df = len(distances)
    chi2_left = chi2.ppf(alpha / 2, df)
    chi2_right = chi2.ppf(1 - alpha / 2, df)
    left_boundary = np.sqrt(chi2_stat / chi2_right)
    right_boundary = np.sqrt(chi2_stat / chi2_left)

    return (left_boundary, right_boundary)
