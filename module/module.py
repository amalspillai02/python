from random import choice

names = ['amal', 'aswin', 'nandhu']


def print_names():
    index = choice("012")
    print(names[int(index)])
