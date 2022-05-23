my_string = input("enter text")
i = 0
result = ""
for c in my_string:
    if c.isupper() and i > 0:
        result += " "
        result += c.lower()
    else:
        result += c
    i += 1

print(result)