import os
from fractions import Fraction

def conversion(input_value: str, notation_from: int , notation_to: int) -> str:
    # Support for comma input
    if ',' in input_value:
        input_value = input_value.replace(',', '.')

    decimal_value = conversion_to_decimal(input_value, notation_from)
    return conversion_from_decimal(decimal_value, notation_to)

def __main__():
    """
    Input numeral systems (notations) and value. Validates it. Calculate.

    Args:
        -
        
    Returns:
        -
    """
    
    while(True):
        clear_terminal()
        
        print("Converter\n")

        # Input numeral system
        notation_from = input("Enter notation from (or 0 to exit): ")
        if notation_from == '0' or notation_from == '': break

        notation_to = input("Enter notation to (or 0 to exit): ")
        if notation_to == '0' or notation_to == '': break

        # Validation numeral systems input
        try:
            notation_from = int(notation_from)
            notation_to = int(notation_to)
        except ValueError:
            print("Error: please enter a valid integer")
            continue

        if not (2 <= notation_from <= 36 and 2 <= notation_to <= 36):
            print("Error: base must be between 2 and 36")
            continue

        # Validation input value
        is_positive = True
        while True:
            input_value = input("\nEnter value: ").upper()
            input_value = input_value.replace(" ", "")

            if len(input_value) > 0 and input_value[0] == '-':
                is_positive = False
                input_value = input_value[1:len(input_value)]
            
            if validate_value(input_value, notation_from):
                break
            print(f"Error: value '{input_value}' is not valid for base {notation_from}")
                
        # Calculation
        result = conversion(str(input_value), notation_from, notation_to)
        
        if is_positive == False:
            result = '-' + result

        # Result
        print("\nResult:", result)

        input("Press Enter to continue...")

def conversion_to_decimal(value: str, notation: int) -> str:
    """
    Convert a number from input numeral system to decimal numeral system.

    Args:
        value (str): The input number (integer or fractional, supports '.').
        notation (int): The base of the input numeral system (2-36).

    Returns:
        str: The converted number as a string in the decimal numeral system.
    """

    # Separate the integer and fractional parts
    if is_fraction(value):
        int_p, frac_p = value.split('.')
    else:
        int_p, frac_p = value, ''

    result = Fraction(0)

    # Integer part
    index = len(int_p) - 1

    for ch in int_p:
        if '0' <= ch <= '9':
            digit = int(ch)
        elif 'A' <= ch <= 'Z':
            digit = (ord(ch) - 55)
        elif ch == '.':
            continue

        result += Fraction(digit) * (notation ** index)
        index -= 1

    # Fractional part
    index = -1
    for ch in frac_p:
        if '0' <= ch <= '9':
            digit = int(ch)
        elif 'A' <= ch <= 'Z':
            digit = (ord(ch) - 55)
        elif ch == '.':
            continue

        result += Fraction(digit) * (notation ** index)
        index -= 1

    return str(result)

def conversion_from_decimal(value: str, notation: int) -> str:
    """
    Convert a number from decimal numeral system to the target numeral system.

    Args:
        value (str): The input number (integer or fractional, supports '.').
        notation (int): The base of the input numeral system (2-36).

    Returns:
        str: The converted number as a string in the target numeral system.
    """

    # Separate the integer and fractional parts
    if '.' in value:
        left, right = value.split('.')
        number = Fraction(left) + Fraction(int(right), 10 ** len(right))
    else:
        number = Fraction(value)

    # Integer part
    integer_part = number.numerator // number.denominator
    if integer_part == 0: 
        int_p = "0"
    else:
        result = ""
        int_part_number = integer_part
        while int_part_number > 0:
            remainder = int_part_number % notation

            if 0 <= remainder <= 9:
                remainder = str(remainder)
            elif 10 <= remainder <= 35:
                remainder = chr(remainder + 55) # 'A' = 65, ..., 'Z' = 90

            result += remainder

            int_part_number //= notation

        int_p = result[::-1]

    # Fractional part
    fraction_part = number - integer_part
    if fraction_part > 0:
        frac_p = ""
        precision = 12

        for _ in range(precision):
            fraction_part *= notation
            digit = fraction_part.numerator // fraction_part.denominator
            
            if 0 <= digit <= 9:
                frac_p += str(digit)
            else:
                frac_p += chr(digit + 55)

            fraction_part -= digit

            if fraction_part == 0: 
                break

        return int_p + '.' + frac_p
    else:
        return int_p
    
def validate_value(value: str, notation: int) -> bool:
    """
    Validates input number

    Args:
        value (str): The input number (integer or fractional, supports '.').
        notation (int): The base of the input numeral system (2-36).

    Returns:
        bool: True if number is correct else False
    """

    if value == '':
        return False

    is_dot = False
    for ch in value:
        if '0' <= ch <= '9':
            if int(ch) >= notation:
                return False
        elif 'A' <= ch <= 'Z':
            if ord(ch) - 55 >= notation:
                return False
        elif ch == '.':
            if is_dot:
                return False
            is_dot = True
        else:
            return False
    return True

def is_fraction(value: str) -> bool:
    return '.' in value

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    __main__()
