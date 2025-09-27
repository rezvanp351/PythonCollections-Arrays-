#authors Mohd R. Panah, give star when use the code! and follow
# list_example.py
# Example demonstrating Python List

# Defining a list
my_list = [10, 20, 30, 20, 40]
print("Original List:", my_list)

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modifying an element
my_list[1] = 25
print("After changing index 1:", my_list)

# Adding an element
my_list.append(50)
print("After append:", my_list)

# Removing an element
my_list.remove(20)  # removes the first occurrence of 20
print("After remove 20:", my_list)

# Length of list
print("Length of list:", len(my_list))
