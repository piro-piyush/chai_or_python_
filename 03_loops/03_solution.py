# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter num :"))

for i in range(1, 11):
    if i == 5:
        continue
    print(num, "X", i, "=", num * i)
