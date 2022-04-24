def sol(input):
    out=[]
    for i in range(len(input)):
        if i%2!=0:
            out.append(input[i])

    return out


x=sol([1,-1,2,-2])
print x