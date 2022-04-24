def checkio(anything):
    def __gt__(self, other):
        return self > other
    def __lt__(self,other):
        return self < other
    def __le__(self,other):
        return self <= other
    def __ne__(self, other):
        return self!=other
    def __ge__(self,other):
        return self>=other
    def __eq__(self,other):
        return self==other

    return None

if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')

'''import re
import math

print checkio(re) <= math
print checkio(80) > 81
print checkio('Hello') < 'World'
print checkio({}) != []
print checkio(5) == ord
assert checkio('Hello') < 'World'''''