# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Password : ")

length = len(password)

# print(length)

if length < 6:
    print("Weak")
elif length < 10:
    print("Medium")
elif length > 10:
    print("Strong")
