def main():
    convert_2()

def convert_1():
    celsius = 30 # 86
    fahr = 50 # 10
    target_unit = input("Target unit cel/fahr")
    conver = Conversion_1()
    if target_unit == "cel":
        print(conver.fahrToCel(fahr))
    else:
        print(conver.celToFahr(celsius))

def convert_2():
    degree = 50
    target_unit = "cel"
    convert = Conversion_2()
    print(convert.convert_to(degree, target_unit))

class Conversion_1():
    def celToFahr(self, celsius):
        return celsius * 1.8 + 32

    def fahrToCel(self, fahr):
        return (fahr - 32) / 1.8

class Conversion_2():
    def __celToFahr(self, celsius):
        return celsius * 1.8 + 32

    def __fahrToCel(self, fahr):
        return (fahr - 32) / 1.8

    def convert_to(self, degree, given_unit, target_unit):
        if target_unit == "cel":
            return self.__fahrToCel(degree)
        elif target_unit == "fahr":
            return self.__celToFahr(degree)
        elif target_unit == "kelvin":
        else:
            raise Exception()

if __name__ == "__main__":
    main()