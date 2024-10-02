# Problem: Reverse a string using a loop.

string = input("Enter String : ")

rev_string = ""

for char in string:
    rev_string = char + rev_string
print(rev_string)
