s = 'This is a global variable'

def func() :
    print(locals())

def hello(name='Melanie') :
    return 'Hello ' + name

print(func())
# print(globals().keys())
print(globals()['s'])
print(hello())

greet = hello
del hello
print(greet)
print(greet())
print(hello()) #hello is now not defined, but greet is still in memory
