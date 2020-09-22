class Person: # create a class with name person
    first_name = "Foo" # class variable

foo = Person() # Create a Person object and assign it to the foo variable
bar = Person() # Create a Person object and assign it to the bar variable
print(foo.first_name) #prints Foo
print(bar.first_name) #prints Foo
bar.first_name = "Bar" # changing first_name of this Person instance
print(foo.first_name) #prints Foo (no change)
print(bar.first_name) #prints Bar (changed)
test = Person()
