s = "Three tomatoes are walking down the street"
l=[]
words = s.split()
print words
for word in words:
    leng = len(word)
    l.append(leng)
print l