#!/usr/bin/python3
# Call the add function and print the result
add = __import__("add_0").add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
