number = input('enter')

keys = {'A':2, 'B':2, 'C':2,
        'D':3, 'E':3, 'F':3,
        'G':4, 'H':4, 'I':4,
        'J':5, 'K':5, 'L':5,
        'M':6, 'N':6, 'O':6,
        'P':7, 'Q':7, 'R':7,'S':7,
        'T':8, 'U':8, 'V':8,
        'W':9, 'X':9, 'Y':9,'Z':9
        }

splitted_number = number.split('-')
first = splitted_number[0]
second = splitted_number[1]
third = splitted_number[2]

print(first[0],end='')
print(first[1],end='')
print(first[2],end='-')
print(keys[second[0]],end='')
print(keys[second[1]],end='')
print(keys[second[2]],end='-')
print(keys[third[0]],end='')
print(keys[third[1]],end='')
print(keys[third[2]],end='')
print(keys[third[3]],end='')
