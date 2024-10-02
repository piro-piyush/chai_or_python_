# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter number : "))
sum = 0

for num in range(1, n + 1):
    if num % 2 == 0:
        sum += 1
print("Sum of even number : ", sum)
