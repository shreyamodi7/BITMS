sample_string = "Hello, World! How are you today?"


print("Length of the string:", len(sample_string))

print("Capitalized string:", sample_string.capitalize())

print("Uppercase string:", sample_string.upper())

print("Lowercase string:", sample_string.lower())

substring = "o"
print("Occurrences of '{}' in the string:".format(substring), sample_string.count(substring))

substring = "World"
print("Index of '{}' in the string:".format(substring), sample_string.find(substring))

old_substring = "Hello"
new_substring = "Hi"
print("String after replacement:", sample_string.replace(old_substring, new_substring))

delimiter = " "
print("Split string:", sample_string.split(delimiter))

substring = "Hello"
print("Does the string start with '{}'?".format(substring), sample_string.startswith(substring))

substring = "today?"
print("Does the string end with '{}'?".format(substring), sample_string.endswith(substring))

print("Is the string alphanumeric?", sample_string.isalnum())

print("Is the string alphabetic?", sample_string.isalpha())

print("Is the string numeric?", sample_string.isdigit())
