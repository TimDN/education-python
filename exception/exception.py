# Will read input until a number is entered
def read_number_from_user():
    valid_number = False
    while not valid_number:
        try:
            number = int(input("Enter number:"))
            valid_number = True
        except ValueError as e:
            print("Can't convert. Message {}".format(e))
        except Exception as e:
            print("Unkown error. Message {}".format(e))
    return number

number = read_number_from_user()

def divide(x, y):
    try:
       result = x / y
       print("result is", result)
    except ZeroDivisionError:
        print("division by zero!")
    finally:
        print("executing finally clause")

divide(2, 1)
# prints result is 2.0
# executing finally clause
divide(2, 0)
# division by zero!
# executing finally clause

