def hello(name='Melanie') :
    print('The hello() function has been executed')

    def greet() :
        return '\t This is inside the greet() function'

    def welcome() :
        return '\t This is inside the welcome function'

    # print(greet())
    # print(welcome())
    # print('Now we are back inside the hello() function')

    if name == 'Melanie' :
        return greet() #returns result of greet function
    else :
        return welcome #returns function not result of function

x = hello() #executes hello()
print(x)
