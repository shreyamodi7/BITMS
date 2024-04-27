# Sets
print("Sets Example:")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union of sets
union_set = set_a.union(set_b)
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print("Intersection of sets:", intersection_set)

# Difference of sets
difference_set = set_a.difference(set_b)
print("Difference of sets:", difference_set)

# Tuples
print("\nTuples Example:")
tuple_a = (1, 2, 3, 4, 5)
tuple_b = ('a', 'b', 'c', 'd', 'e')

# Accessing elements in a tuple
print("First element of tuple_a:", tuple_a[0])
print("Last element of tuple_b:", tuple_b[-1])

# Lists
print("\nLists Example:")
list_a = [1, 2, 3, 4, 5]
list_b = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Appending an element to a list
list_a.append(6)
print("List after appending element:", list_a)

# Removing an element from a list
list_b.remove('cherry')
print("List after removing element:", list_b)

# Strings
print("\nStrings Example:")
string_a = "Hello"
string_b = "World"

# Concatenating strings
concatenated_string = string_a + " " + string_b
print("Concatenated string:", concatenated_string)

# Accessing characters in a string
print("First character of string_a:", string_a[0])
print("Last character of string_b:", string_b[-1])
