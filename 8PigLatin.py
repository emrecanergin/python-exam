words = str(input("Input Sentence:")).split()
for word in words:
    print(word[1:] + word[0] + "AY", end = " ")
print ()