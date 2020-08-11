def say_hello(name):
    print("Hello {}!".format(name))

say_hello("World") # prints Hello World
say_hello("Foo") # prints Hello Foo


def combine_name(fname, sname, mname = ""):
    return "{} {} {}".format(fname, mname, sname)

full_name = combine_name("Tim", "Nielsen", "Daldorph")
print(full_name) # prints Tim Daldorph Nielsen
full_name = combine_name(sname="Nielsen", fname="Tim")
print(full_name) # prints Tim Nielsen