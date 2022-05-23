file1 = open('yazı.txt','r')
file2 = open('yazı2.txt','r')
file1words = {""}
file2words = {""}

for line in file1:
    for word in line.split():
        file1words.add(word)

for line in file2:
    for word in line.split():
        file2words.add(word)

s = file1words.intersection(file2words)
existOnly1 = file1words.difference(file2words)
existOnly2 = file2words.difference(file1words)

