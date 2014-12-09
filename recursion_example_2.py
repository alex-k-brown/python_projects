def exponent(base, exp, current_value=1):
    if exp == 0:
        return current_value

    current_value *= base
    exp -= 1

    return exponent(base, exp, current_value)

print exponent(8, 8)