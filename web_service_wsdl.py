# from suds.client import Client
# _client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
# add = getattr(_client.service, 'Add')
# print('addition = ', add(10, 12))

# def reverse_and_remove_space(string):
#     without_space = string.replace(" ", "")
#     result = "".join(reversed(without_space))
#     return result
#
#
# string = 'yyy yy zz zz xx '
# print(reverse_and_remove_space(string))

x = lambda a: a*2
print(x(4))

list1 = [4, 2, 3, 1]
a = list(map(lambda x: x*2, list1))
print(a)
