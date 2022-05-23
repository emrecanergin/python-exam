file = open("yazı.txt")
wordList = []
wordSet = set()


for line in file:
    for word in line.split():
        wordList.append(word)
        wordSet.add(word)
for i in wordSet:
    print(i + ':')
    print(wordList.count(i))



