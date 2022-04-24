def string_match(a, b):
  s=0
  if len(a) <= len(b): s=len(a)
  else: s=len(b)
  #print s
  count=0
  for i in range(s-1):
    if a[i:i+2]==b[i:i+2]:
      count=count+1
  return count
    

    
print string_match('abcde', 'abcd')

