from itertools import count
from operator import le


correct = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
answers = []

dosya = open("studentAnswers.txt","r")
veri = dosya.read().splitlines() 

true = 0
false = 0
falseAnswers = []

for i in range(20):
    if correct[i] == veri[i]:
        print('correct')
        true += 1
    else:
        print('false')
        falseAnswers.append(i)
        false +=1

if true >= 15:
    print('passed the exam')

print('your incorrect answers are')
for i in falseAnswers:
    print((i + 1),end=" ")
    

print('\n')
print(true)
print(false)