class User:
    def __init__(self, id, name = ""): # ctor taking two parameters
        self.id = id # instance variable
        self.name = name # instance variable
        self.test = "Test" # instance variable

    def change_name(self, new_name): # class methods that take one parameter
        self.name = new_name # access instance variables using self

foo = User(1, "Foo")
bar = User(2) # Name is an optional parameter
print(foo.id, foo.name, foo.test) # Prints 1 Foo Test
print(bar.id, bar.name, bar.test) # Prints 2 Test
bar.change_name("Bar") # call function change_name for bar instance of User
print(bar.name) # Prints Bar


