str = input('enter sentence')


vowels = ['a', 'e', 'i', 'o', 'u']

vowelCount = 0
consonantCount = 0

for i in str:
    if i in vowels:
        vowelCount += 1
    elif i != ' ':
        consonantCount += 1

print('vowel count is: ' + str(vowelCount))
print('consonant count is: ' + str(consonantCount))