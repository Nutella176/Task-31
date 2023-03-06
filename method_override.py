# Adult class that takes name, age, eye colour and hair colour as attributes
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # Adult class method that prints the person's name and that they are old enough to drive
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")


# Subclass with the same attributes as the Adult class
class Child(Adult):
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    # Child class method which overrides the can_drive method to print that person is too young to drive
    def can_drive(self):
        print(f"{self.name} is too young to drive.")


# Asking user to input name, age, hair colour, and eye colour of a person
name = input("Please enter a person's name: ").title()
age = int(input("Please enter their age: "))
eye_colour = input("Please enter their eye colour: ")
hair_colour = input("Please enter their hair colour: ")

# Condition statement which creates an instance of either an Adult or Child class depending on the person's age
if age >= 18:
    adult = Adult(name, age, eye_colour, hair_colour)
    adult.can_drive()
else:
    child = Child(name, age, eye_colour, hair_colour)
    child.can_drive()
