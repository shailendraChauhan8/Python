# Define a base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return f"{self.name} is {self.age} years old"

# Define a subclass that inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"{super().__str__()} and is a {self.breed}"

# Define another subclass that inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

    def __str__(self):
        return f"{super().__str__()} and is {self.color} in color"

# Create instances of Dog and Cat
dog = Dog(name="Buddy", age=3, breed="Golden Retriever")
cat = Cat(name="Whiskers", age=2, color="Tabby")

# Call methods on the instances
print(dog)         # Output: Buddy is 3 years old and is a Golden Retriever
print(dog.speak()) # Output: Buddy says Woof!

print(cat)         # Output: Whiskers is 2 years old and is Tabby in color
print(cat.speak()) # Output: Whiskers says Meow!

# Demonstrate polymorphism
animals = [dog, cat]
for animal in animals:
    print(animal)    # Calls __str__ method
    print(animal.speak())  # Calls speak method
