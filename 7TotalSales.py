sales = []
daysOfweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in daysOfweek:
    sale = int(input(i +  ' sale?'))
    sales.append(sale)

total = 0
for sale in sales:
    total += sale

print('total sale is : ' + str(total))
