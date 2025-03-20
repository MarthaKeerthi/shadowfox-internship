class Person:
    # Constructor method to initialize the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display person's information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    # Method to greet the person
    def greet(self):
        print(f"Hello, {self.name}! Welcome to the program.")

# Create objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
# Access and display the details of each person
print("Details of Person 1:")
person1.display_info()
person1.greet()
print("\nDetails of Person 2:")
person2.display_info()
person2.greet()
