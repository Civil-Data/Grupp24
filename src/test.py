""" this string is a module docstring """

def factorial(n):
    """
    Calculate the factorial of a number.

    :param n: The number to calculate the factorial of.
    :return: The factorial of the number.
    """
    if n == 0:
        return 1

    return n * factorial(n-1)

# Calculate the factorial of 5
print(factorial(5))
