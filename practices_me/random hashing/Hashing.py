import random
import string


class Hashing:

    def __init__(self):
        pass

    def convert_to_16_bit(self, input):
        binary_string = ""

        if len(input) > 16:
            binary_string = input[:16]
        while len(binary_string) < 16:
            binary_string = '0' + binary_string

        return binary_string

    def random_code(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        random_code = ''.join(random.choice(characters) for _ in range(length))
        return random_code

    def combine_strings_randomly(self, str1, str2, str3):
        combined_characters = list(str1 + str2 + str3)
        random.shuffle(combined_characters)
        combined_result = ''.join(combined_characters)
        return combined_result
