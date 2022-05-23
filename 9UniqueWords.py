file = open('yazı.txt','r')
   
lines = file.readlines()
wordList = []
words = set()
for line in lines:
    for word in line.split():
        wordList.append(word)
        words.add(word)
        
for i in words:
    if wordList.count(i) == 1:
        print('one of the unique words is : ' + i)
    
