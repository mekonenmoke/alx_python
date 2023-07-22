#!/usr/bin/python3
# Call the add function and print the result
a = 1
b = 2
print("{} + {} = {}".format(a, b, __import__("add_0").add(a, b)))
