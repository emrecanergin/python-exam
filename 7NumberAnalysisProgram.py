numbers = []
for i in range(20):
    number = int(input('enter a number '))
    numbers.append(number)

total = 0
for i in numbers:
    total += i

print('total: ' + str(total))
print('average: ' + str(total/20))
print('max: ' + str(max(numbers)))
print('min: ' + str(min(numbers)))

