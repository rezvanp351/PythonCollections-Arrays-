#authors Mohd R. Panah, give star when use the code! and follow
# set_example.py
# Example demonstrating Python Set

# Defining a set
my_set = {10, 20, 30, 20, 40}
print("Original Set:", my_set)  # duplicates are removed

# Adding an element
my_set.add(50)
print("After add:", my_set)

# Removing an element
my_set.remove(30)
print("After remove 30:", my_set)

# Membership test
print("Is 20 in set?", 20 in my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
