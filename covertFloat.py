import string
symbols = string.digits + string.uppercase

def convert(number, original_base, new_base, precision=None):
    #from original_base
    integral, point, fractional = number.strip().partition('.')
    num = int(integral + fractional, original_base) * original_base ** -len(fractional)

    #to new_base
    precision = len(fractional) if precision is None else precision
    s = _int_to_base(int(round(num / new_base ** -precision)), new_base)
    if precision:
        return s[:-precision] + '.' + s[-precision:]
    else:
        return s
def _int_to_base(number, new_base):

    # Uses "the division method"
    sign = -1 if number < 0 else 1
    number *= sign
    ans = ''
    while number:
        ans += symbols[number % new_base]
        number //= new_base
    if sign == -1:
        ans += '-'
    return ans[::-1]        

print convert('1.4002000000000', 16,2)
print convert('1.4002000000000', 16,2).ljust(53,'0')