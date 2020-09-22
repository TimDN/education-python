def say_hello(name):
    print("Hello {}!".format(name))

def combine_name(fname, sname, mname = ""):
    return "{} {} {}".format(fname, mname, sname)

def read_number():
    number = input("Give number: ")
    if is_special_operator(number):
        handle_special_operator(number)
    else:
        return float(number)

def read_operator():
    operator = input("Give operator: ")
    if is_special_operator(operator):
        handle_special_operator(operator)
    else:
        return operator

def handle_special_operator(operator):
    pass

def is_special_operator(operator):
    if operator == "c" or operator == "x":
        return True
    return False

number_1 = read_number()
operator = read_operator()
number_2 = read_number()

say_hello("World") # prints Hello World
say_hello("Foo") # prints Hello Foo

full_name = combine_name("Tim", "Nielsen", "Daldorph")
print(full_name) # prints Tim Daldorph Nielsen
full_name = combine_name(sname="Nielsen", fname="Tim")
print(full_name) # prints Tim Nielsen