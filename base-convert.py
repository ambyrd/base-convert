# Following the representation used by bash for numbers up to base 64
# See: https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html
DIGIT_TABLE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 
               'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 
               'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '_']
REVERSE_TABLE = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                 '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 
                 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 
                 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 
                 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, 
                 'A': 36, 'B': 37, 'C': 38, 'D': 39, 'E': 40, 'F': 41, 'G': 42, 
                 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 
                 'O': 50, 'P': 51, 'Q': 52, 'R': 53, 'S': 54, 'T': 55, 'U': 56, 
                 'V': 57, 'W': 58, 'X': 59, 'Y': 60, 'Z': 61, '@': 62, '_': 63}


"""
    Returns the given decimal number expressed in base.
    Supports bases between 2 and 64.
"""
def to_base(decimal, base):
    digits = []
    # Standard algorithm for base conversion--continuously divide by the target base
    # and save the remainders to obtain the representation in the new base
    while (decimal > 0):
        digit = DIGIT_TABLE[decimal % base]
        digits.append(digit)
        decimal = decimal // base
    digits.reverse()  #algorithm calculates digits from least to most significant (ie right to left)
    return "".join(map(str, digits))


"""
    Returns the decimal representation of the input number.
    Supports bases between 2 and 64.  For bases 36 and below, letter case is ignored.
"""
def to_decimal(input, base):
    ignore_case = (base <= 36)  #support using lowercase and uppercase letters interchangeably if we can
    digits = list(str(input))
    digits.reverse()  #so we can start with the 1s place and work upwards
    result = 0
    exp = 0
    for digit in digits:
        if ignore_case:
            digit = digit.lower()
        result += REVERSE_TABLE[digit] * base**exp
        exp += 1
    return result
