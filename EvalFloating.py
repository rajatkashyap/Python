def eval_strfrac(s, base=2):
     
    integral, point, fractional = s.strip().partition('.')
    print integral, point, fractional
    integral_i= int(integral,base)
    s=0
    for i in range(len(fractional)):
    	s=s+int(fractional[i],base)*(base**-(i+1))
    #
    # YOUR CODE HERE
    #
    return float(integral_i+s)

def eval_fp(sign, significand, exponent, base=2):
    #assert sign in ['+', '-'], "Sign bit must be '+' or '-', not '{}'.".format(sign)
    #assert is_valid_strfrac(significand, base), "Invalid significand for base-{}: '{}'".format(base, significand)
    #assert type(exponent) is int
    s=eval_strfrac(significand,base)
    if sign=='+':
    	f=(+1.0) * s * base ** int(exponent)
    else:
    	f=(-1.0) * s * base ** int(exponent)
    return f
#	print((+1.0) * eval_strfrac('1.0100000000000', base=16) * (2**4))

eval_fp('+','1.1001001000011111101101010100010001001000011011100000',2)