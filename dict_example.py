#authors Mohd R. Panah, give star when use the code! and follow
# dict_example.py
# Example demonstrating Python Dictionary

# Defining a dictionary
my_dict = {
    "name": "Ali",
    "age": 25,
    "city": "Kabul"
}
print("Original Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict["name"])

# Modifying a value
my_dict["age"] = 26
print("After modifying age:", my_dict)

# Adding a new key-value pair
my_dict["job"] = "Engineer"
print("After adding job:", my_dict)

# Removing a key
my_dict.pop("city")
print("After removing city:", my_dict)

# Looping through dictionary
for key, value in my_dict.items():
    print(key, ":", value)
