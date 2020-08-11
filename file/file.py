def basic_example():
    f = open("test.txt", "a+")
    # Open or creates the file text.txt with mode w+
    f.write("Test line")
    # writes Test line to the file
    f.close()
    # closes the file handle so that other processes can use it

def save_try_open():
    # safe way to use open close
    try:
        f = open("try_test.txt", "w")
        f.write("Test Line")
    finally:
        # will always be closed
        f.close()

def with_open():
    with open("with_test.txt", "w+") as f:
        f.write("Test line")
    # file handle is closed when moving out of block
    print(f.read()) # Raise exception
    # ValueError: I/O operation on closed file

def extended_example():
    f = open("file.txt", "w")
    f.write("Hello\n")
    f.write("World")
    f.close()
    # If it was not closed next open would cause exception

    # read entire file
    f = open("file.txt", "r")
    print(f.read())
    # prints Hello
    # World
    f.close()

    # read file line by line
    f = open("file.txt")
    for line in f:
        if line == "World":
            print("Found", line)
            # prints Found World
    f.close()

basic_example()
extended_example()
save_try_open()
with_open()