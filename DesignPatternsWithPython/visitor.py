class House(object): #The class being visited
    def accept(self, visitor):
        '''Interface to accept a visitor'''
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        '''Simply return the class name when the House object is printed'''
        return self.__class__.__name__

class Visitor(object):
    '''Abstract visitor'''
    def __str__(self):
        '''Simply return the class name when the Visitor object is printed'''
        return self.__class__.__name__

class HvacSpecialist(Visitor): #Inherit from the parent class Visitor
    '''Concrete visitor: HVAC specialist'''
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor): #Inherit from the parent class Visitor
    '''Concrete visitor: Electrician'''
    def visit(self, house):
        house.work_on_electricity(self)

#create on HVAC specialist
hv = HvacSpecialist()
#creae an electrician
e = Electrician()

#create a house
home = House()

#Let the house accept the HVAC specialist and work on the house by invoking the visit mehtod()
home.accept(hv)

#Let the house accept the HVAC specialist and work on the house by invoking the visit mehtod()
home.accept(e)    
