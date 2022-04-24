'''
(404) 555-1212
(404) 5551212
404-555-1212
404-5551212
404555-1212
4045551212
'''


import re
def parse_phone2 (s):
 
    
    re_p = re.compile ('''^
                           \s*?\(?
                           (?P<area>[0-9][0-9][0-9])
                           \)?-?\s*?
                           (?P<first>[0-9][0-9][0-9])
                           \)?-?
                           (?P<last>[0-9][0-9][0-9][0-9])
                           \s*?
                           $
                        ''',
                        re.VERBOSE)
       
    a=re_p.match(s)#.group('area')
    f=re_p.match(s)#.group('first')
    l=re_p.match(s)#.group('last')
    if not a or not f or not l:
        raise ValueError
    
    if s.strip()[0:1]=='(' and s.strip()[4:5]!=')':
        raise ValueError
    if s.strip()[0:1]!='(' and s.strip()[3:4]==' ':
        raise ValueError    
    #print 'Hi'    
    #print a.group('area')   
    #print f.group('first')
    #print l.group('last')
    return (a.group('area'),f.group('first'),l.group('last'))
#re_p = re.compile('^(?P<area>\s*\(\d\d\d\))')
#print re_p.match('(123)456-7878').group('area')
#print  parse_phone1('(123)456-7878')

def asm_phone2(a, l, r):
    from random import random
    x = random()
    if x < 0.33:
        a2 = '(' + a + ')' + rand_spaces()
    elif x < 0.67:
        a2 = a + '-'
    else:
        a2 = a
    y = random()
    if y < 0.5:
        l2 = l + '-'
    else:
        l2 = l
    return rand_spaces() + a2 + l2 + r + rand_spaces()

def rand_spaces(m=5):
    from random import randint
    return ' ' * randint(0, m)

def gen_digits(k):
    from random import choice # 3.5 compatible; 3.6 has `choices()`
    DIGITS = '0123456789'
    return ''.join([choice(DIGITS) for _ in range(k)])

def pass_phone2(p=None, a=None, l=None, r=None):
    if p is None:
        a = gen_digits(3)
        l = gen_digits(3)
        r = gen_digits(4)
        p = asm_phone2(a, l, r)
    else:
        assert a is not None and l is not None and r is not None, "Need to supply sample solution."
    msg = "Should pass: '{}'".format(p)
    print(msg)
    p_you = parse_phone2(p)
    assert p_you == (a, l, r), "Got {} instead of ('{}', '{}', '{}')".format(p_you, a, l, r)
    
pass_phone2("  (404)   555-1212  ", '404', '555', '1212')
pass_phone2("(404)555-1212  ", '404', '555', '1212')
pass_phone2("  404-555-1212 ", '404', '555', '1212')
pass_phone2("  404-5551212 ", '404', '555', '1212')
pass_phone2(" 4045551212", '404', '555', '1212')
    
for _ in range(5):
    pass_phone2()
    
    
def fail_phone2(s):
    msg = "Should fail: '{}'".format(s)
    print(msg)
    try:
        parse_phone2 (s)
    except ValueError:
        print ("==> Function correctly raised an exception.")
    else:
        raise AssertionError ("Function did *not* raise an exception as expected!")
        
failure_cases = [#'+1 (404) 555-3355',
                 #'404.555.3355',
                 '404 555-3355'
                 #'404 555 3355',
                 #'(404-555-1212'
                ]
for s in failure_cases:
    fail_phone2(s)
    
print("\n(Passed!)")