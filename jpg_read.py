import io
with open('Tulips.jpg', 'rb') as inf:
    jpgdata = inf.readline()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a jpeg file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

print text % len(jpgdata)

print jpgdata