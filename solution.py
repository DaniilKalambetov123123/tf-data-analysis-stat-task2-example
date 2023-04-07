import pandas as pd
import numpy as np

from scipy.stats import erlang


chat_id = 657892082 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
alpha = 1 - p
    return (2 * x.mean() - 1 + 2 * erlang.ppf(alpha / 2, len(x), loc = 0, scale = 1 / len(x))) / 9025, \
                      (2 * x.mean() - 1 + 2 * erlang.ppf(1 - alpha / 2, len(x), loc = 0, scale = 1 / len(x))) / 9025
