def for_examples():
    numbers = [0, 1 ,2]

    for i in numbers:
        print(i)
    for i in range(3):
        print(i)
    # Both of these will print
    # 0
    # 1
    # 2

    hello = "Hello"
    for char in hello:
        print(char)
    # Prints
    # H
    # e
    # l
    # l
    # 0

def while_examples():
    i = 0
    # print i while i is less than 3
    while i < 3:
        print(i)
        i += 1
    # prints
    # 0
    # 1
    # 2

def dictionary_for_loop():
    car = {
        "brand": "Lancia",
        "model": "Delta S4"
    }
    for key in car:
        print(key, car[key]) # prints the key and value

    for value in car.values():
        print(value) # prints the value

    for key, value in car.items():
        print(key, value) # prints the key and value

for_examples()
while_examples()
dictionary_for_loop()