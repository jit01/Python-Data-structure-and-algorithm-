"""A function to return minimum and maximum number from given sequence data without using inbuilt functions"""


def minmax(data: list) -> tuple:
    """
    function to check min and max values

    :param data: sequence of data in list format
    :return: min and max values in tuple
    """
    data_min, data_max = data[0], data[1]
    for no in data[2:]:
        if data_min > no:
            data_max = no
        if data_max > no:
            data_min = no
    return data_min, data_max


data = [eval(x) for x in input("Enter the number of list to see (min, max) values \n").split()]
print(data)
da_min, da_max = minmax(data)
print(da_min, da_max)

