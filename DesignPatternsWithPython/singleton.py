class Borg:
    ''' Borg class making class attributes global '''
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    ''' Sub class of Borg class '''
    # This essentially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # returns the attribute dictionary for printing
        return str(self._shared_state)

# Lets create Singleton object
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
# Print the object
print(x)
# Let's create another Singleton object
y = Singleton(SMTP = "Simple Message Transfer Protocol")
print(y)
