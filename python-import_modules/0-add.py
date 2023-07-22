# Step 3: Define the variables a and b
a = 1
b = 2

# Step 4: Import the add function from add_0.py
from add_0 import add

# Step 5: Call the add function and print the result
result = add(a, b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, result))
