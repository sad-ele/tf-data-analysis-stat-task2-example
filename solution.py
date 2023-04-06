import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 170380561 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Вычисляем выборочное среднее и выборочную дисперсию
    alpha = 1 - p
    chi2_stat = np.sum(x**2) / len(x) / 24
    chi2_left = chi2.ppf(alpha / 2, df=2 * len(x))
    chi2_right = chi2.ppf(1 - alpha / 2, df=2 * len(x))
    left_boundary = np.sqrt((len(x) * chi2_stat) / chi2_right)
    right_boundary = np.sqrt((len(x) * chi2_stat) / chi2_left)
    return left_boundary, right_boundary
