ROWS=3
COLS=3

def main():
    values=[[0,0,0],[0,0,0],[0,0,0]]
    for r in range(ROWS):
        for c in range(COLS):
            print('Enter number ', c + 1)
            values[r][c]=int(input('Enter your number'))
        if values[0][0] + values[0][1] + values[0][2] == values[1][0] + values[1][1] + values[1][2] == values[1][0] \
                + values[1][1] + values[1][2] == values[2][0] + values[2][1] + values[2][2] == values[0][2] \
                + values[1][2] + values[2][2] == values[0][0] + values[1][1] + values[2][2]:
            print ('there is magic square')
    print(values)
main()