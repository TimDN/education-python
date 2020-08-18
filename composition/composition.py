class Address:
    def __init__(self, street, city, zipcode, street2='', state = ''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self): # overload print()
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return ', '.join(lines)

# a person has-a address
class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    @property
    def address(self):
        return self.__address

    def __str__(self): #overload print()
        return "Name: {}".format(self.__name)

# a building has-a address and has inhabitants
class Building:
    def __init__(self, address, inhabitants):
        self.__address = address
        self.__inhabitants = inhabitants

    def print_inhabitants(self):
        for inhabitant in self.__inhabitants:
            print(inhabitant)

    @property
    def address(self):
        return self.__address

person_address = Address("Gamla Staden 3", "Göteborg", "48912") # adress must be created separately
person = Person("Foo Bar", person_address) # pass address instance to person
building_address = Address("Gamla Staden 3", "Göteborg", "48912") # adress must be created separately
building = Building(building_address, [person]) # pass address and person instance to building

print(person.address) # prints Gamla Staden 3, Göteborg,  48912
building.print_inhabitants() # prints Name: Foo Bar

