# Problem: Given a string, find the first non-repeated character.

str = input("Enter string : ")

for char in str:
    print(char)
    if str.count(char) == 1:
        print("Char is : ", char)
        break
