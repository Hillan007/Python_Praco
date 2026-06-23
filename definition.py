def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add three numbers and print the result.")
    parser.add_argument('a', type=float, nargs='?', help='first number', default=3.0)
    parser.add_argument('b', type=float, nargs='?', help='second number', default=4.0)
    parser.add_argument('c', type=float, nargs='?', help='third number', default=5.0)
    args = parser.parse_args()

    adding(args.a, args.b, args.c)

