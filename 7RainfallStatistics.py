months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainful_statistic = []
for i in months:
    rs = int(input(i + ' rainfall statistic: '))
    rainful_statistic.append(rs)

total_rainfull = 0
for k in rainful_statistic:
    total_rainfull += k


print('total rainfull ' + str(total_rainfull))
print('average ' + str((total_rainfull/12)))
print('highest ' + str(max(rainful_statistic)))
print('lowest ' + str(min(rainful_statistic)))

