def longest_palindromic(text):
    palins=[]
    for i in range(len(text)):
        for j in range(0,i):
            sub=text[j:i+1]
            if sub==sub[::-1]:
                palins.append(sub)
    print palins
    print max(palins,key=len)
    print palins.index(max(palins, key=len))
    return palins[palins.index(max(palins, key=len))]


'''if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"'''

print longest_palindromic('rajat')