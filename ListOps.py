# Enter your code here. Read input from STDIN. Print output to STDOUT
L = []
inp = int(raw_input())
'''for i in range(inp):
    x = raw_input().split()
    if x[0] == "insert":
        if x[int(x[1])]!='':
            L.insert(int(x[1]),x[2])
        else:
            del x[int(x[1])]
            L.insert(int(x[1]), x[2])

print L'''


for i in range(inp):
    x = raw_input().split()
    cmd=x[0]
    if x[0] != "print":
        cmd+='('+','.join(x[1:])+')'
        eval('L.'+cmd)
    else:
        print L

print L

