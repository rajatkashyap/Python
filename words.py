def break_words(sent):
	words=sent.split()
	return words

def sort_words(sent):
	return sorted(break_words(sent))
	
user_input=raw_input("Pls. enter a sentence: ")

def print_first(words):
	return words.pop()

sorted=sort_words(user_input)
print sorted

print print_first(sorted)