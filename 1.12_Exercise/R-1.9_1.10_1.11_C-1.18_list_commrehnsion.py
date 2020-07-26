import string

# range constructor
a = [i for i in range(50, 90, 10)]  # [50,60,70,80]
b = [i for i in range(8, -10, -2)]  # [8,6,4,2,0,-2,-4,-6,-8]

# List Comprehension
c = [2 ** i for i in range(9)]  # [1,2,4,8,16,32,64]
d = [i * (i + 1) for i in range(10)]  # [0,2,6,12,20,30,42,56,72,90]
e = [i for i in string.ascii_lowercase[:]]  # ['q','b','c','d','e','f',g','h','i','j',....'z']

print(a, b, c, d, e, end='\n')
