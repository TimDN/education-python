
def init_variable():
    #declares a variable with name age
    user_age = input("Input you age: ")
    user_name = "Tim"
    user_float = 10.12111

    print(f'Hello {user_name}')

    print("Age: {}, Name: {}".format(user_age, user_name))
    print(f"Age: {user_age}, Name: {user_name} ,Test {user_float:.2f}")


def naming_example():
    average_age = 26 #correct
    Average_age = 26 #wrong
    averageAge = 26 #wrong
    average_Age = 26 #wrong

def operators():
    one = 1
    two = 1 + 1
    three = 1 + 1 * 2
    four = (1 + 1) * 2
    two += 2 # equals 4

def operators_variables():
    one = 1
    two = one + one
    three = one + one * two
    four = (one + one) * two
    two += two # equals 4

def int_example():
    four = 4
    print(type(four)) # prints <class 'int'>
    price = 9.99
    print(type(price)) # prints <class 'float'>
    quarter = 3/four # quarter is a float
    print(quarter) # prints 0.75

def str_example():
    hello = "Hello"
    print(type(hello)) # prints <class 'str'>
    world = "World"
    hello_world = hello + world # concatenation
    print(hello_world) # prints HelloWorld

def escape_example():
    single_quoute = "Hello(\") \n World(')"
    double_quote = 'Hello(") \n World(\')'
    tripple_quotes = """Hello(")
World(')"""
    # These string all prints Hello(")
# World(')

def casting_example():
    one = "1"
    two = 1 + int("1") # two is a int with value 2
    twelve = one + str(two)
    # twelve is a str with value "12"

def bool_example():
    is_true = True
    is_false = 1 == 2
    # is false is a bool with value False
    print(1 == 2) # prints False

init_variable()