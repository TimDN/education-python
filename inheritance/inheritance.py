class Person:
    def __init__(self, first_name, last_name, adress, email):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.email = email

    def get_info(self):
        return "Name {} {}, Adress {}, Email {}".format(
            self.first_name, self.last_name, self.adress, self.email
        )

    def print_info(self):
        print(self.get_info())

class Student(Person): # notice the Person base class
    def __init__(self, first_name, last_name, adress, email, grade):
        super().__init__(first_name, last_name, adress, email)
        # call base class Persons constructor
        self.grade = grade

    def print_info(self): # overloads base class print_info
        info = self.get_info() # calls base class function
        print("{}, Grade {}".format(info, self.grade))

foo = Student("Foo", "Bar", "Osman", "Foo@mail.com", "VG+")
foo.print_info() # calls students version of print info
# prints Name Foo Bar, Adress Osman, Email Foo@mail.com, Grade VG+

