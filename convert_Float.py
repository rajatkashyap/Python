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
eval_strfrac('100.101')
eval_strfrac('3.14', base=10)
eval_strfrac('2c', base=16)
# Test 1: `eval_strfrac_test1` (1 point)

eval_strfrac('f.a', base=16)
eval_strfrac('1101', base=2)
eval_strfrac('-0x1.4002000000000', base=16)
print((+1.0) * eval_strfrac('1.0100000000000', base=16) * (2**4))
print((-1.0) * eval_strfrac('1.4002000000000', base=16) * (2**10))
print eval_strfrac('1.4002000000000',base=16)
