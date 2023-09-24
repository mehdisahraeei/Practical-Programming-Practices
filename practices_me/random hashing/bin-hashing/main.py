from BinaryConv import BinaryConv
from p.Hashing import Hashing

obj1 = BinaryConv()
obj2 = Hashing()

binary_code = obj1.convert_input('hello world')
print('main bin:', binary_code)

binary_16_bit = obj2.convert_to_16_bit(binary_code)
print('shorted bin: ', binary_16_bit)

random = obj2.random_code(8)
print("random: ", random)

print("hashed :", obj2.combine_strings_randomly(binary_16_bit, random, str(binary_16_bit.count('0'))))
