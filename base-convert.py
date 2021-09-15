"""Returns the given decimal number expressed in base"""
def to_base(decimal, base):
    digits = []
    while (decimal > 0):
        digits.append(decimal % base)
        decimal = decimal // base
    digits.reverse()
    return "".join(map(str, digits))


"""Returns the decimal representation of the input number"""
def to_decimal(input, base):
    pass