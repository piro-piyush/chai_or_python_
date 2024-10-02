# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Size : ")
order_size = order_size.capitalize()
extra_shot = input("Enter True if you need extra shot of espresso else False : ")

if extra_shot == "True":
    coffee = order_size + " Coffee with an extra shot"
else:
    coffee = order_size + " Coffee"

print("Order : ", coffee)
