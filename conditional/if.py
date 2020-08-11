def if_example():
    if True:
        print("Condition is True")
        # Will be printed
    else:
        print("Condition is false")
        # Will not be printed
    print("If block completed")
    # Will be printed

def relational_operators():
    if 1 != 2:
        print("Not equal")
        # Will be printed
    if 1 < 2:
        print("Less than")
        # Will be printed
    if 1 <= 1:
        print("Less than or equal")
        # Will be printed
    if 2 > 1:
        print("Greater than")
        # Will be printed
    if 2 >= 2:
        print("Greater than or equal")
        # Will be printed

def conditional_operators():
    if True and True:
        print("True and True == True")
        # Will be printed
    if True or False:
        print("True or False == True")
        # Will be printed
    if False or True:
        print("False or True == True")
        # Will be printed
    if not False:
        print("not False == True")
        # Will be printed

def elif_example():
    if False:
        print("If statement")
    elif False:
        print("First elif statement")
    elif True:
        print("Second elif statement")
        # Will be printed
    else:
        print("Else statement")



if_example()
relational_operators()
conditional_operators()