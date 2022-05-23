file = open('average.txt','r')

lines = file.readlines()
sumOfWords = 0
for i in lines:
    sumOfWords += len(i.split())

average = sumOfWords / len(lines)
print(average)