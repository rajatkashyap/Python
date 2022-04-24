from sys import argv 
first,second,third=argv
print first
print second
print third
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print months
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print fat_cat


i=int(raw_input("Enter a number"))
if i in range(0,5):
	print "You enter 0-5"
else: print "Entered a number"

if i in [0,1,2]:
	print "You enter 0,1,2"
else: print "Entered a number"
