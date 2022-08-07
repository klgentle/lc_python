def remove_digit(n, digit):
    """n >= 0, 0 <= digit <= 9 
    ruturn a number that remove digit from n
    >>> remove_digit(180, 1)
    80
    >>> remove_digit(1111, 1)
    0
    >>> remove_digit(8883, 8)
    3
    """
    if n == 0:
        return 0
    if n % 10 == digit:
        return remove_digit(n // 10, digit)

    return n % 10 + remove_digit(n // 10, digit) * 10


if __name__ == "__main__":
    import doctest
    doctest.testmod()
