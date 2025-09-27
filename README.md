# PythonCollections-Arrays-
# Python Collections: List, Tuple, Set, Dictionary

Python provides four main types of collections. Each has unique properties and use cases. Below you will find detailed explanations with examples.

---

## 1. List

**Properties:**
- Ordered
- Changeable (mutable)
- Allows duplicate elements

### Python Example
```python
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
```

---

## 2. Tuple

**Properties:**
- Ordered
- Unchangeable (immutable)
- Allows duplicate elements

### Python Example
```python
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
```

---

## 3. Set

**Properties:**
- Unordered
- Unindexed
- No duplicate elements
- Elements cannot be changed, but items can be added or removed

### Python Example
```python
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
```

---

## 4. Dictionary

**Properties:**
- Ordered (since Python 3.7)
- Changeable (mutable)
- No duplicate keys

### Python Example
```python
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
```

---

## Summary
- **List** → Ordered, mutable, allows duplicates.
- **Tuple** → Ordered, immutable, allows duplicates.
- **Set** → Unordered, unindexed, no duplicates.
- **Dictionary** → Ordered, mutable, unique keys.

These are the four fundamental collection types in Python.

---

## For GitHub (README.md)
The code snippets above are ready for use in a `README.md` file for GitHub documentation.

## For Python Scripts
Each section’s code can be saved separately into `.py` files (e.g., `list_example.py`, `tuple_example.py`, etc.) to run and test individually.
