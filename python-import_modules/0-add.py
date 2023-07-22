#!/usr/bin/python3
# Call the add function and print the result
if __name__ == "__main__":
    a = 1
    b = 2
    add = __import__("add_0").add
    print("{} + {} = {}".format(a, b, add(a, b)))
