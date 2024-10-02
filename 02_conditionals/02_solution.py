# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int((input("Enter Your age : ")))
day = "Wednesday"

price = 12 if age >= 18 else 8

print(price)

discount = 2 if day == "Wednesday" else 0

Total_price = price - discount

print("Amount to be paid $", Total_price)
