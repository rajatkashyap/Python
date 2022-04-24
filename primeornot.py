try:
    i=int(raw_input())
    if i==1:
        print 'Not prime or composite'
    if i==2:
       print 'Prime'
    for j in range(2,i):
      if i%j==0:
            print "Not Prime"
            break
      else:
          print "Prime"
except:
    print 'Not a number'
