""" A function to check given no is even or odd without using any multiplication, modulo or division operation"""


def is_evan(k: int) -> bool:
    """
    Check whether k is even or not

    :param k: input number
    :return: True if k is even or false
    """
    is_evan = True
    for i in range(1, k+1):
        is_evan = False if is_evan else True
    return is_evan


k = eval(input("Enter number to check evan or odd \n"))
if not isinstance(k, int):
    raise TypeError("Number must be integer")
result = is_evan(k)
print(f'{k} is even' if result else f'{k} is odd')




