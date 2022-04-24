def checkio1(data):
    dig=False
    up=False
    low=False

    for i in range(len(data)):
        if data[i].isdigit():
            dig=True

        if data[i].isupper():
            up = True

        if data[i].islower():
            low = True


    if dig and up and low and len(data)>=10:
        return True
    else: return False


def checkio(data):
    return(not(len(data)<10 or data.isupper() or data.islower() or data.isdigit() or data.isalpha()))
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty9') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"


