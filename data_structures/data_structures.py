def list_example():
    inputs = [] # empty list
    inputs = [0, 1, 2] # list with start values
    print(inputs) # prints [0, '1', 2]
    inputs.append(3)
    inputs[1] = 1
    # changes the value of index 1 ("1")
    print(inputs) # prints [0, 1, 2, 3]

def list_extended():
    inputs = [0, 1]
    print(len(inputs)) # prints 2
    inputs = inputs + [2, 3]
    print(inputs) # prints [0, 1, 2, 3]
    if 0 in inputs:
        print("0 is in inputs") # will be printed
    inputs.remove(0) # removes the first 0 in list
    print(inputs) # prints [1, 2, 3]
    del inputs[1] # del index 1 (2)
    print(inputs) # prints [1, 3]
    print(', '.join(inputs)) # prints 1, 3

def slicing_example():
    string = "0123"
    skip_first = string[1:]
    print(skip_first) # prints 1, 2, 3
    sequence = [0, 1, 2, 3]
    skip_first = sequence[-3:]
    print(skip_first) # prints [1, 2, 3]

def dictionary_example():
    car = {} # empty dict
    car = {
        "brand": "Lancia",
        "model": "Delta S4"
    } # dict with start values
    print(car["brand"]) # prints Lancia
    car["year"] = 1985
    print(car)
    #prints {'brand': 'Lancia', 'model': 'Delta S4', 'year': 1985}

def dictionary_extended():
    car = {
        "brand": "Lancia",
        "model": "Delta S4"
    }
    print(len(car)) # prints 2
    if "brand" in car:
        print(car["brand"]) # prints Lancia, will be printed
    del car["brand"] # deletes the key-value pair "brand"
    brand = car.get("brand", "No brand set")
    # brand does not exists will return default "No brand set"
    print(brand) #prints No brand set

def out_of_range_list_error():
    inputs = [0, 1]
    print(inputs[2]) # raises IndexError: list index out of range

def out_of_range_dict_error():
    car = {
        "brand": "Lancia"
    }
    print(car["model"]) # raises KeyError : model

def handling_out_of_range():
    inputs = [0, 1]
    index = 3
    if 0 <= index < len(inputs): # if 0 <= index and index < len(inputs)
        print("Index in range")
    else:
        print("Index out of range") # will be printed

def handling_key_error():
    car = {
        "brand": "Lancia"
    }
    model = car.get("model", "No model set")
    print(model) # prints "No model set"

print("list_examples")
list_example()
print("list_extended")
list_extended()
print("slicing_example")
slicing_example()
print("dictionaries_example")
dictionary_example()
print("dictionary_extended")
dictionary_extended()
try:
    out_of_range_list_error()
except Exception as e:
    print(e)
try:
    out_of_range_dict_error()
except Exception as e:
    print(e)

handling_out_of_range()
handling_key_error()

