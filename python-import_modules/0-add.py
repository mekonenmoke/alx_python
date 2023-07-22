# Call the add function and print the result
if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add

    # Define the variables a and b
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
