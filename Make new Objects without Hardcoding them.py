class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{name} has been created!".format(name=self.name))

    def __repr__(self):
        return "A person called {name}".format(name=self.name)

    def get_details(self):
        print("This person's name is {name}, and they are {age} years old".format(name=self.name, age=self.age))


#---- Function to create new objects without hard coding them ----

#A list is used to store the objects in
objects = []

#This function generates a new number (the length of the list, as it'll always be changing,
#and then adds that number to the list, then creates an object from the item in the list,
#creating a list full of objects.
def newObject(name, age):
    x = len(objects)
    objects.append(x)
    objects[x] = Person(name, age)


#Testing
newObject("test", 2)
