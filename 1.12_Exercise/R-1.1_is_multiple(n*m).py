"""A function to check is the first number is multiple of second one or not"""


def is_multi(n: int, m: int) -> bool:
    """
    checks whether n is multiple of m

    :param n: first number
    :param m: second number
    :return: return True if n is multiple of m else false
    """
    div, mod = divmod(n, m)
    if mod == 0:
        return True


n, m = [eval(x) for x in input("Enter 2 no. to check whether is multiple \n").split()]
if not isinstance((n and m), int):
    raise TypeError("No. must be integer")
if n and m < 0:
    raise ValueError("No must be greater than zero")
else:
    result = is_multi(n, m)
    if result:
        print(f'Yes!!!, {n} is multiple of {m}')
    else:
        print(f"No!! {n} is not multiple of {m}")
