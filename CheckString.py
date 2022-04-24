s=raw_input()
an=False
ab=False
dig=False
low=False
up=False

for i in range(len(s)):
    if s[i].isalnum():
        an=True
    if s[i].isalpha():
        ab=True
    if s[i].isdigit():
        dig=True
    if s[i].islower():
        low=True
    if s[i].isupper():
        up=True

print an
print ab
print dig
print low
print up

