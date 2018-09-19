
def convert_to_roman_numerals(num):

    numerals_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''

    while num > 0:

        for key, value in sorted(numerals_dict.items(), reverse=True):

            while num / key >= 1:

                result += value
                num -= key

    return result
