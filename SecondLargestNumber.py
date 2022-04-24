n = int(raw_input())
arr = map(int, raw_input().split())
#arr.sort(reverse=True)
s=list(set(arr))
print s
s.sort(reverse=True)
print arr
print s
print s[1]

