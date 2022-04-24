def cumsum(input):
    output=[]
    sum=0
    for i in input:
        sum=sum+i
        output.append(sum)

    return output


print cumsum([1,21,3,44,5])
