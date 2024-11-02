from typing import Any
import math


def ft_mean(data) -> int:
    mean = sum(data) / len(data)
    return mean


def ft_median(data) -> int:
    mid = len(data) // 2
    median = (
        data[mid] if len(data) % 2 == 1 else (data[mid - 1] + data[mid]) / 2)
    return median


def get_quartile_value(data: list[float], percentile: float) -> float:
    n = len(data)
    index = n * percentile
    position = math.ceil(index) if not index.is_integer() else int(index)
    return data[position - 1]  # Adjust for 0-based index


def ft_quartile(data: list[float]) -> list[float]:
    quartile = []
    quartile.append(get_quartile_value(data, 1/4))  # Q1 (25%)
    quartile.append(get_quartile_value(data, 3/4))  # Q3 (75%)
    return quartile


def standard_deviation(data) -> float:
    std = viation(data) ** 0.5
    return std


def viation(data) -> float:
    var_part1 = 0
    mean = sum(data) / len(data)
    for elem in data:
        var_part1 += (elem - mean) ** 2
    var = var_part1 / len(data)
    return var


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    # Ensure all args are numeric
    try:
        data = sorted([float(x) for x in args])
    except ValueError:
        print("ERROR")
        return

    # Calculate statistics as requested in kwargs
    for key, elem in kwargs.items():
        if len(data) == 0:
            print("ERROR")
            continue

        if elem == 'mean':
            print('mean : ', ft_mean(data))

        if elem == 'median':
            print("median : ", ft_median(data))

        if elem == 'quartile':
            print('quartile : ', ft_quartile(data))

        # Standard deviation calculation
        if elem == 'std':
            print('std : ', standard_deviation(data))

        if elem == 'var':
            print("var : ", viation(data))
