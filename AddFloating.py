import string
symbols = string.digits + string.ascii_uppercase
def eval_strfrac(s, base=2):
     
    integral, point, fractional = s.strip().partition('.')
    #print integral, point, fractional
    integral_i= int(integral,base)
    s=0
    for i in range(len(fractional)):
    	s=s+int(fractional[i],base)*(base**-(i+1))
    return float(integral_i+s)



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

def fp_bin(v):
	h=v.hex()
	new_h=''
	print h
	#print h[0]
	if h[0]=='0':
		v_sign='+'
		new_h=h[2:]
		p=new_h.find('p')
		s_signif=new_h[:p]
		s_signif=convert(s_signif, 16,2,52).ljust(53,'0')
		if v==0.0: 
			s_signif='0'+s_signif
		v_exp=new_h[p+1:]
	else:
		v_sign='-'
		new_h=h[3:]
		p=new_h.find('p')
		s_signif=new_h[:p]
		s_signif=convert(s_signif, 16,2,52).ljust(53,'0')
		if v==0.0: 
			s_signif='0'+s_signif

		v_exp=new_h[p+1:]
	#v_exp_signif	
	#print v_sign
	print new_h
	print s_signif
	print convert(s_signif, 16,2).ljust(53,'0')
	print v_exp
	return (v_sign,s_signif,int(v_exp))
	#print eval_strfrac('1.4002000000000', 16)
	#print bin(int('4002000000000', 16))[2:].zfill(53)
	#binary_string = binascii.unhexlify(s_signif)
print fp_bin(-0.1)


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



def add_fp_bin(u, v, signif_bits):
    u_sign, u_signif, u_exp = u
    v_sign, v_signif, v_exp = v
    
    # You may assume normalized inputs at the given precision, `signif_bits`.
    u1=eval_fp(u_sign,u_signif,u_exp)
    v1=eval_fp(v_sign,v_signif,v_exp)
    print '*'*100
    print u
    print v
    n=u1+v1
    print n
    tup1= fp_bin(n)
    print tup1
    x,y,z=tup1
    y1=y[:int(signif_bits)+1]
    return (x,y1,z)

u = ('+', '1.010010', 0)
v = ('-', '1.000000', -2)

print add_fp_bin(u,v,7)
