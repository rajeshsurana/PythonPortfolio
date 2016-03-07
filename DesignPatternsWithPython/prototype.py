import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_objects(self, name, obj):
        ''' Register an object '''
        self._objects[name] = obj

    def unregister_objects(self, name):
        ''' Unregister an object '''
        del self._objects[name]

    def clone(self, name, **kwargs):
        '''Clone a registered object and update its attributes '''
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(kwargs)
        return obj

class Car():
    def __init__(self):
        self.name_car = 'Skylark'
        self.color = 'Red'
        self.options = 'Ex'

    def __str__(self):
        return '{} | {} | {}'.format(self.name_car, self.color, self.options)

# create new car
car = Car()

# create new prototype object
prototype = Prototype()

# register car object
prototype.register_objects('skylark', car)

c1 = prototype.clone('skylark', name_car = 'Fierce', color = 'Black', options='Limited')
print(c1)
