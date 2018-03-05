class Dog() :

    #class object attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

# mydog = Dog(breed='Lab', name='Sammy')
mydog = Dog('Lab', 'Sammy')
print(mydog.breed, mydog.name)
print(mydog.species)
