class Pet:
    print("Pet class created")
pet_object = Pet()
class PetProfile:
    category = "pet"
    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.aniaml_type = animal_type
        self.age = age
        self.favourite_food = favourite_food
pet1 = PetProfile("Max", "Dog", 3, "Chiken")
pet2 = PetProfile("Luna", "Cat", 2, "Fish")
print(pet1.category)
print(pet2.category)
print(pet1.name)
print(pet1.aniaml_type)
print(pet1.age)
print(pet1.favourite_food)
print(pet2.name)
print(pet2.aniaml_type)
print(pet2.age)
print(pet2.favourite_food)