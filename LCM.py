def lcm(x,y):
    x=int(x)
    y=int(y)
    if x<y: lar=y
    else: lar=x

    for i in range(lar,x*y+1):
        if i%x==0 and i%y==0:
            return i
    #else:
     #   return x*y

print lcm(6,8)