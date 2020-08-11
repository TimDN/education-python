class User:
    def __init__(self, id):
        self.__id = id # the name will be used by prop use __
        self.__name = "N:A" # the name will be used by prop use __

    @property # getter for id no setter can not be changed
    def id(self):
        return self.__id

    @property # getter for name
    def name(self):
        return self.__name

    @name.setter # setter for name
    def name(self, value):
        print("Changing name to {}".format(value))
        self.__name = value

foo = User(1)
print(foo.id) # prints 1
print(foo.name) # prints N:A
foo.name = "Foo"
#print Changing name to Foo
print(foo.name) # prints Foo

