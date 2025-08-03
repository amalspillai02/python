""" this is python tutorial """
course = "python"
length = len(course)
print(len(course))
print(length)
print(course[0])  # prints the first letter
print(course[-1])  # prints last letter
print(course[0:3])  # prints the letters from 1 to 3

fname = "amal"
lname = "pillai"
full = fname+" "+lname  # traditional way of concatination
print(full)

# this is formatted string also a way of concatination
# we can use built-in fns like len() inside here
full_name = f"{len(fname)} {fname} {lname}"
print(full_name)

print(course.upper())  # to upper case
print(course.find("t"))
print(course.replace("p", "j"))

print("py" in course)
