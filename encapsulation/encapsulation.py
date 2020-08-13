class Person: #public class
    def __init__(self, name):
        self.__name = name #private instance variable

    def _get_info(self): # protected
        return "Name {}".format(self.__name)

    def print_info(self): # public
        print(self._get_info())

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name) # calling constructor is ok
        self.__grade = grade # private so that we can validate

    @property
    def grade(self): # public
        return self.__grade # accessing private variable

    @grade.setter
    def grade(self, value): # public
        if value in ["G", "VG"]:
            self.__grade = value # setting private variable
        else:
            raise ValueError("Non valid grade", value)

    def print_info(self): # public overload
        info = self._get_info() # calling protected is ok from super class
        print("{}, Grade {}".format(info, self.__grade))

foo = Student("Foo Bar", "G")
foo.grade = "VG"
foo.print_info() # Prints Name Foo Bar, Grade VG

