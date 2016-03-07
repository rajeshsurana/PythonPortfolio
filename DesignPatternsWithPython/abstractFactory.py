class Dog:
    ''' the dog class'''
    def __init__(self, name):
        self._name = name

    def speak(self):
        return 'Woof Woof!'

    def __str__(self):
        return "Dog: " + self._name

class DogFactory:
    ''' Concrete Factory '''
    def get_pet(self):
        ''' Returns a Dog object '''
        return Dog("Lucy")
    def get_food(self):
        ''' Returns a Dog's food '''
        return 'Dog Biscuits'

class PetStore:
    ''' This is a Abstract Factory '''
    def __init__(self, pet_factory=None):
        ''' _pet_factory our Abstract Factory '''
        self._pet_factory = pet_factory

    def show_pet(self):
        ''' Utility method to display details of object '''

        pet = self._pet_factory.get_pet()

        food = self._pet_factory.get_food()

        print("Our pet is {}".format(pet))
        print("Our pet says hello by {}".format(pet.speak()))
        print("Our pet eats {}".format(food))

# create concrete factory
factory = DogFactory()

# create pet store housing our abstract factory
shop = PetStore(factory)

# Invoke utility method to display pet information
shop.show_pet()
        
