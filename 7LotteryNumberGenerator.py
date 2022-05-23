import random

numbers = []
for i in range(7):
    number = random.randint(0, 9)
    numbers.append(number)

for i in numbers:
    print(i)

