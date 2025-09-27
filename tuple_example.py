#authors Mohd R. Panah, give star when use the code! and follow
# tuple_example.py
# Example demonstrating Python Tuple

# Defining a tuple
my_tuple = (10, 20, 30, 20, 40)
print("Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuples are immutable
# my_tuple[1] = 25  # This will raise an error

# Workaround: convert to list, modify, then back to tuple
temp_list = list(my_tuple)
temp_list[1] = 25
my_tuple = tuple(temp_list)
print("Modified Tuple:", my_tuple)

# Length of tuple
print("Length of tuple:", len(my_tuple))
