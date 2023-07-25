#!/usr/bin/python3
import add_0


def main():
    a = 1
    b = 2
    result = add_0.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))


if __name__ == "__main__":
    main()
