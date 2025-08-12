value = 1

# This is a simple while loop that prints numbers from 1 to 9
# while value <= 10:
#     print(value)
#     value += 1

# The loop will break when value is equal to 5
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# The loop will skip the number 5 and continue printing the rest of the numbers until 10
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)

names = ["Alice", "Bob", "Charlie", "David"]
actions = ["run", "jump", "swim"]

# This for loop iterates through the list of names and prints each name
# for x in names:
#     print(x)

# This for loop iterates through the list of names and breaks when it encounters "Bob"
# for name in names:
#     if name == "Bob":
#         break
#     print(name)

# This for loop uses the range function to print numbers from 0 to 10
# for i in range(0, 11):
#     print(i)

# This for loop uses the range function to print numbers from 0 to 100 in steps of 10
# for i in range(0, 100, 10):
#     print(i)

for name in names:
    for action in actions:
        print(f"{name} {action}")
