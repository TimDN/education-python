# Global variable
foo = "foo"
if foo == "foo":
    bar = "bar" #Global variable

# Global function
def global_function(world): # parameters are local
    hello = "hello" # local variable

global_function("world")

print(foo) # prints foo
print(bar) # prints bar

print(hello) # NameError: name 'hello' not defined
print(world) # NameError: name 'world' not defined

def main():
    print("Hello main!") # will be printed

if __name__ == "__main__":
    main() # call the main function

