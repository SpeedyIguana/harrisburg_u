from math import log10
from typing import assert_never


def true_error(
    true_value: float,
    approximate_value: float,
) -> float:
    return true_value - approximate_value


def approximate_error(
    current_value: float,
    previous_value: float,
) -> float:
    return current_value - previous_value


def true_relative_error(
    true_value: float,
    approximate_value: float,
) -> float:
    return 1 - approximate_value / true_value


def error_tolerance_based_on_significant_digits(
    significant_digits: int,
) -> float:
    return 0.5 * 10 ** (-significant_digits)


def compute_significant_digits(
    error_tolerance: float,
) -> float:
    return log10(0.5 / error_tolerance)
