""" this is python tutorial """
import math  # math module for mathematical functions
# ? course = "python"
# ? length = len(course)
# ? print(len(course))
# ? print(length)
# prints the first letter
# ? print(course[0])
# prints last letter
# ? print(course[-1])
# prints the letters from 1 to 3
# ? print(course[0:3])

# ? fname = "amal"
# ? lname = "pillai"

# traditional way of concatination
# ? full = fname+" "+lname
# ? print(full)

# this is formatted string also a way of concatination
# we can use built-in fns like len() inside here
# ? full_name = f"{len(fname)} {fname} {lname}"
# ? print(full_name)

# to upper case
# ? print(course.upper())
# ? print(course.find("t"))
# ? print(course.replace("p", "j"))

# ? print("py" in course)

# to round of a number
# ? number = 3
# ? print(round(number))

# absolute value
# ? neg_num = -6
# ? print(abs(neg_num))

# math.ceil will give the ceiling value of the number
# ? print(math.ceil(number))


# Typeconvertion
# ? x = input("x: ")
# ? print(type(x))
# ? y = int(x)+1
# ? print(f"x: {x}, y: {y}")

# ? if number < 2:
# ?     print("number is lesser than 2")
# ? elif number > 2:
# ?     print("number is greater than 2")
# ? else:
# ?     print("NaN")

# ternary operator
number = 0
# ?message = "greater" if number > 5 else "lesser"
# ? print(message)

# logical operator #!and
# ?if number > 0 and number != 0:
# ?     print("number is positive")
# ? elif number < 0 and number != 0:
# ?    print("number is negative")
# ?else:
#  ?   print("number is 0")

# FOR loop
# ?for i in range(3):
# ?     print(i)

# for else
'''success = False
for i in range(1, 4):
    print("attempt", i)
    if success:
        print("success")
        break
else:
    print("attempted 3 times & failed")'''

# nested loop
'''for x in range(1, 3):
    for y in range(1, 3):
        print(f"{x},{y}")'''

# while loop
command = ""
while command.lower() != "quit":
    command = input(">")
    print("echo", command)
