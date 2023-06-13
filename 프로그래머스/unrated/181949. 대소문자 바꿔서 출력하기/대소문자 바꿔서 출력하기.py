str1 = input()
str2 = ""
for i in str1:
    if i.isupper():
        str2 += i.lower()
    elif i.islower():
        str2 += i.upper()
print(str2)
    