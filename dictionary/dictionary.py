user1 = {
    "name": "John Doe",
    'age': 30,
    'height': 5.9,
    'is_student': False,
}
user2 = dict(name="George", age=25, height=5.5, is_student=True)
print(user1)
print(type(user1))
print(len(user1))

# Accessing values in the dictionary
print(user1['name'])
print(user1.get('age'))

# to get keys of the dictionary
print(user1.keys())

# to get values of the dictionary
print(user1.values())

# to verify if a key exists in the dictionary
print("name" in user1)

# updating value
user1['age'] = 31
# updating or adding value using update method
user1.update({"gender": "male"})
print(user1)

# removing a key-value pair
user1.pop('is_student')
print(user1)
# or
user1['is_student'] = True
print(user1)
user1.popitem()  # removes the last inserted key-value pair
print(user1)

# deleting a key-value pair
del user1['height']
print(user1)

print(user2)
# clears the dictionary
# user2.clear()
# print(user2)

# Copying a dictionary
user_copy = user1.copy()
print(user_copy)

# Nested dictionaries
nested_dict = {
    "key1": user1,
    "key2": user2,
}
print(nested_dict)
