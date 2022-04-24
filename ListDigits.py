def solution(input):
    output = []
    no=str(input)
    for i in no:
        output.append(i)
    return output

print solution(123)
print solution(400)

#assert solution(123) == [1,2,3]
#assert solution(400) == [4,0,0]
