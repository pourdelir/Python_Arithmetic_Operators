"""A collection of reusable math helper functions."""

from __future__ import annotations

import math
from functools import reduce
from statistics import median as _median
from typing import Iterable


Number = int | float


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Cannot take modulo by zero")
    return a % b


def floor_divide(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Cannot floor divide by zero")
    return a // b


def power(base: Number, exponent: Number) -> Number:
    return base**exponent


def square(value: Number) -> Number:
    return value * value


def cube(value: Number) -> Number:
    return value * value * value


def square_root(value: Number) -> float:
    if value < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(value)


def cube_root(value: Number) -> float:
    if value < 0:
        return -abs(value) ** (1 / 3)
    return value ** (1 / 3)


def nth_root(value: Number, n: int) -> float:
    if n == 0:
        raise ValueError("Root degree cannot be zero")
    if value < 0 and n % 2 == 0:
        raise ValueError("Cannot calculate an even root of a negative number")
    if value < 0:
        return -abs(value) ** (1 / n)
    return value ** (1 / n)


def absolute(value: Number) -> Number:
    return abs(value)


def reciprocal(value: Number) -> float:
    if value == 0:
        raise ValueError("Cannot calculate reciprocal of zero")
    return 1 / value


def factorial(value: int) -> int:
    if value < 0:
        raise ValueError("Cannot calculate factorial of a negative number")
    return math.factorial(value)


def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    return math.lcm(a, b)


def is_even(value: int) -> bool:
    return value % 2 == 0


def is_odd(value: int) -> bool:
    return value % 2 != 0


def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    if value <= 3:
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= value:
        if value % divisor == 0 or value % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def degrees_to_radians(degrees: Number) -> float:
    return math.radians(degrees)


def radians_to_degrees(radians: Number) -> float:
    return math.degrees(radians)


def sine(radians: Number) -> float:
    return math.sin(radians)


def cosine(radians: Number) -> float:
    return math.cos(radians)


def tangent(radians: Number) -> float:
    return math.tan(radians)


def logarithm(value: Number, base: Number = math.e) -> float:
    if value <= 0:
        raise ValueError("Logarithm value must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(value, base)


def natural_log(value: Number) -> float:
    return logarithm(value)


def log10(value: Number) -> float:
    return logarithm(value, 10)


def mean(values: Iterable[Number]) -> float:
    items = _as_list(values)
    return sum(items) / len(items)


def median(values: Iterable[Number]) -> Number:
    return _median(_as_list(values))


def product(values: Iterable[Number]) -> Number:
    items = _as_list(values)
    return reduce(lambda left, right: left * right, items, 1)


def percentage(part: Number, whole: Number) -> float:
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100


def percentage_change(original: Number, new: Number) -> float:
    if original == 0:
        raise ValueError("Original value cannot be zero")
    return ((new - original) / original) * 100


def clamp(value: Number, minimum: Number, maximum: Number) -> Number:
    if minimum > maximum:
        raise ValueError("Minimum cannot be greater than maximum")
    return max(minimum, min(value, maximum))


def round_to(value: Number, digits: int = 0) -> Number:
    return round(value, digits)


def _as_list(values: Iterable[Number]) -> list[Number]:
    items = list(values)
    if not items:
        raise ValueError("Values cannot be empty")
    return items
