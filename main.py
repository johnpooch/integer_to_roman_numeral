
import math


def next_power_of_10(x):
    return 1 if x == 0 else 10**math.ceil(math.log10(x))


def convert_to_roman_numerals(num):

    numerals_dict = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }

    result = ''

    while num > 0:

        for key, value in sorted(numerals_dict.items(), reverse=True):

            upper_value = next_power_of_10(num)

            while num / key >= 1:

                if not num >= 1000:

                    if ((num + (upper_value / 10)) % (upper_value / 2)) < (upper_value / 10):

                        if (num % upper_value) > (upper_value / 2):
                            result += numerals_dict[upper_value / 10] + numerals_dict[upper_value]
                            num -= upper_value - (upper_value / 10)
                        else:
                            result += numerals_dict[upper_value / 10] + numerals_dict[upper_value / 2]
                            num -= (upper_value / 2) - (upper_value / 10)

                        continue

                result += value
                num -= key

    return result
