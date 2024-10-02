# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).


pet = input("Pet type : ")
age = int(input("Pet age : "))

pet = pet.capitalize()

if pet == "Dog":
    if age < 2:
        print("Puppy Food")
elif pet == "Cat":
    if age > 5:
        print("Senior Cat Food")
