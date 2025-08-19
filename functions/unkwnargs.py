# Function to handle unknown arguments.
def unkwnargs(*args):
    print(args)
    print(type(args))


unkwnargs('amal', 'unni', 1)


# Function to handle unknown keyword arguments.
def unkwnkwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))


unkwnkwargs(name='amal', age=25, city='Kochi')
