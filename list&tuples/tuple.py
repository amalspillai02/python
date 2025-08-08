# This code defines a tuple with mixed data types and prints it along with its type.
mytuple = ('amal', 'sree', 'kumar', 25, 5.6, True)
print(mytuple)
print(type(mytuple))

# This code unpacks the tuple into individual variables and prints them.
(one, two, *rest) = mytuple
print(one)
print(two)
print(rest)
