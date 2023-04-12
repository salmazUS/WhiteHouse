class Finger:
    # private variable
    __private_variable = 123.9

    # public variable
    public_variable = "Public uzma Variable"

    # constructor
    def __init__(self):
        pass

    # function
    def some_function(self):
        print("This is a function")

    # method
    def some_method(self):
        print("This is a method")
        print(self.__private_variable)
        vvv = type(self.__private_variable)
        print(vvv)
    # private method
    def __private_method(self):
        print("This is a private method")


# create object of SampleClass
obj = Finger()
print("=======")
print(type(obj))
print("=======")
LittleFinger = Finger()
# calling some_function
obj.some_function()

# calling some_method
obj.some_method()
some_method()
# calling private method
#obj.__private_method()

# accessing public variable
abc = obj.public_variable
print(abc)

# accessing private variable
#print(obj._SampleClass__private_variable)