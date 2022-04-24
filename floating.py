import binascii
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
