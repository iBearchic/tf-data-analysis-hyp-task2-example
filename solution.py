import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 539822853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Выполняем t-тест для двух независимых выборок
    t_stat, p_value = ttest_ind(x, y, equal_var=False)
    
    # Уровень значимости (alpha)
    alpha = 0.05
    
    # Возвращаем True, если p-значение меньше alpha (различия статистически значимы)
    return p_value < alpha
