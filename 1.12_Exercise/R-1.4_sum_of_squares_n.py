""" A Program takes a positive integer n and returns the sum of the squares of all the positive integer smaller than n
"""


def sum(elements: list) -> int:
    """
    function to add all the element present in list

    :param elements:  all elements which need to be sum
    :return: addition of all elements
    """
    sum = 0
    for ele in elements:
        sum += ele
    return sum


def square(number: int) -> int:
    """
    function to make list which contains square of till n

    :param number: number n
    :return: addition of all square numbers
    """

    square = [ele**2 for ele in range(number)]
    result = sum(square)
    return result


number = int(input("Enter number\n"))
if not isinstance(number, int):
    raise TypeError("Number must be integer")

print(f'result = {square(number)}')
