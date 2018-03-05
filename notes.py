# def hello(name="Melanie") :
#     return "hello " + name
#
# print(hello())
#
# mynewgreet = hello
#
# print(mynewgreet())

def hello(name="Melanie") :
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet() :
        return "THIS STRING IS INSIDE GREET()"

    def welcome() :
        return "THIS STRING IS INSIDE WELCOME()"

    # print(greet())
    # print(welcome())
    # print("End of hello")

    if name == "Melanie" :
        return greet
    else :
        return welcome

x = hello()

print(x())
