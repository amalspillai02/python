# example of list
users = ['amal', 'unni', 'sreeja', 'sreelakshmi', 'sreerag', 'sreehari']
data = ['achu', 18, True]

# This will check if 'amal' is in the users list
# and print the result
print("amal" in users)
print(18 in data)

# This will print the first element of the data list
print(data[0])

# This will print the index of 'sreeja' in users list
print(users.index('sreeja'))
print(data.index(True))

# prints first three elements
print(users[0:3])

# prints the length of users list
print(len(users))

# This will append 'new_data' to the data list
data.append('new_data')
print(data)

# This will extend the users list with the data list
# users.extend(data)
# print(users)

# This will insert 'new_user' at the beginning of the users list
users.insert(0, 'new_user')
print(users)

# This will remove 'sreeja' from the users list
# and print the updated list
users.remove('sreeja')
print(users)

# prints the users list in sorted order
users.sort()
print(users)

# This will sort the users list in a case-insensitive manner
users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]

# prints the nums in reverse order
# nums.reverse()
# print(nums)

# This will sort the nums list in ascending order
# nums.sort()
# print(nums)

# This will sort the nums list in descending order
# nums.sort(reverse=True)
# print(nums)

# prints the nums list in ascending order without modifying the original list
print(sorted(nums))

# prints the nums list in descending order without modifying the original list
print(sorted(nums, reverse=True))
