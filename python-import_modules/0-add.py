#!/usr/bin/python3
def main():
    add = __import__("add_0").add
    a = 1
    b = 2
    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))


if __name__ == "__main__":
    main()
