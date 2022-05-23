file = open('average.txt','r')

words = file.read().split()

upperCase = 0
lowerCase = 0
digitCase = 0
spaceCase = 0

for word in words:
    for letter in word:
        if letter.isupper():
            upperCase +=1
        elif letter.islower():
            lowerCase +=1
        elif letter.isdigit():
            digitCase +=1
            
char = file.read(1)
for i in char:
    if i.isspace():
        spaceCase +=1

print(upperCase)
print(lowerCase)
print(digitCase)
print(spaceCase)

