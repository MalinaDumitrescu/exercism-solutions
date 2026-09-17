def steps(number):
    """Return the number of steps to reach 1 according to the Collatz Conjecture.

    :param number: int - positive integer to test.
    :return: int - number of steps taken to reach 1.
    :raises ValueError: if number is less than or equal to zero.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        count += 1

    return count
