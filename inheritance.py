# Base class
class Animal:
    def __init__(self, species):
        self.species = species
    def make_sound(self):
        print("This animal makes a sound.")
# Derived class
class Dog(Animal):
    def __init__(self, species, breed):
        # Call the constructor of the base class
        super().__init__(species)
        self.breed = breed
    # Overriding the base class method
    def make_sound(self):
        print("Woof! Woof!")
    # New method specific to the Dog class
    def fetch(self):
        print(f"The {self.breed} is fetching the ball.")
# Create an object of the base class
animal = Animal("General Animal")
print(f"Species: {animal.species}")
animal.make_sound()
print("\n")
# Create an object of the derived class
dog = Dog("Dog", "Golden Retriever")
print(f"Species: {dog.species}")
print(f"Breed: {dog.breed}")
dog.make_sound() 
dog.fetch()       