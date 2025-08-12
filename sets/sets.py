set1 = {1, 2, 3, 4, 5}
print(set1)
print(len(set1))

# This will not add duplicates, as sets do not allow them
set2 = {7, 8, 9, 10}
print(set2)

# Adding an element to the set
set1.add(6)
print(set1)

set1.update(set2)
print(set1)

set3 = {11, 12, 13}
newset1 = set1.union(set3)
print(newset1)
