#!/usr/bin/python3
# Call the add function and print the result
if __name__ == "__main__":
    # add = __import__("add_0").add
    from add_0 import add 
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
