from numpy import binary_repr
from non_type_adf import *
# from a1a_type_adf import *
# from a2a_type_adf import *


def toggleKthBit(n, k):
    return n ^ (1 << (k-1))


# a = [3423, 2352, -5234]

with open('non_type_adf.csv', 'w') as f:
    for i in loop_cosine:
        temp = binary_repr(int(float(i)*(2**14)), 14)
        offset_binary = toggleKthBit(int(temp, 2), 14)
        print(temp, end='\n')
        print(str('00') + binary_repr(offset_binary, 14), end='\n', file=f)
