def longest_palindromic(text):
	palins=[]
	for i in range(len(text)):
		for j in range(i+1,len(text)):
			sub=text[i:j+1]
			if sub==sub[::-1]:
				palins.append(sub)
	print palins			
	print max(palins)
				

'''if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"'''

print longest_palindromic('artrartrt')