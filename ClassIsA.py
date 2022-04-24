class first(object):
    def func1(self):
        print "func 1"

class second(object):
    def __init__(self):
        self.first=first()
    def func1(self):
        self.first.func1()
    def func2(self):
        print "func 2"

sec=second()
sec.func1()
sec.func2()

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None