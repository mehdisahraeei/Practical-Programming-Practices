class BinaryConv:

    def __init__(self):
        self.default = "input must be string!"

    """
    def decimal_to_binary(self, decimal_number):
        binary_representation = bin(decimal_number)[2:]  # حذف '0b' از نمایش دودویی
        return binary_representation
    """

    def str_binary(self, input):
        binary = ''
        for character in input:
            binary += format(ord(character), '08b')
        return binary

    def convert_input(self, input_value):
        if isinstance(input_value, str):
            return self.str_binary(input_value)
        else:
            return self.default
